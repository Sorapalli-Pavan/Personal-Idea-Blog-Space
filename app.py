from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client["admin"]  # Replace with your database name
collection = db["Pavan"]  # Replace with your collection name
@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Data inserted successfully"})

@app.route('/get/<string:key>', methods=['GET'])
def get_data(key):
    data = collection.find_one({"key": key})
    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "Data not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Your users (for demonstration purposes, replace this with a real user database)
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the provided credentials are valid
    for user in users:
        if user['username'] == username and user['password'] == password:
            return "Login successful!"  # You can customize this response
    return "Login failed. Please check your credentials."  # You can customize this response

if __name__ == '__main__':
    app.run(debug=True)

