from flaskwebgui import FlaskUI
from nto.wsgi import application as app
from django.conf import settings


# settings.configure()
settings.DEBUG = False

FlaskUI(
	app=app, 
	server="django", 
).run()
