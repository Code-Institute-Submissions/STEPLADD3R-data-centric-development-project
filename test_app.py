import app


def test_search_results_empty():
    """
        Test Search Functionality
        Test the book we'll create to make sure the search is empty
    """
    search_term = 'Test Book'
    search_results_count = app.mongo.db.books.count_documents(
                           {'$text': {'$search': search_term}})
    if search_results_count < 1:
        search_results = 'Empty'
    else:
        search_results = app.mongo.db.books.find(
                         {'$text': {'$search': search_term}})
    assert search_results == 'Empty'


def test_insert_book():
    """
        Test creating book
    """
    books = app.mongo.db.books
    books.insert_one({
        'name': 'Test Book',
        'description': 'Description',
        'isbn': 'ISBN',
        'publication_date': '27 August 2019',
        'author': 'Author'.lower(),
        'publisher': 'Publisher'.lower(),
        'amazon_affiliate_url': 'https://www.amazon.co.uk/tag=FakeTag'.lower(),
        'genres': ['fantasy'],
        'top_pick': 'on'
    })
    book_query = app.mongo.db.books.find_one({'name': 'Test Book'})
    assert book_query['name'] == 'Test Book'


def test_search_results_not_empty():
    """
        Test Search Functionality
        Now that the book is inserted, it should not be empty
    """
    search_term = 'Test Book'
    search_results_count = app.mongo.db.books.count_documents(
                           {'$text': {'$search': search_term}})
    if search_results_count < 1:
        search_results = 'Empty'
    else:
        search_results = app.mongo.db.books.find(
                         {'$text': {'$search': search_term}})
    assert search_results != 'Empty'


def test_read_book():
    """
        Test reading the book
    """
    the_book = app.mongo.db.books.find_one({'name': 'Test Book'})
    assert the_book['name'] == 'Test Book'


def test_update_book():
    """
        Test updating the book
    """
    the_book = app.mongo.db.books.find_one({'name': 'Test Book'})
    the_book_id = the_book['_id']
    books = app.mongo.db.books
    books.update_one(
        {'_id': app.ObjectId(the_book_id)},
        {
            '$set': {
                'name': 'Test Book Updated',
                'description': 'Description Updated',
                'isbn': 'ISBN Updated',
                'publication_date': '28 August 2019',
                'author': 'Author Updated'.lower(),
                'publisher': 'Publisher Updated'.lower(),
                'amazon_affiliate_url': 'Affiliate Link Updated'.lower(),
                'genres': ['fantasy'],
                'top_pick': 'off'
            }
        }
    )
    the_book_query = app.mongo.db.books.find_one({'name': 'Test Book Updated'})
    assert the_book_query['name'] == 'Test Book Updated'


def test_delete_book():
    """
        Test deleting the book
    """
    the_book = app.mongo.db.books.find_one({'name': 'Test Book Updated'})
    the_book_id = the_book['_id']
    app.mongo.db.books.delete_one({'_id': app.ObjectId(the_book_id)})
    the_book_query = app.mongo.db.books.find_one({'name': 'Test Book Updated'})
    if the_book_query is None:
        assert 'Empty'
    else:
        assert 'Not Empty'


def test_insert_genre():
    """
        Test creating genre
    """
    genres = app.mongo.db.genres
    genres.insert_one({
        'genre': 'test'
    })
    genre_query = app.mongo.db.genres.find_one({'genre': 'test'})
    assert genre_query['genre'] == 'test'


def test_read_genre():
    """
        Test reading the genre
    """
    the_genre = app.mongo.db.genres.find_one({'genre': 'test'})
    assert the_genre['genre'] == 'test'


def test_update_genre():
    """
        Test updating the genre
    """
    the_genre = app.mongo.db.genres.find_one({'genre': 'test'})
    the_genre_id = the_genre['_id']
    genres = app.mongo.db.genres
    genres.update_one(
        {'_id': app.ObjectId(the_genre_id)},
        {
            '$set': {
                'genre': 'test updated',
            }
        }
    )
    the_genre_query = app.mongo.db.genres.find_one({'genre': 'test updated'})
    assert the_genre_query['genre'] == 'test updated'


def test_delete_genre():
    """
        Test deleting the genre
    """
    the_genre = app.mongo.db.genres.find_one({'genre': 'test updated'})
    the_genre_id = the_genre['_id']
    app.mongo.db.genres.delete_one({'_id': app.ObjectId(the_genre_id)})
    the_genre_query = app.mongo.db.genres.find_one({'genre': 'test updated'})
    if the_genre_query is None:
        assert 'Empty'
    else:
        assert 'Not Empty'
