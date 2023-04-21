import os, psycopg
from psycopg.rows import dict_row
from flask import Flask, request, jsonify
from flask_cors import CORS 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app) # Tillåt cross-origin requests

# databas-connection:
db_url = os.environ.get('DB_URL') # ta variabeln från .env
conn = psycopg.connect(db_url, row_factory=dict_row, autocommit=True) # autocommit: commita databas-transaction automatiskt

@app.route("/")
def index():
    return "Use endpoints /rooms or /bookings"


@app.route("/guests/<int:id>")
def guest(id):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * 
                FROM hotel_guest
                WHERE id = %s""", [ id ])
            result = cur.fetchone()
        return result
    except:
        # vi kan skriva statuskoden direkt efter response bodyn
        return {"message": "ERROR: no such guest"}, 400

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


@app.route("/bookings", methods=['GET', 'POST'])
def bookings():
    if request.method == 'GET':
        with conn.cursor() as cur:
            cur.execute("""
                SELECT 
                    *
                FROM 
                    hotel_booking""")
            result = cur.fetchall()
        return { "bookings": result }

    if request.method == 'POST':
        try:
            req_body = request.get_json()
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO hotel_booking (
                        room_id,
                        guest_id,
                        startdate,
                        info
                    ) VALUES (
                        %s, %s, %s, %s
                    ) RETURNING id
                """, [
                    req_body['room_id'],
                    req_body['guest_id'],
                    req_body['startdate'],
                    req_body['info']
                ])
                new_id = cur.fetchone()['id']

            return { "new_booking": new_id }
        except Exception as e:
            # visa inte fullständig error-info i produktion!
            print("ERROR: " + repr(e)) # Skriv felmeddelandet i serverns konsol
            return { "message": "ERROR: Something went wrong."}, 400

    else:
        return { "Du använde metoden": request.method }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)

