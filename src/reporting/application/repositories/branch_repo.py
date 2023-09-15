from decimal import Decimal

from reporting.application.mappers.branch_mapper import BranchMapper
from reporting.db.models.branch_document import BranchDocument
from reporting.models.branch import Branch


class BranchRepo:

    def __init__(self, repository: str):
        self._mapper = BranchMapper()
        self._repository = repository

    def upsert(self, branch: Branch) -> Branch:
        doc = self._mapper.map_to_document(branch)
        doc.save()
        return self._mapper.map_to_model(doc)

    def get(self, name: str) -> Branch:
        doc = BranchDocument.objects.get({"name": name})
        return self._mapper.map_to_model(doc)

    def update_coverage(self, name: str, coverage_diff: Decimal) -> None:
        BranchDocument.objects(name=name, repository=self._repository).update_one(
            upsert=True,
            inc__coverage_rate=coverage_diff)
