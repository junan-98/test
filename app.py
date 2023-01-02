#!/usr/bin/python3
from flask import Flask, Response, request, json, redirect, url_for

app = Flask(__name__)

#!/usr/bin/python3
from flask import Flask, Response, request, json

app = Flask(__name__)


@app.route('/', methods=['GET','POST','OPTIONS'])
def index():
    resp = Response('redirect', 308)
    resp.headers['Location'] = 'http://13.209.4.194:8000/login'
    print(dir(request))
    #resp.headers['X-Powered-By'] = 'Express'
    return resp

@app.route('/login')
def login():
    print(request.data)
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)