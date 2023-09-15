from pydantic import BaseModel


class GithubUser(BaseModel):
    username: str

    def __eq__(self, other: "GithubUser"):
        return other.username == self.username
