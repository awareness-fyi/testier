from decimal import Decimal
from typing import Annotated

from pydantic import AfterValidator

RoundDecimal = Annotated[Decimal, AfterValidator(lambda v: round(v, 2))]
