from pydantic import BaseModel

from reporting.models.branch import Branch
from reporting.models.gituhub_user import GithubUser
from reporting.models.repository import Repository


class PullRequest(BaseModel):
    id: str
    branch: Branch
    author: GithubUser
    repository: Repository


    def __eq__(self, other: "PullRequest") -> bool:
        return other.id == self.id
