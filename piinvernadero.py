from piinvernadero import create_app, db
from piinvernadero.models import User, Post

piinvernadero = create_app()
#cli.register(piinvernadero)

#@app.shell_context_processor
#def make_shell_context():
#return {'db': db, 'User': User, 'Post': Post}