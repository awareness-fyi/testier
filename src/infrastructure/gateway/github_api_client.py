from github import Auth, GithubIntegration
from github.Installation import Installation
from github.IssueComment import IssueComment
from github.PullRequest import PullRequest

from infrastructure.config import Config


KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAwfJmP1luNx4Bx4+IP7XZldkhLCOv8tZ23GFlFFA9M519ApFe\ngBY2mxvzOlZ7I1uknBHhF6eZyS48WGxkEBfPpTS405dEy2+VA+uc0HZxLuOUkOJw\nRoWrHLOn81t884vn0CTmhHBjOD8S0m4qnoJ+epmkFf355YV1rudCGe1WTx/SoN7+\n/Trok2c+K5hQWUKlwgZsz+1+7WILdZIAlu2/TJdEfloH0TM9a+XUsLUjLozZKrtd\nRGFszAkz52nG4I9bLVD2VgVRPmiwmXID8hlECBOm1nMVhcPritbOVNJ8edjdWZph\nZ0u/jhTMF68iqHrjJCwHZFZSIDtQNipqrtfcxQIDAQABAoIBAHPCBh0Rd6MWGeHO\nXXgJRhEWQ6JguoeqUc8/omD5c033VcHOmiTBHV5+1DGhpGV6MUmlsj+4HSXinsn4\nB9FDJQBp81b3FmyF8N8iJbqWtv9Rfj7rqC+vYG4FHN03YeDLRFULcTrjCZVssANB\nFdb99Beg1Dr8F8dSXOdDyERJUBZw0KQGvdVWIEppZQhXNkdwWmvKZm1zpiPo1U2x\nV1Au3b0ttM66fgd1R1ISMWi+KkCX5/ZjdJfced8fiTE1QTIPZH87Te9ew+9l5Mtk\n66QPJzlKZaKl89YRt253tqrx7BE3OvG6Gu9sImXlWqj2PoYOL65nHScw2dT0RsWS\nd326qpECgYEA9mkypHthQAgyJopTihpn75fbTm4WYzzQazYHqx01YS87SpXg5rAr\nwQ8g9XJxLAjD7eoiOucnMyZYAhxGvtDtcHlW9d7XALRuioKivs31F5tcY58tyDP/\nxcKyBMOBiA59jbaTd3VOMx0w4jtDe/i9Y0M792v6yYa2JL/r8ITD6Q8CgYEAyX6K\n6U+JC0JyOQxxJ/PjT+kOmIGOGU90ApWf0eRiLN9fQv7pqoBS3KAJuZr+IKzGAm53\ngGA0baqoKS0HUaCUSYfd9PtaEEGo98VUrqkVd0QnmgsVgopNPBxkULXHcgDkpIcP\nu0+whPeAgouZ9t6Rqk9rSacPX55SwG6QzUD4VOsCgYEA5Cv5dxHAtdhhCAsi3Ekj\nYVtO+ks6c95GaGB5rVu4qCtiTeiHf1Y2zejCbkXwwgPD2jTqSXzucZDaAepJIDy7\nAWF6wuX8VWy+x4e8R87TW27DmIQ3kqGEAI4O5hZbha9VV7puxzlalj47m+Gg1dU5\nGgeSKcRVT/NsCo+lXOyztMUCgYBGY0xHgJ9RLZ8VSsFkwZAQ5EtS/z8SnGzcUkSI\nYA3juwxeLQqXo0hPBiEfk4NfCrwJMWnRkMn/3XPtHmvGGiBzJ2FkKUInF6jdFTQl\n5682ALsM1v5mocWlUA3DHB1WN/Wne/8E4iu553QfJoFcehfMtP23twJp1rb1viob\naazWjQKBgQDvwPdcf6I+cmiqpdm7B7V/gLl4EflPKrklK4YWC7tVvJBTedrQ/1dl\nfDDu7mgbj/4YTv+fCohGVLKYcHIgy2B6x+YsHgRNx/SSOOg+zuZK9OC+KHLpY9CI\n2qrXV5OSZhwk8mFS3cyoksuDpVdGGaCv8/64bfevC00YOw7S8TsZGA==\n-----END RSA PRIVATE KEY-----\n"


class GithubApiClient:
    def __init__(self, repository: str) -> None:
        auth = Auth.AppAuth(Config.TESTIER_GITHUB_APP_ID, KEY)
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


if __name__ == '__main__':
    GithubApiClient("awareness-fyi/testier").delete_comment("6", "1722068146")
