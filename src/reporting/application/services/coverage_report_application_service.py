import json
from pathlib import Path

from infrastructure.gateway.github_api_client import GithubApiClient
from infrastructure.readers.file_reader import FileReader
from notifications.interfaces.notification_service import NotificationService
from reporting.gateway.pytest.parsers.pytest_coverage_report_parser import PytestCoverageReportParser
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
        coverage_diff = main.coverage_report.compare(report)
        # self._github_service.upsert(pull_request.id, report, coverage_diff)
        message = f"""
### Code coverage change report
Hola! 👋🏼
I'm here to report about the code coverage change of your PR 🤩
        """
        if coverage_diff.is_zero():
            message += f"""
It seems that nothing has changed, which is good!
The repository keeps a decent {coverage_diff}% code coverage.
All thanks to you! 🙏🏼
            """
        elif coverage_diff < 0:
            message += f"""
So, the situation is not looking very good.
The code coverage in the repo just dropped {coverage_diff}% 🔻
            """
        elif coverage_diff > 0:
            message += f"""
OMG! Look at you! You testing badass!
The code coverage in this repository just went up by {coverage_diff}% 💚
            """

        message += """
_You can always add more tests before you merge your PR and I'll make sure to update you here, through this comment_ 😎
_Keep the hard work_ 💪🏼

At your service 🫡
            """

        # notification = self._notification_service.get(Channel.GITHUB)
        # notification.notify(message)

        GithubApiClient("awareness-fyi/testier").post_comment(pull_request_number, message)
