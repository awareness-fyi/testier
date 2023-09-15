from notifications.interfaces.notification import Notification


class GithubComment(Notification):
    def notify(self, content: str) -> None:
        pass
