from decimal import Decimal

from pydantic import BaseModel

from reporting.models.coverage_report import CoverageReport


class Branch(BaseModel):
    name: str
    coverage_report: CoverageReport
    diff_from_main_branch: Decimal
