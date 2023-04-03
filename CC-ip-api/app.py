from flask import Flask, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

@app.route("/")
def hello():
    return request.remote_addr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

