from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class Workers(db.Model):
    __tablename__ = 'workers'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address1= db.Column(db.String(80))
    city=db.Column(db.String(50))
    country=db.Column(db.String(50))
    telephone_no=db.Column(db.String(20))
    role= db.Column(db.String(80))
    email=db.Column(db.String(60))
    addresslocation=db.Column(db.String(80))
    

    def __init__(self, first_name, last_name,address1,city,country,telephone_no,role, email, addresslocation):
        self.first_name = first_name
        self.last_name = last_name
        self.address1=address1
        self.city = city
        self.country = country 
        self.telephone_no= telephone_no
        self.role=role
        self.email=email
        self.addresslocation=addresslocation

        
       



    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
    
