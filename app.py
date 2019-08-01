import os
from flask import Flask

# Create an instance of a Flask app
app = Flask(__name__)

@app.route('/')
def test():
    return 'Test'


# Set up IP address and Port number
if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
    )