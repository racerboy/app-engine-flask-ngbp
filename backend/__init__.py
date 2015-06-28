from flask import Flask
app = Flask(__name__, static_url_path = "")
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


import backend.controller
