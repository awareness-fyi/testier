from infrastructure.gateway.github_api_client import GithubApiClient
from reporting.models.branch import Branch
from reporting.models.coverage_report import CoverageReport
from reporting.models.gituhub_user import GithubUser
from reporting.models.pull_request import PullRequest
from reporting.models.repository import Repository


class GithubService:

    def __init__(self, repository: str):
        self._github_api_client = GithubApiClient(repository)
        self._repository = repository

    def obtain_pull_request(self, github_pull_request_number: str, coverage_report: CoverageReport) -> PullRequest:
        # TODO: if exists in DB: pull from there
        # if not:
        github_pull_request = self._github_api_client.get_pull_request(github_pull_request_number)
        pull_request = PullRequest(github_pull_request_number=github_pull_request_number,
                                   branch=Branch(name=github_pull_request.head.ref,
                                                 coverage_report=coverage_report),
                                   author=GithubUser(username=github_pull_request.user.login,
                                                     name=github_pull_request.user.name),
                                   repository=Repository(id=self._repository))

        # TODO: upsert PR
        return pull_request

    def get_main_branch(self) -> Branch | None:
        # TODO: get main branch from DB
        return Branch(name=Config.MAIN_BRANCH,
                      coverage_report=CoverageReport(percent=Decimal("85.70"),
                                                     diff_from_main_branch=Decimal("0"))
                      )
        # return None

    def notify(self, pull_request: PullRequest, content: str) -> None:
        if pull_request.comment_id:
            self._github_api_client.edit_comment(pull_request.github_pull_request_number, pull_request.comment_id, content)
            return

        comment = self._github_api_client.post_comment(pull_request.github_pull_request_number,
                                                       content)
        pull_request.comment_id = comment.id
        # TODO: upsert PR
