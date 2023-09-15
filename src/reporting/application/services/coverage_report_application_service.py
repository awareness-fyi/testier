import json
from pathlib import Path

from infrastructure.readers.file_reader import FileReader
from reporting.gateway.pytest.parsers.pytest_coverage_report_parser import PytestCoverageReportParser
from reporting.models.message import Message
from reporting.services.github_service import GithubService


class CoverageReportApplicationService:

    def __init__(self, repository: str):
        self._github_service = GithubService(repository)
        self._file_reader = FileReader()
        self._report_parser = PytestCoverageReportParser()

    def run(self, file_path: str, pull_request_number: str):
        raw = self._file_reader.read(Path(file_path))
        report = self._report_parser.parse(json.loads(raw))
        pull_request = self._github_service.obtain_pull_request(pull_request_number, report)

        main = self._github_service.get_main_branch()

        message = Message.build(main, report)

        self._github_service.notify(pull_request, message)
