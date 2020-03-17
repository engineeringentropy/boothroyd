from ohms.models.database.base import db

class OhmsDatabaseRequirement(db.Model):
    __tablename__ = 'ohms_requirement'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    