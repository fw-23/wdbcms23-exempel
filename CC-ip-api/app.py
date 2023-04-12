from flask import Flask, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

@app.route("/")
def hello():
    # i Flask kan vi skicka dict direkt, blir JSON automatiskt
    return { 
        "ip": request.remote_addr,
        "msg": "hello!",
        "lista": [1, 2, 3, "hej"], # list
        "octets": request.remote_addr.split(".") #list
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

