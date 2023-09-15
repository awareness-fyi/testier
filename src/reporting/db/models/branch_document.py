from mongoengine import Document, StringField, DecimalField


class BranchDocument(Document):
    repository = StringField(required=True, primary_key=True)
    name = StringField(required=True, primary_key=True)
    coverage_rate = DecimalField(required=True)
