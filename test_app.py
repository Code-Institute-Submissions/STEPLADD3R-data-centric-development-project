import app

def test_search_results():
    """
        Test Search Functionality
    """
    search_term = 'AsdSSSSdasdadf123213'
    search_results_count = app.mongo.db.books.count_documents({'$text': {'$search': search_term}})
    if search_results_count < 1:
        search_results = 'Empty'
    else:
        search_results = app.mongo.db.books.find({'$text': {'$search': search_term}})
    assert search_results == 'Empty'