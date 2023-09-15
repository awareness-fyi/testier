import json
from pathlib import Path

from infrastructure.readers.file_reader import FileReader
from notifications.interfaces.channel import Channel
from notifications.interfaces.notification_service import NotificationService
from reporting.gateway.pytest.parsers.pytest_coverage_report_parser import PytestCoverageReportParser
from reporting.services.github_service import GithubService


class CoverageReportApplicationService:

    def __init__(self, repository: str):
        self._github_service = GithubService(repository)
        self._file_reader = FileReader()
        self._report_parser = PytestCoverageReportParser()
        self._notification_service = NotificationService()

    def run(self, file_path: str, pull_request: str):
        raw = self._file_reader.read(Path(file_path))
        report = self._report_parser.parse(json.loads(raw))
        pull_request = self._github_service.get_pull_request(pull_request)

        main = self._github_service.get_main_branch()
        coverage_diff = main.coverage_report.compare(report)
        self._github_service.upsert(pull_request.id, report, coverage_diff)

        message = f"Coverage change is {coverage_diff:.2f}%.\nFrom {main.coverage_report.percent:.2f}% to {report.percent:.2f}%"
        notification = self._notification_service.get(Channel.GITHUB)
        notification.notify(message)
