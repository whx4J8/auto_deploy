import os
from bottle import run, route

@route("/callback")
def callbackHandler():
    os.system('./deploy.sh')
    return "ok"


run(host='0.0.0.0', port=8081, debug=False)  # use 0.0.0.0 inner or outer net ip is all ok
