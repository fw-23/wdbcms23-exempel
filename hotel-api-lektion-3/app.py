from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

# Ersätts senare med databas
rooms_list = [
    { "number": 101, "type": "single", "price": 80},
    { "number": 202, "type": "double", "price": 150},
    { "number": 303, "type": "single", "price": 80},
    { "number": 404, "type": "suite", "price": 500}
]

@app.route("/")
def index():
    return "Use endpoints /rooms or /bookings"

@app.route("/rooms")
def rooms():
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