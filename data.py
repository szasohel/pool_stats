from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Stats, Base

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


player1 = Stats(player="Sayed", game=0, win=0, lose=0)
session.add(player1)
session.commit()

player2 = Stats(player="Sohel", game=0, win=0, lose=0)
session.add(player2)
session.commit()

player3 = Stats(player="Jay", game=0, win=0, lose=0)
session.add(player3)
session.commit()

player4 = Stats(player="Tim", game=0, win=0, lose=0)
session.add(player4)
session.commit()

print ("stats populated!")
