from reporting.models.branch import Branch

COVERAGE_DECREASE = """
Hopa hopa hopa, wait a minute 🛑
The code coverage in the repo just dropped {coverage_diff:.2f}% 🔻
From {main:.2f}% to {head:.2f}%."""



COVERAGE_INCREASE = """
OMG! Look at you! You testing badass!
The code coverage in this repository just went up by {coverage_diff:.2f}% 💚
From {main:.2f}% to {head:.2f}%."""

COVERAGE_NO_CHANGE = """
It seems that nothing has changed, which is good!
The repository keeps a decent {main:.2f}% code coverage.
All thanks to you! 🙏🏼"""



NO_MAIN = """
We are missing information about the main branch and therefore can not compare the current branch to the main branch.
This might happen due to either:
1. It is your first PR 🎉
2. There is a problem with the main branch update.

Please make sure the main branch updates after a PR is being merged."""

FOOTER = """

_You can always add more tests before you merge your PR and I'll make sure to update you here, through this comment_ 😎
_Keep the hard work_ 💪🏼"""


class Message:
    @classmethod
    def build(cls, main: Branch | None, head: Branch) -> str:
        message = "### Code coverage change report"

        if not main:
            message += NO_MAIN
            return message

        coverage_diff = head.compare(main)

        if coverage_diff.is_zero():
            message += COVERAGE_NO_CHANGE.format(main=main.coverage_report.percent)
        elif coverage_diff < 0:
            message += COVERAGE_DECREASE.format(main=main.coverage_report.percent, head=head.coverage_report.percent, coverage_diff=coverage_diff)
        elif coverage_diff > 0:
            message += COVERAGE_INCREASE.format(main=main.coverage_report.percent, head=head.coverage_report.percent, coverage_diff=coverage_diff)

        message += FOOTER

        return message
