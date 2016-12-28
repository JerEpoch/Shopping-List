from google.appengine.ext import ndb
import model

class Shoplist(model.Base):
	user_key = ndb.KeyProperty(kind=model.User, required=True)
	item = ndb.StringProperty(required=True)
	favorite = ndb.BooleanProperty(default=False)