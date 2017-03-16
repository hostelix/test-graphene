from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Models
class ActorModel(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


class DirectorModel(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


class CategoryModel(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class MovieModel(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    director_id = Column(Integer, ForeignKey('directors.id'))

    category = relationship(CategoryModel)
    director = relationship(DirectorModel)
