from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.core import SelectField, StringField
from wtforms.validators import DataRequired
# from flask_wtf.file import FileField, FileAllowed_


LANGUAGE = [ 'en', 'es', 'fr']
SORT_BY = [ 'relevancy', 'popularity', 'publishedAt']
CATEGORY = ['business','entertainment', 'general', 'health', 'science', 'sports', 'technology']
COUNTRY = [ 'us', 'au', 'ca', 'ch', 'fr' ]

class SelectForm(FlaskForm):
    language = SelectField("Language", choices=LANGUAGE, validators=[DataRequired()])
    query = StringField("Topic", validators=[DataRequired()])
    category = SelectField("Category", choices=CATEGORY, validators=[DataRequired()])
    country = SelectField("Country", choices=COUNTRY, validators=[DataRequired()])
    sort_by = SelectField("Sort By", choices=SORT_BY, validators=[DataRequired()])
    submit = SubmitField('Select')



