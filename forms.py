from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField(label='User Name: ', validators = [DataRequired()])
    Gender = RadioField('Gender', choices = [('M', 'Male'),('F', 'Female'),('O', 'Other')])
    Address = TextAreaField('Address')
    email = StringField(label = 'email')
    Age = IntegerField('age')
    language=SelectField('Languages', choices=[('cpp', 'c++'), ('py', 'Python')])
    submit = SubmitField('Send')