from decimal import Decimal

from mongoengine import DoesNotExist

from infrastructure.config import Config
from infrastructure.gateway.github_api_client import GithubApiClient
from infrastructure.logger import logger
from reporting.application.repositories.branch_repo import BranchRepo
from reporting.application.repositories.pull_request_repo import PullRequestRepo
from reporting.models.branch import Branch
from reporting.models.coverage_report import CoverageReport
from reporting.models.gituhub_user import GithubUser
from reporting.models.pull_request import PullRequest
from reporting.models.repository import Repository


class GithubService:

    def __init__(self, repository: str):
        self._github_api_client = GithubApiClient(repository)
        self._repository = repository
        self._branch_repo = BranchRepo(repository)
        self._pull_request_repo = PullRequestRepo(repository)

    def upsert_pull_request(self, github_pull_request_number: str, coverage_report: CoverageReport) -> PullRequest:
        logger.info(f"upserting PR")
        main = self.get_main_branch()
        if main:
            coverage_change = coverage_report.compare(main.coverage_report)
        else:
            coverage_change = Decimal("0")

        try:
            pull_request = self._pull_request_repo.get(github_pull_request_number)
            pull_request.coverage_change = coverage_change
            pull_request.branch.coverage_report = coverage_report
        except DoesNotExist:
            github_pull_request = self._github_api_client.get_pull_request(github_pull_request_number)
            pull_request = PullRequest(github_pull_request_number=github_pull_request_number,
                                       branch=Branch(name=github_pull_request.head.ref,
                                                     coverage_report=coverage_report,
                                                     repository=self._repository),
                                       author=GithubUser(username=github_pull_request.user.login,
                                                         name=github_pull_request.user.name),
                                       repository=Repository(id=self._repository),
                                       coverage_change=coverage_change)

        self._pull_request_repo.upsert(pull_request)
        return pull_request

    def update_main(self, pr_number: str) -> None:
        pr = self._pull_request_repo.get(pr_number)
        main = self.get_main_branch()
        if not main:
            main = pr.branch.model_copy(deep=True)
            main.name = Config.MAIN_BRANCH
            self._branch_repo.upsert(main)
            comment_id = self._github_api_client.post_comment(pr_number, "Congrats! This is the first time you are using our tool!")
            pr.comment_id = str(comment_id)
            return

        self._branch_repo.update_coverage(name=pr.branch.name,
                                          coverage_diff=pr.coverage_change)

    def get_main_branch(self) -> Branch | None:
        try:
            return self._branch_repo.get(Config.MAIN_BRANCH)
        except DoesNotExist:
            return None

    def notify(self, pull_request: PullRequest, content: str) -> None:
        logger.info(f"notifying PR '{pull_request.github_pull_request_number}', current comment: {pull_request.comment_id}")
        if pull_request.comment_id:
            logger.info(f"deleting comment '{pull_request.comment_id}'")
            self._github_api_client.delete_comment(pull_request.github_pull_request_number, pull_request.comment_id)
            pull_request.comment_id = None

        logger.info(f"posting comment")
        comment = self._github_api_client.post_comment(pull_request.github_pull_request_number,
                                                       content)
        logger.info(f"comment posted, id: {comment.id}")
        pull_request.comment_id = str(comment.id)
        self._pull_request_repo.upsert(pull_request)
