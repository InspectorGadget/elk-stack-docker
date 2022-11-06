from app import db
from app.models.mixins import (
    ReprMixin,
    CreateTimestampMixin,
    UpdateTimestampMixin
)

class Student(
    db.Model,
    ReprMixin,
    CreateTimestampMixin,
    UpdateTimestampMixin
):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    is_deleted = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }