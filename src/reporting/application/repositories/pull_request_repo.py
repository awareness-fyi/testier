from reporting.application.mappers.pull_request_mapper import PullRequestMapper
from reporting.db.models.pull_request_document import PullRequestDocument
from reporting.models.pull_request import PullRequest


class PullRequestRepo:
    def __init__(self, gh_repository: str) -> None:
        self._mapper = PullRequestMapper()
        self._gh_repository = gh_repository

    def upsert(self, pull_request: PullRequest) -> PullRequest:
        doc = self._mapper.map_to_document(pull_request)
        doc.branch.save()
        doc.save(cascade=True)
        return self._mapper.map_to_model(doc)

    def get(self, gh_pr_number: str) -> PullRequest:
        doc = PullRequestDocument.objects.get(gh_number=gh_pr_number, repository=self._gh_repository)
        return self._mapper.map_to_model(doc)
