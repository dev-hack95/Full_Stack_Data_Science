from flask import Flask
import psycopg2
from psycopg2.extras import RealDictCursor


app = Flask(__name__)

while True:
    try:
        conn = psycopg2.connect(host='192.168.43.180',
                                user='postgres',
                                password='postgres',
                                database='api_learn_db',
                                cursor_factory=RealDictCursor)
        
        cursor = conn.cursor()
        print("Database connected successfully")
        break
    except Exception as error:
        print("Error: ", error)

@app.route("/", methods=['GET'])
def root():
    return {"message": "Hello World"}

@app.route("/posts", methods=['GET'])
def get_posts()