from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def connect_db():

    return sqlite3.connect("car.db")



conn=connect_db()

conn.execute("""

CREATE TABLE IF NOT EXISTS cars(

id INTEGER PRIMARY KEY,

name TEXT,

brand TEXT

)

""")

conn.close()



@app.route("/cars", methods=["GET"])

def get():

    conn=connect_db()

    data=conn.execute("SELECT * FROM cars").fetchall()

    conn.close()

    return jsonify(data)



@app.route("/cars", methods=["POST"])

def add():

    data=request.get_json()

    conn=connect_db()

    conn.execute(

    "INSERT INTO cars(name,brand) VALUES (?,?)",

    (data["name"],data["brand"])

    )

    conn.commit()

    conn.close()

    return "Added"


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)