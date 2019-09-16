import app

def test_search_results_empty():
    """
        Test Search Functionality
        Test the book we'll create to make sure the search is empty
    """
    search_term = 'Test Book'
    search_results_count = app.mongo.db.books.count_documents({'$text': {'$search': search_term}})
    if search_results_count < 1:
        search_results = 'Empty'
    else:
        search_results = app.mongo.db.books.find({'$text': {'$search': search_term}})
    assert search_results == 'Empty'


def test_insert_book():
    """
        Test creating book
    """
    books = app.mongo.db.books
    books.insert_one({
        'name': 'Test Book',
        'cover_photo': 'test.jpg', # come back to image upload
        'description': 'Description',
        'isbn': 'ISBN',
        'publication_date': '27 August 2019',
        'author': 'Author'.lower(),
        'publisher': 'Publisher'.lower(),
        'amazon_affiliate_url': 'https://www.amazon.co.uk/book&tag=FakeTag'.lower(),
        'genres': ['fantasy'],
        'top_pick': 'on'
    })
    book_query = app.mongo.db.books.find_one({ 'name': 'Test Book'})
    assert book_query['name'] == 'Test Book'


def test_search_results_not_empty():
    """
        Test Search Functionality
        Now that the book is inserted, it should not be empty
    """
    search_term = 'Test Book'
    search_results_count = app.mongo.db.books.count_documents({'$text': {'$search': search_term}})
    if search_results_count < 1:
        search_results = 'Empty'
    else:
        search_results = app.mongo.db.books.find({'$text': {'$search': search_term}})
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
                'cover_photo': 'test.jpg', # come back to image upload
                'description': 'Description Updated',
                'isbn': 'ISBN Updated',
                'publication_date': '28 August 2019',
                'author': 'Author Updated'.lower(),
                'publisher': 'Publisher Updated'.lower(),
                'amazon_affiliate_url': 'https://www.amazon.co.uk/book&tag=FakeTagUpdated'.lower(),
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
    if the_book_query == None:
        assert 'Empty'
    else:
        assert 'Not Empty'