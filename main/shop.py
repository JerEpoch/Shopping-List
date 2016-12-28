import wtforms
import flask
import auth
import model


from flask_wtf import FlaskForm
from flask.ext import wtf
from wtforms import Form, validators, StringField,TextAreaField
from wtforms.validators import DataRequired
from main import app

class ShoplistUpdateForm(FlaskForm):
	item = wtforms.StringField('item', validators=[DataRequired()])


@app.route('/shop/create/', methods=['GET', 'POST'])
#@auth.login_required
def shoplist_create():
	form = ShoplistUpdateForm()

	if form.validate_on_submit():
		list_db = model.Shoplist(
			user_key = auth.current_user_key(),
			item = form.item.data,)
		list_db.put()
		return flask.redirect(flask.url_for('welcome'))

	return flask.render_template(
		'list_new.html',
		html_class='list-new',
		title='Shopping List',
		form=form,
		)