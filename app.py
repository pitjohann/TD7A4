# app.py

# Import the Flask module
from flask import Flask, jsonify

# Import the PyMongo module to interact with MongoDB
from pymongo import MongoClient

# Create a Flask application instance
app = Flask(__name__)

# Connect to the MongoDB container
# We use the hostname "mongodb" to connect to the MongoDB container
# as it will be automatically resolved to the IP address of the container
# within the Docker network
client = MongoClient("mymongo",27017)

# Get a reference to the test_database
db = client["test_database"]

# Get a reference to the test_collection
collection = db["test_collection"]

colors = [ {"red":"true","blue":"false"},
           {"red":"false","blue":"true"}]
collection.insert_many(colors)

# Define a function to read the contents of the "test.txt" file
def get_data():
    with open("test.txt", "r") as f:
        data = f.read()
    return data
    
    
# Define the route for the index page
@app.route("/")
def index():
    # Fetch a single document from the test_collection
    data = collection.find_one()
    data["_id"] = str(data["_id"])

    
    # Return the fetched data as a string
    return jsonify(data)
@app.route("/text")
def display_text():
    # Call the get_data function to read the contents of the "test.txt" file
    data = get_data()

    # Return the contents of the "test.txt" file as plain text
    return data
# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")