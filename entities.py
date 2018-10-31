
from flask_sqlalchemy import SQLAlchemy

from dao import dao

db=dao.get_db()
class ConfigurationEntity(db.Model):
    """Persistent entity representing a configuration property"""
    __tablename__ = 'configuration'
    key = db.Column(db.String(25), primary_key=True)
    value = db.Column(db.String(250), nullable=False)

    def __init__(self, key, value):
        self.key = key
        self.value = value
        # Create all database tables