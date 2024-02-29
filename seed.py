from models import db, User, Post
from app import app


db.drop_all()
db.create_all()


emily = User(first_name='Emily', last_name='Walker', image_url='')
JiHye = User(first_name='JiHye', last_name='Yoon', image_url='')


db.session.add(emily)
db.session.add(JiHye)

post1 = Post(title='Hello World', content='hello from world', user_id=1)
post2 = Post(title='Goodbye World', content='goodbye to world', user_id=1)

db.session.add(post1)
db.session.add(post2)

db.session.commit()
