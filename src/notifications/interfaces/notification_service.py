from notifications.interfaces.channel import Channel
from notifications.interfaces.notification import Notification
from notifications.models.github_comment import GithubComment


class NotificationService:
    def get(self, channel: Channel) -> Notification:
        if channel is Channel.GITHUB:
            return GithubComment()
