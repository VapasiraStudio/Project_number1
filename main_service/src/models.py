from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class List(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    url = Column(String, index=True)
    title = Column(String, index=True)
    description = Column(String)
    list_id = Column(Integer, ForeignKey('lists.id'))
