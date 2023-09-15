from pydantic import BaseModel

from infrastructure.types import RoundDecimal
from reporting.models.coverage_report import CoverageReport


class PytestCoverageReport(BaseModel):
    class Totals(BaseModel):
        percent_covered: RoundDecimal
        percent_covered_display: str

    totals: Totals

    def map(self) -> CoverageReport:
        return CoverageReport(percent=self.totals.percent_covered)
