from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__= "earthquakes"#define table name

    id= db.Column(db.Integer, primary_key=True)
    magnitude= db.Column(db.Float)#magnitude column
    location = db.Column(db.String)#location column
    year = db.Column(db.Integer)#year column

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>" #return a formatted strin