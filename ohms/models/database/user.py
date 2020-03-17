from ohms.models.database.base import db

class OhmsDatabaseUser(db.Model):
    __tablename__ = 'ohms_user'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    