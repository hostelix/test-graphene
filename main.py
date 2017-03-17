import json
import graphene
from database import init_db, db_session
from schema import Query, Movie

if __name__ == '__main__':
    init_db()

    schema = graphene.Schema(query=Query)

    query1 = '''
        query {
            movies {

                        id
                        name
                        duration
                        gender {
                            name
                        }
                        director {
                            firstName
                            lastName
                        }
                        actors {
                            id
                            firstName
                            lastName
                        }

            }
        }
    '''



    result = schema.execute(query1, context_value={'session': db_session})

    print json.dumps(result.data, indent=4)
