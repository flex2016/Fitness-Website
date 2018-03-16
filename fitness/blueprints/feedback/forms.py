from flask_wtf import Form
from wtforms import TextAreaField, TextField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class FeedbackForm(Form):
    name = TextField("What's your Name?",
                     [DataRequired(), Length(1, 15)])

    email = EmailField("What's your e-mail address?",
                       [DataRequired(), Length(3, 254)])

    feedback = TextAreaField("Please Leave your feedback!!!",
                             [DataRequired(), Length(1, 8192)])
