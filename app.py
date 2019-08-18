import os
from flask import Flask, flash, render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Create an instance of a Flask app
app = Flask(__name__)

# Mongo DB Setup
app.config['MONGO_DBNAME'] = 'book_reviewer'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
# File Upload
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

mongo = PyMongo(app)

# File Upload Helper Functions
# Used to check extensions allowed
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# Used to retrieve the URL of the upload from MongoDB
@app.route('/uploads/<filename>')
def upload(filename):
    return mongo.send_file(filename)


@app.route('/')
@app.route('/books')
def get_books():
    return render_template('books.html', top_books=mongo.db.books.find(), new_books=mongo.db.books.find())


@app.route('/book/add')
def create_book():
    return render_template('create-book.html', genres=mongo.db.genres.find())


@app.route('/book/insert', methods=['POST'])
def insert_book():
    if 'book_cover_photo' not in request.files:
        return redirect(url_for('create_book'))

    book_cover_photo = request.files['book_cover_photo']

    if book_cover_photo.filename == '':
        flash('The uploaded file MUST have a file name.')
        return redirect(url_for('create_book'))

    if book_cover_photo and allowed_file(book_cover_photo.filename):
        secure_book_cover_photo_filename = secure_filename(book_cover_photo.filename)
        mongo.save_file(secure_book_cover_photo_filename, book_cover_photo)
        books = mongo.db.books
        books.insert_one({
            'book_name' : request.form.get('book_name'),
            'book_cover_photo' : secure_book_cover_photo_filename,
            'book_description' : request.form.get('book_description'),
            'book_press_reviews' : request.form.get('book_press_reviews'),
            'isbn' : request.form.get('isbn'),
            'publication_date' : request.form.get('publication_date'),
            'author' : request.form.get('author'),
            'publisher' : request.form.get('publisher'),
            'genres' : request.form.getlist('genres'),
            'score' : int(request.form.get('score')),
            'amazon_affiliate_link' : request.form.get('amazon_affiliate_link')
        })
        return redirect(url_for('get_books'))
    else:
        return redirect(url_for('create_book'))


# read
@app.route('/book/<book_id>')
def read_book(book_id):
    the_book = mongo.db.books.find_one({ '_id' : ObjectId(book_id) })
    return render_template('read-book.html', book=the_book, genres=mongo.db.genres.find())


@app.route('/book/<book_id>/edit')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({ '_id' : ObjectId(book_id) })
    return render_template('edit-book.html', book=the_book, genres=mongo.db.genres.find())


@app.route('/book/<book_id>/update', methods=['POST'])
def update_book(book_id):
    if 'book_cover_photo' in request.files:
        book_cover_photo = request.files['book_cover_photo']

        # if book_cover_photo.filename = '':
        #     flash('The uploaded file MUST have a file name.')
        #     return redirect(request.url)

        books = mongo.db.books

        if book_cover_photo.filename == '':
            books.update_one(
                {'_id' : ObjectId(book_id)},
                {
                    '$set': {
                        'book_name' : request.form.get('book_name'),
                        'book_description' : request.form.get('book_description'),
                        # 'book_press_reviews' : request.form.get('book_press_reviews'),
                        'isbn' : request.form.get('isbn'),
                        'publication_date' : request.form.get('publication_date'),
                        'author' : request.form.get('author'),
                        'publisher' : request.form.get('publisher'),
                        'genres' : request.form.getlist('genres'),
                        'score' : int(request.form.get('score')),
                        'amazon_affiliate_link' : request.form.get('amazon_affiliate_link')
                    }
                }
            )
            # print( ObjectId(book_id) )
            print( 'This is empty... but the value of cover_photo is still set to null after this operation' )
            return redirect(url_for('get_books'))
        else:
            if allowed_file(book_cover_photo.filename):
                secure_book_cover_photo_filename = secure_filename(book_cover_photo.filename)
                mongo.save_file(secure_book_cover_photo_filename, book_cover_photo)
                books.update_one(
                    {'_id' : ObjectId(book_id)},
                    {
                        'book_name' : request.form.get('book_name'),
                        'book_cover_photo' : secure_book_cover_photo_filename,
                        'book_description' : request.form.get('book_description'),
                        'book_press_reviews' : request.form.get('book_press_reviews'),
                        'isbn' : request.form.get('isbn'),
                        'publication_date' : request.form.get('publication_date'),
                        'author' : request.form.get('author'),
                        'publisher' : request.form.get('publisher'),
                        'genres' : request.form.getlist('genres'),
                        'score' : int(request.form.get('score')),
                        'amazon_affiliate_link' : request.form.get('amazon_affiliate_link')
                    }
                )
                print( 'I\'m not even ran' )
                return redirect(url_for('get_books'))
            else:
                return redirect(url_for('edit_book', book_id=ObjectId(book_id)))


@app.route('/book/<book_id>/delete')
def delete_book(book_id):
    mongo.db.books.remove({'_id' : ObjectId(book_id)})
    return redirect(url_for('get_books'))


# Set up IP address and Port number
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )