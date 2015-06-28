# Import the Flask Framework
from flask import jsonify, abort, request, make_response, url_for
from backend import app
from backend.models import * ## load all of the models
from random import randint

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

def gql_json_parser(query_obj):
    count = 0
    result = {}
    for entry in query_obj:
        result[count] = entry.to_dict()
        count = count + 1
    return result

@app.route('/todo', methods = ['GET'])
def get_tasks():
    # for i in range(10):
    #     greeting = Greeting(parent=guestbook_key('cookbook'))
    #     greeting.author = Author(
    #                 identity= str(randint(0, 100)),
    #                 email=str(i) + "@emails.com")

    #     greeting.content = str(randint(0, 100))
    #     greeting.put()
    greetings_query = Greeting.query(
            ancestor=guestbook_key('cookbook')).order(-Greeting.date)
    greetings = greetings_query.fetch(10)
    return jsonify(gql_json_parser(greetings));
