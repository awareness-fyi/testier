from reporting.application.mappers.branch_mapper import BranchMapper
from reporting.db.models.pull_request_document import PullRequestDocument
from reporting.models.gituhub_user import GithubUser
from reporting.models.pull_request import PullRequest
from reporting.models.repository import Repository


class PullRequestMapper:

    def __init__(self):
        self._branch_mapper = BranchMapper()

    def map_to_document(self, pr: PullRequest) -> PullRequestDocument:
        return PullRequestDocument(gh_number=pr.github_pull_request_number,
                                   repository=pr.repository.id,
                                   branch=self._branch_mapper.map_to_document(pr.branch),
                                   author_username=pr.author.username,
                                   author_name=pr.author.name,
                                   comment_id=pr.comment_id,
                                   coverage_change=pr.coverage_change,
                                   id=f"{pr.repository.id}_{pr.github_pull_request_number}")

    def map_to_model(self, document: PullRequestDocument) -> PullRequest:
        return PullRequest(github_pull_request_number=document.gh_number,
                           branch=self._branch_mapper.map_to_model(document.branch),
                           author=GithubUser(username=document.author_username,
                                             name=document.author_name),
                           repository=Repository(id=document.repository),
                           comment_id=document.comment_id,
                           coverage_change=document.coverage_change)
