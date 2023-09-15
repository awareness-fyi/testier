from decimal import Decimal

from reporting.models.coverage_report import CoverageReport

COVERAGE_DECREASE = """So, the situation is not looking very good.
The code coverage in the repo just dropped {coverage_diff:.2f}% 🔻
From {main:.2f}% to {head:.2f}%."""

COVERAGE_INCREASE = """OMG! Look at you! You testing badass!
The code coverage in this repository just went up by {coverage_diff:.2f}% 💚
From {main:.2f}% to {head:.2f}%."""

COVERAGE_NO_CHANGE = """It seems that nothing has changed, which is good!
The repository keeps a decent {main:.2f}% code coverage.
All thanks to you! 🙏🏼"""

FOOTER = """_You can always add more tests before you merge your PR and I'll make sure to update you here, through this comment_ 😎
_Keep the hard work_ 💪🏼"""


class Message:
    @classmethod
    def build(cls, main: CoverageReport, head: CoverageReport) -> str:
        coverage_diff = main.compare(head)
        message = "### Code coverage change report"
        if coverage_diff.is_zero():
            message += COVERAGE_NO_CHANGE.format(main=main.percent)
        elif coverage_diff > 0:
            message += COVERAGE_DECREASE.format(main=main.percent, head=head.percent, coverage_diff=coverage_diff)
        elif coverage_diff < 0:
            message += COVERAGE_INCREASE.format(main=main.percent, head=head.percent, coverage_diff=coverage_diff)

        message += FOOTER

        return message
