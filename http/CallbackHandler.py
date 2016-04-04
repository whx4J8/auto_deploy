import os
from bottle import run,route
@route("/callback")
def callbackHandler():
    os.system('./deploy.sh')
    return "ok"

run( host='localhost',port=8082, debug=False)