from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired
from wtforms import StringField

class ContactForm(Form):
    #name = TextField("Name of Student", [validators.Required("Please enter name ")])
    #name = StringField(label='User Name: ', validators=[Length(min=2, max=30), DataRequired()])
    name = StringField(u'Name of student :', [validators.Required("Please enter name ")])
    Gender = RadioField('Gender', choices = [('M', 'Male'),('F', 'Female')])
    Address = TextAreaField('Address')
    email = TextField('Email',[validators.Required('Please enter email address'), validators.Email('Please enter email again')])
    Age=IntegerField('age')
    language=SelectField('Languages', choices=[('cpp', 'c++'), ('py', 'Python')])
    submit = SubmitField('Send')