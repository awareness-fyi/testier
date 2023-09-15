from mongoengine import Document, StringField, ReferenceField, DecimalField

from reporting.db.models.branch_document import BranchDocument


class PullRequestDocument(Document):
    gh_number = StringField(required=True, primary_key=True)
    repository = StringField(required=True, primary_key=True)
    branch = ReferenceField(BranchDocument, required=True)
    author_username = StringField(required=True)
    author_name = StringField(required=True)
    comment_id = StringField(required=False)
    coverage_change = DecimalField(required=True)
