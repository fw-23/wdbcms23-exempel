import os, psycopg
from psycopg.rows import dict_row
from flask import Flask, request, jsonify
from flask_cors import CORS 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

# databas-connection:
db_url = os.environ.get('DB_URL') # ta variabeln från .env
conn = psycopg.connect(db_url, row_factory=dict_row) # dict_row: få query-resultat som list of dicts

@app.route("/")
def index():
    return "Use endpoints /rooms or /bookings"

@app.route("/guests")
def guests():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM hotel_guest")
        result = cur.fetchall()
    return { "guests": result }

@app.route("/rooms")
def rooms():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM hotel_room ORDER BY room_number")
        rooms_list = cur.fetchall()
    return { 
        "rooms": rooms_list, 
        "room_count": len(rooms_list) 
    }
    #return jsonify(rooms_list)

@app.route("/rooms/<int:id>")
def room(id):
    try:
        return rooms_list[id]
    except:
        # vi kan skriva statuskoden direkt efter response bodyn
        return {"message": "ERROR: no such room"}, 400



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)

