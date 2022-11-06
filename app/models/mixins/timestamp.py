import datetime

from app import db

def get_current_username():
    return "SUPERUSER"

class CreateTimestampMixin(object):
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    created_by = db.Column(db.String(20), default=get_current_username)

class UpdateTimestampMixin(object):
    last_updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    last_updated_by = db.Column(db.String(20), onupdate=get_current_username)