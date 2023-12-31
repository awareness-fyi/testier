from typing import Any

from reporting.gateway.pytest.dtos.coverage_report import PytestCoverageReport
from reporting.models.coverage_report import CoverageReport


class PytestCoverageReportParser:

    def parse(self, raw: dict[str, Any]) -> PytestCoverageReport:
        return PytestCoverageReport.model_validate(raw)
