import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Create an instance of a Flask app
app = Flask(__name__)

# Mongo DB Setup
app.config['MONGO_DBNAME'] = 'book_reviewer'
app.config['MONGO_URI'] = 'mongodb+srv://root:48Kcr5un1Mmlwpw5@datacentricdevelopment-hxsk1.mongodb.net/book_reviewer?retryWrites=true&w=majority'

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