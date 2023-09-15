from decimal import Decimal

from pydantic import BaseModel, Field

from reporting.models.coverage_report import CoverageReport


class PytestCoverageReport(BaseModel):
    class Totals(BaseModel):
        percent_covered: Decimal = Field(..., decimal_places=2)
        percent_covered_display: str

    totals: Totals

    def map(self) -> CoverageReport:
        return CoverageReport(percent=self.totals.percent_covered)
