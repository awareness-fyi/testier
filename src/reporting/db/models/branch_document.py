from mongoengine import Document, StringField, DecimalField


class BranchDocument(Document):
    id = StringField(required=True, primary_key=True)
    repository = StringField(required=True)
    name = StringField(required=True)
    coverage_rate = DecimalField(required=True)
