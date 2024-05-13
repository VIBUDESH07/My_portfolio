from flask import Flask, jsonify, render_template
import pymongo

app = Flask(__name__)


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["Order"]

# Route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
   
    data = {"_id": 1, "name": "Alice", "age": 25}
    collection.insert_one(data)

    # Query data from MongoDB
    result = collection.find_one({"_id": 1})
    return jsonify(result)
@app.route('/Email')
def contact():
    

if __name__ == '__main__':
    app.run()
