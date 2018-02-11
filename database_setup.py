from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

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
