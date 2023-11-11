from pydantic import BaseModel

from infrastructure.types import RoundDecimal




from reporting.models.branch import Branch

from reporting.models.gituhub_user import GithubUser


from reporting.models.repository import Repository






class PullRequest(BaseModel):
    github_pull_request_number: str
    branch: Branch
    author: GithubUser
    repository: Repository
    comment_id: str | None = None
    coverage_change: RoundDecimal

    def __eq__(self, other: "PullRequest") -> bool:
        return other.id == self.id
