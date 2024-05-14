from flask import Flask, jsonify, render_template
from flask_mail import Mail, Message
import pymongo

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'vibudesh0407@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'vibudesh0407@gmail.com'

mail = Mail(app)

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

@app.route('/send_email')
def send_email():
    # Sending email
    msg = Message('Hello!', recipients=['vishal@gmail.com'])
    msg.body = 'This is a test email sent from Flask.'
    mail.send(msg)
    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run()
