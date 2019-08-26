import os
from datetime import datetime
from flask import Flask, flash, render_template, redirect, request, url_for
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Create an instance of a Flask app
app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Mongo DB Setup
app.config['MONGO_DBNAME'] = 'book_reviewer'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

# File Upload Config
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

mongo = PyMongo(app)

@app.context_processor
def global_template_variables():
    navbar_genres = mongo.db.genres.find().limit(4)
    footer_genres = mongo.db.genres.find()
    footer_top_picks = mongo.db.books.find({ 'top_pick' : 'on' }).limit(4)
    footer_user_picks = mongo.db.genres.find();
    footer_recent_books = mongo.db.books.find().sort([( '$natural', -1 )]).limit(4)
    return dict(navbar_genres=navbar_genres, footer_genres=footer_genres, footer_top_picks=footer_top_picks, footer_user_picks=footer_user_picks, footer_recent_books=footer_recent_books)


# File Upload Helper Functions
# Checks if the extension is allowed
def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# Retrieve the URL of the upload from MongoDB
@app.route('/uploads/<filename>')
def upload(filename):
    return mongo.send_file(filename)


# Get the search term
@app.route('/search/', methods=['POST'])
@app.route('/books/search/', methods=['POST'])
def search_books():
    search_term = request.form.get('search_term')
    return redirect(url_for('search_results', search_term=search_term))


# Return the search results
@app.route('/search/<search_term>')
@app.route('/books/search/<search_term>')
def search_results(search_term):
    mongo.db.books.create_index([( 'name', 'text' )])
    search_results = mongo.db.books.find({ '$text': { '$search' : search_term } }).limit(8)
    search_results_count = mongo.db.books.find({ '$text': { '$search' : search_term } }).count()
    return render_template('search-results.html', search_term=search_term, search_results=search_results, search_results_count=search_results_count)


#
#   BOOKS
#
# Return top picks and recent books
@app.route('/')
@app.route('/books')
def get_books():
    top_picks = mongo.db.books.find({ 'top_pick' : 'on' }).sort([( '$natural', -1 )]).limit(8)
    recent_books = mongo.db.books.find().sort([( '$natural', -1 )]).limit(8)
    return render_template('books.html', top_picks=top_picks, recent_books=recent_books)


# Create Book (Form)
@app.route('/book/add')
def create_book():
    genres = mongo.db.genres.find()
    return render_template('create-book.html', genres=genres)


# Insert into the DB
@app.route('/book/insert', methods=['POST'])
def insert_book():
    if 'cover_photo' not in request.files:
        flash('The uploaded file MUST have a file name.', 'error')
        return redirect(url_for('create_book'))

    cover_photo = request.files['cover_photo']

    if cover_photo.filename == '':
        flash('The uploaded file MUST have a file name.', 'error')
        return redirect(url_for('create_book'))

    if cover_photo and allowed_file(cover_photo.filename):
        secure_cover_photo_filename = secure_filename(cover_photo.filename)
        mongo.save_file(secure_cover_photo_filename, cover_photo)
        books = mongo.db.books
        books.insert_one({
            'name' : request.form.get('name'),
            'cover_photo' : secure_cover_photo_filename,
            'description' : request.form.get('description'),
            'isbn' : request.form.get('isbn'),
            'publication_date' : request.form.get('publication_date'),
            'author' : request.form.get('author').lower(),
            'publisher' : request.form.get('publisher').lower(),
            'amazon_affiliate_url' : request.form.get('amazon_affiliate_url').lower(),
            'genres' : request.form.getlist('genres'),
            'top_pick' : request.form.get('top_pick')
        })
        flash('Upload Successful.', 'success')
        return redirect(url_for('get_books'))
    else:
        flash('Something has gone wrong, please try again.', 'error')
        return redirect(url_for('create_book'))


# Read Book
@app.route('/book/<book_id>')
def read_book(book_id):
    the_book = mongo.db.books.find_one({ '_id' : ObjectId(book_id) })
    genres = mongo.db.genres.find()
    reviews = mongo.db.reviews.find({ 'book_id' : book_id })
    
    ratings = [1, 3, 5]
    average_rating = sum(ratings) / len(ratings)
    
    return render_template('read-book.html', book=the_book, genres=genres, reviews=reviews, average_rating=average_rating)


# Update Book (Form)
@app.route('/book/<book_id>/edit')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({ '_id' : ObjectId(book_id) })
    return render_template('edit-book.html', book=the_book, genres=mongo.db.genres.find())


# Update the DB
@app.route('/book/<book_id>/update', methods=['POST'])
def update_book(book_id):
    if 'cover_photo' in request.files:
        cover_photo = request.files['cover_photo']

        books = mongo.db.books

        if cover_photo.filename == '':
            books.update_one(
                {'_id' : ObjectId(book_id)},
                {
                    '$set': {
                        'name' : request.form.get('name'),
                        'description' : request.form.get('description'),
                        'isbn' : request.form.get('isbn'),
                        'publication_date' : request.form.get('publication_date'),
                        'author' : request.form.get('author').lower(),
                        'publisher' : request.form.get('publisher').lower(),
                        'amazon_affiliate_url' : request.form.get('amazon_affiliate_url').lower(),
                        'genres' : request.form.getlist('genres'),
                        'top_pick' : request.form.get('top_pick')
                    }
                }
            )
            flash('Update Successful.', 'success')
            return redirect(url_for('get_books'))
        else:
            if allowed_file(cover_photo.filename):
                secure_cover_photo_filename = secure_filename(cover_photo.filename)
                mongo.save_file(secure_cover_photo_filename, cover_photo)
                books.update_one(
                    {'_id' : ObjectId(book_id)},
                    {
                        '$set': {
                            'name' : request.form.get('name'),
                            'cover_photo' : secure_cover_photo_filename,
                            'description' : request.form.get('description'),
                            'isbn' : request.form.get('isbn'),
                            'publication_date' : request.form.get('publication_date'),
                            'author' : request.form.get('author').lower(),
                            'publisher' : request.form.get('publisher').lower(),
                            'amazon_affiliate_url' : request.form.get('amazon_affiliate_url').lower(),
                            'genres' : request.form.getlist('genres'),
                            'top_pick' : request.form.get('top_pick')
                        }
                    }
                )
                flash('Update Successful.', 'success')
                return redirect(url_for('get_books'))
            else:
                flash('Something has gone wrong, please try again.', 'error')
                return redirect(url_for('edit_book', book_id=ObjectId(book_id)))


# Delete Book
@app.route('/book/<book_id>/delete')
def delete_book(book_id):
    mongo.db.books.remove({'_id' : ObjectId(book_id)})
    flash('Delete Successful.', 'success')
    return redirect(url_for('get_books'))


#
#   GENRES
#
# Returns a list of genres
@app.route('/genres')
def get_genres():
    genres = mongo.db.genres.find()
    return render_template('genres.html', genres=genres)


# Create Genre (Form)
@app.route('/genre/add')
def create_genre():
    return render_template('create-genre.html')


# Insert into the DB
@app.route('/genre/insert', methods=['POST'])
def insert_genre():
    genres = mongo.db.genres
    genres.insert_one({
        'genre' : request.form.get('genre').lower(),
    })
    flash('Upload Successful.', 'success')
    return redirect(url_for('get_genres'))


# Read Genre (from Books)
@app.route('/genre/<genre>')
def read_genre(genre):
    the_genre = genre
    books = mongo.db.books.find({ 'genres' : genre })
    return render_template('read-genre.html', the_genre=the_genre, books=books)


# Update Genre (Form)
@app.route('/genre/<genre_id>/edit')
def edit_genre(genre_id):
    the_genre = mongo.db.genres.find_one({ '_id' : ObjectId(genre_id) })
    return render_template('edit-genre.html', genre=the_genre)


# Update the DB
@app.route('/genre/<genre_id>/update', methods=['POST'])
def update_genre(genre_id):
    genres = mongo.db.genres
    
    genres.update_one(
        {'_id' : ObjectId(genre_id)},
        {
            '$set': {
                'genre' : request.form.get('genre')
            }
        }
    )
    flash('Update Successful.', 'success')
    return redirect(url_for('get_genres'))


# Delete Genre
@app.route('/genre/<genre_id>/delete')
def delete_genre(genre_id):
    mongo.db.genres.remove({'_id' : ObjectId(genre_id)})
    flash('Delete Successful.', 'success')
    return redirect(url_for('get_genres'))


#
#   REVIEWS
#
# Insert into the DB
@app.route('/book/<book_id>/review/insert', methods=['POST'])
def insert_review(book_id):
    reviews = mongo.db.reviews
    reviews.insert_one({
        'book_id' : request.form.get('book_id'),
        'posted_at' : datetime.utcnow(),
        'author' : request.form.get('author'),
        'review' : request.form.get('review'),
        'rating' : int(request.form.get('rating')),
    })
    flash('Upload Successful.', 'success')
    return redirect(url_for('read_book', book_id=book_id))


# Set up IP address and Port number
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )