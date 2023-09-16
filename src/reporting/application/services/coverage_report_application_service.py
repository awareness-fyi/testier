import json
from pathlib import Path

from infrastructure.logger import logger
from infrastructure.readers.file_reader import FileReader
from reporting.gateway.pytest.parsers.pytest_coverage_report_parser import PytestCoverageReportParser
from reporting.models.coverage_report import CoverageReport
from reporting.models.message import Message
from reporting.services.github_service import GithubService


class CoverageReportApplicationService:

    def __init__(self, repository: str):
        self._github_service = GithubService(repository)
        self._file_reader = FileReader()
        self._report_parser = PytestCoverageReportParser()

    def update_pull_request(self, file_path: str, pull_request_number: str) -> None:
        logger.info(f"updating PR '{pull_request_number}' from file '{file_path}'")
        raw = self._file_reader.read(Path(file_path))
        report = self._report_parser.parse(json.loads(raw))
        coverage_report = CoverageReport(percent=report.totals.percent_covered)
        logger.info(f"got coverage of {coverage_report.percent:.2f}")
        main = self._github_service.get_main_branch()
        pull_request = self._github_service.upsert_pull_request(pull_request_number, coverage_report)
        message = Message.build(main, pull_request.branch)

        self._github_service.notify(pull_request, message)

    def pull_request_merged(self, pull_request_number: str) -> None:
        self._github_service.update_main(pull_request_number)
