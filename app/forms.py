from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email


class WorkerForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    address1= StringField('Address', validators=[DataRequired()])
    city= StringField('City', validators=[DataRequired()])
    country= StringField('Country', validators=[DataRequired()])
    telephone_no = StringField('Telephone Number', validators=[DataRequired()])
    role= StringField('Role', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    addresslocation= StringField('Location (Kingston or Montego Bay)', validators=[DataRequired()])

class HomeForm(FlaskForm):
    city = StringField('City (Kingston or Montego Bay)', validators=[DataRequired()])
    
   
   
