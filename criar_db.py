from fakeinterest import database, app
from fakeinterest.models import Usuario, Posts

with app.app_context():
    database.create_all()