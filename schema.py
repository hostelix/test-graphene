from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
import graphene
from graphene import relay

from models import *
from database import db_session, init_db


class Actor(SQLAlchemyObjectType):
    class Meta:
        model = ActorModel
        interfaces = (relay.Node,)


class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel
        interfaces = (relay.Node,)


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (relay.Node,)


class Director(SQLAlchemyObjectType):
    class Meta:
        model = DirectorModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    actors = SQLAlchemyConnectionField(Actor)
    movies = SQLAlchemyConnectionField(Movie)
    categories = SQLAlchemyConnectionField(Category)
    directors = SQLAlchemyConnectionField(Director)

    gentes = graphene.List(Actor)

    def resolve_gentes(self, args, context, info):
        query = Actor.get_query(context)  # SQLAlchemy query
        return query.all()

