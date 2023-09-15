from decimal import Decimal

from pydantic import BaseModel

from reporting.models.coverage_report import CoverageReport


class Branch(BaseModel):
    name: str
    coverage_report: CoverageReport
    repository: str

    def compare(self, other: "Branch") -> Decimal:
        return self.coverage_report.compare(other.coverage_report)
