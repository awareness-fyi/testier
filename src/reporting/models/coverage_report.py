from decimal import Decimal

from pydantic import BaseModel


class CoverageReport(BaseModel):
    percent: Decimal

    def compare(self, other: "CoverageReport") -> Decimal:
        return self.percent - other.percent
