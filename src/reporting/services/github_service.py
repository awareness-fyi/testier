from _decimal import Decimal

from reporting.models.branch import Branch
from reporting.models.coverage_report import CoverageReport
from reporting.models.gituhub_user import GithubUser
from reporting.models.pull_request import PullRequest
from reporting.models.repository import Repository


class GithubService:
    def get_pull_request(self, github_id: str) -> PullRequest:
        pass

    def get_main_branch(self) -> Branch:
        pass

    def upsert(self, github_pr_id: str, report: CoverageReport, repository: str, diff_from_main_branch: Decimal) -> PullRequest:
        pull_request = PullRequest(id=github_pr_id,
                                   author=GithubUser(username=...),
                                   branch=Branch(coverage_report=report, id=..., diff_from_main_branch=diff_from_main_branch, ),
                                   repository=Repository(id=repository))

        return pull_request
