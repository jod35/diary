from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class DayForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired])
    day=TextAreaField("Your day",validators=[DataRequired])
    submit=SubmitField("submit")
