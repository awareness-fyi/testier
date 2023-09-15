from pydantic import BaseModel

from infrastructure.types import RoundDecimal


class PytestCoverageReport(BaseModel):
    class Totals(BaseModel):
        percent_covered: RoundDecimal

    totals: Totals
