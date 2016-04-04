import os
from bottle import run,route
import Server

@route("/callback")
def callbackHandler():
    os.system('./deploy.sh')
    return "ok"

run( host=Server.gethostbyname(),port=8082, debug=False)