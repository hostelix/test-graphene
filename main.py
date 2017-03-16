import json
import graphene
from database import init_db, db_session
from schema import Query

if __name__ == '__main__':
    init_db()

    schema = graphene.Schema(query=Query)

    query1 = '''
        query {
            gentes {
                name
            }
        }
    '''

    query = '''
            query {
                persons {
                    edges{
                        node {
                            id
                            firstName

                            hobbies{
                                name
                            }
                        }
                    }
                }
            }
        '''

    query2 = '''
    query {
        allPersons{
            edges {
                node {
                    person {
                        firstName
                        age
                    }

                    hobbies {
                        name
                    }
                }
            }
        }
    }
    '''



    result = schema.execute(query1, context_value={'session': db_session})

    print json.dumps(result.data, indent=4)
