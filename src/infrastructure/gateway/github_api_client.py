from github import Auth, GithubIntegration
from github.Installation import Installation
from github.IssueComment import IssueComment
from github.PullRequest import PullRequest

from infrastructure.config import Config


class GithubApiClient:
    def __init__(self, repository: str) -> None:
        auth = Auth.AppAuth(Config.TESTIER_GITHUB_APP_ID, Config.TESTIER_GITHUB_APP_PRIVATE_KEY)
        integration = GithubIntegration(auth=auth)
        installation: Installation = integration.get_installations()[0]
        self._gh = installation.get_github_for_installation().get_repo(repository)

    def get_pull_request(self, github_pull_request_number: str) -> PullRequest:
        pr = self._gh.get_pull(int(github_pull_request_number))
        return pr

    def post_comment(self, github_pull_request_number: str, content: str) -> IssueComment:
        pr = self.get_pull_request(github_pull_request_number)
        return pr.create_issue_comment(content)

    def delete_comment(self, github_pull_request_number: str, comment_id: str) -> None:
        self.get_pull_request(github_pull_request_number).get_issue_comment(int(comment_id)).delete()

    def edit_comment(self, github_pull_request_number: str, comment_id: str, content: str) -> IssueComment:
        pr = self.get_pull_request(github_pull_request_number)
        comment = pr.get_issue_comment(int(comment_id))
        comment.edit(content)
        return comment
