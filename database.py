from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import json


def get_vars():
    env_vars_file = open("env_vars.json", "r")
    data_json = env_vars_file.read()

    return json.loads(data_json)

vars_env = get_vars()

engine = create_engine(vars_env.get('postgres_uri'), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)