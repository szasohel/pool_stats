from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base is the instance of declarative_base class
Base = declarative_base()

class Stats(Base):
    """Stats is inherited from Base class, which is the instance
    of declarative_base. it is used to create user table
    and map the table acording to given atributes"""

    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True, nullable=False)
    player = Column(String(250), nullable=False)
    game = Column(Integer)
    win = Column(Integer)
    lose = Column(Integer)


engine = create_engine('sqlite:///stats.db')

Base.metadata.create_all(engine)