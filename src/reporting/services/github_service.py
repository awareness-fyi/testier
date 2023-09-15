from _decimal import Decimal

from infrastructure.config import Config
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

    def get_pull_request(self, github_pull_request_number: str) -> PullRequest:
        pass

    def get_main_branch(self) -> Branch:
        return Branch(name=Config.MAIN_BRANCH,
                      coverage_report=CoverageReport(percent=Decimal("85.71")),
                      diff_from_main_branch=Decimal("0"))

    def upsert(self, github_pull_request_number: str, report: CoverageReport, diff_from_main_branch: Decimal) -> PullRequest:
        github_pull_request = self._github_api_client.get_pull_request(github_pull_request_number)
        pull_request = PullRequest(github_pull_request_number=github_pull_request_number,
                                   author=GithubUser(username=github_pull_request.user.login,
                                                     name=github_pull_request.user.name),
                                   branch=Branch(coverage_report=report, name=github_pull_request.head.ref, diff_from_main_branch=diff_from_main_branch, ),
                                   repository=Repository(id=self._repository))

        return pull_request
