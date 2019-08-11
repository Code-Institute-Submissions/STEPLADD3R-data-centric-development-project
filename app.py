import os
from flask import Flask, render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
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


@app.route('/book/add')
def create_book():
    return render_template('create-book.html', genres=mongo.db.genres.find())


@app.route('/book/insert', methods=['POST'])
def insert_book():
    if 'book_cover_photo' not in request.files:
        return redirect(url_for('create_book'))
        
    book_cover_photo = request.files['book_cover_photo']
    mongo.save_file(secure_filename(book_cover_photo.filename), book_cover_photo)
            
    books = mongo.db.books
    books.insert({
        'book_name' : request.form.get('book_name'),
        'book_cover_photo' : book_cover_photo.filename,
        'book_description' : request.form.get('book_description'),
        'book_press_reviews' : request.form.get('book_press_reviews'),
        'isbn' : request.form.get('isbn'),
        'publication_date' : request.form.get('publication_date'),
        'author' : request.form.get('author'),
        'publisher' : request.form.get('publisher'),
        'genres' : request.form.get('genres'),
        'score' : int(request.form.get('score')),
        'amazon_affiliate_link' : request.form.get('amazon_affiliate_link')
    })
        
    return redirect(url_for('get_books'))


@app.route('/uploads/<filename>')
def upload(filename):
    return mongo.send_file(filename)


# Set up IP address and Port number
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )