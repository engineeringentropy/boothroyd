from ohms.models.database.base import db

class OhmsDatabaseProject(db.Model):
    __tablename__ = 'ohms_project'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.)