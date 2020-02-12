from flask_wtf import FlaskForm
from wtforms.fields import TextField, StringField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = TextField('Name',
    validators=[DataRequired()])
    email = TextField('Email',validators=[DataRequired(),Email()])
    subject = StringField('Subject',validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])