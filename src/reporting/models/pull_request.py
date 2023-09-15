from pydantic import BaseModel

from reporting.models.branch import Branch
from reporting.models.gituhub_user import GithubUser
from reporting.models.repository import Repository


class PullRequest(BaseModel):
    github_pull_request_number: str
    branch: Branch
    author: GithubUser
    repository: Repository


    def __eq__(self, other: "PullRequest") -> bool:
        return other.id == self.id
