from reporting.db.models.branch_document import BranchDocument
from reporting.models.branch import Branch
from reporting.models.coverage_report import CoverageReport


class BranchMapper:
    def map_to_document(self, branch: Branch) -> BranchDocument:
        return BranchDocument(repository=branch.repository,
                              name=branch.name,
                              coverage_rate=branch.coverage_report.percent,
                              id=f"{branch.repository}_{branch.name}")

    def map_to_model(self, document: BranchDocument) -> Branch:
        coverage_report = CoverageReport(percent=document.coverage_rate)
        return Branch(name=document.name,
                      coverage_report=coverage_report,
                      repository=document.repository)
