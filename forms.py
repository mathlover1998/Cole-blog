from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL,Email,Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
class CreateRegisterForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email(message='Wrong format for email!')])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(8)])
    name = StringField(label='Name',validators=[DataRequired()])
    submit = SubmitField('Register')
class CreateLoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(8)])
    submit = SubmitField('Login')
class CommentForm(FlaskForm):
    body = CKEditorField('Comment',validators=[DataRequired()])
    submit = SubmitField('Submit comment')