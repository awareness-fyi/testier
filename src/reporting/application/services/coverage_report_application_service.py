import json
from pathlib import Path

from infrastructure.gateway.github_api_client import GithubApiClient
from infrastructure.readers.file_reader import FileReader
from notifications.interfaces.notification_service import NotificationService
from reporting.gateway.pytest.parsers.pytest_coverage_report_parser import PytestCoverageReportParser
from reporting.models.message import Message
from reporting.services.github_service import GithubService


class CoverageReportApplicationService:

    def __init__(self, repository: str):
        self._github_service = GithubService(repository)
        self._file_reader = FileReader()
        self._report_parser = PytestCoverageReportParser()
        self._notification_service = NotificationService()

    def run(self, file_path: str, pull_request_number: str):
        raw = self._file_reader.read(Path(file_path))
        report = self._report_parser.parse(json.loads(raw))
        # pull_request = self._github_service.get_pull_request(pull_request)

        main = self._github_service.get_main_branch()
        message = Message.build(main.coverage_report, report)
        # self._github_service.upsert(pull_request.id, report, coverage_diff)

        # notification = self._notification_service.get(Channel.GITHUB)
        # notification.notify(message)

        GithubApiClient("awareness-fyi/testier").post_comment(pull_request_number, message)
