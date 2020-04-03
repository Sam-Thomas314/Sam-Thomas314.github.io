from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class TimeSheetForm(FlaskForm):
    #Customer_id
    Customer_name = StringField('Customer Name:', validators=[DataRequired()])
    Customer_Total = IntegerField('Total', validators=[DataRequired()])
