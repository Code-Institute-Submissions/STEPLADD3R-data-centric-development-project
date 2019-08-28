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