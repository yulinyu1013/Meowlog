from flask_wtf import FlaskForm
# from flask.ext.uploads import UploadSet, IMAGES
import wtforms
from wtforms import SubmitField,StringField,TextAreaField, FileField
from flask_wtf.file import FileAllowed, FileField
from wtforms.validators import DataRequired
# images = UploadSet('images', IMAGES);

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    pic = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')