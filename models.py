from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

actors_movies = Table(
    'actors_movies', Base.metadata,
    Column('actor_id', Integer, ForeignKey('actors.id')),
    Column('movie_id', Integer, ForeignKey('movies.id'))
)


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


class GenderModel(Base):
    __tablename__ = 'genders'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class MovieModel(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(Float)
    gender_id = Column(Integer, ForeignKey('genders.id'))
    director_id = Column(Integer, ForeignKey('directors.id'))

    gender = relationship(GenderModel)
    director = relationship(DirectorModel)

    actors = relationship(ActorModel, backref="movies", secondary='actors_movies')
