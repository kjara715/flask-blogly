"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()


# Add Users
user1 = User(first_name='Marley', last_name='Fischer', image_url='https://www.stockvault.net/data/2010/09/21/114948/preview16.jpg')
user2 = User(first_name='Alyssa', last_name='Keratin', image_url='https://www.stockvault.net/data/2011/04/12/121747/preview16.jpg')
user3 = User(first_name='Johnny', last_name='Harrington')
user4 = User(first_name='Mark', last_name='Twain')

# users
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)

# Commit
db.session.commit()

#Add Posts
post1=Post(title='My First Post!!!', content="Some random content", user_id=1)
post2=Post(title='My Second Post', content="Some test content part 2", user_id=1)
post3=Post(title='Hi World', content="What brings you to this neck of the woods?", user_id=2)
post4=Post(title='You Little Rats', content="There were a bunch of little rats at yoga today.", user_id=3)

#posts
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)

# Commit
db.session.commit()

#Tags
tag1=Tag(name="newbie")
tag2=Tag(name="littlerats")
tag3=Tag(name="hi")

#PostTag
posttag1=PostTag(post_id="1",tag_id="1") 
posttag2=PostTag(post_id="3",tag_id="1")
posttag3=PostTag(post_id="4",tag_id="2")


#tags
db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)

# Commit
db.session.commit()

#PostTags

db.session.add(posttag1)
db.session.add(posttag2)
db.session.add(posttag3)

# Commit
db.session.commit()

