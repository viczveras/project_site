from fakeinterest import database, app
from fakeinterest.models import Usuarios, Posts


with app.app_context():
    database.create_all()