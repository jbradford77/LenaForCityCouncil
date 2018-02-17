from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Blogpost(Base):
    __tablename__ = 'blogpost'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    subtitle = Column(String(100))
    author = Column(String(20))
    date_posted = Column(String(20))
    content = Column(String)



engine = create_engine('sqlite:///blog.db')
 

Base.metadata.create_all(engine)
