import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Create an instance of a Flask app
app = Flask(__name__)

# Mongo DB Setup
app.config['MONGO_DBNAME'] = 'book_reviewer'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/books')
def get_books():
    return render_template('books.html', books=mongo.db.books.find())


# Set up IP address and Port number
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )