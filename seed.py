from models import db, User
from app import app


db.drop_all()
db.create_all()


emily = User(first_name='Emily', last_name='Walker', image_url='')
JiHye = User(first_name='JiHye', last_name='Yoon', image_url='')


db.session.add(emily)
db.session.add(JiHye)


db.session.commit()
