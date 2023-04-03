from flask import Flask, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

@app.route("/")
def hello():
    return "<h1>Hello, Flask!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)



# Instruktioner
#
# FÖRSTA GÅNGEN:
# - I denna katalog, kör: pip install -r requirements.txt
# - Kopiera/byt namn på .env-example ==> .env
# - I .env, byt FLASK_RUN_PORT=8000 till din egen portnummer (se itslearning!)
# 
# STARTA APPEN:
# flask run