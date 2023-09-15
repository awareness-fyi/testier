from decimal import Decimal

from pydantic import BaseModel

from infrastructure.types import RoundDecimal


class CoverageReport(BaseModel):
    percent: RoundDecimal

    def compare(self, other: "CoverageReport") -> Decimal:
        return self.percent - other.percent
