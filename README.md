# Data Centric Development Project
## By Stuart Green

### Project Overview
I was tasked with creating one of three things, I decided to go with the book review and recommendationg site as it seemed like a good example of what a real world project might look like. The goal of this project was to allow users to find books that they would like to read. It would also make a good place for the creator of the app to make a bit of extra money on the side through the use of Amazon Affiliation.

### UX
Details of the UX design process is available inside the 'project-supplements/user-experience' directory. This directory contains an array of documents that illustrate the UX design process in the form of wireframes.

### Database
Details of the Database design process is available inside the 'project-supplements/database-design' directory. This directory contains an array of documnents that illustrate how I came to decide on the database collections and fields.

### Features
#### Existing Features
This is a web application that allows users to peruse a list of books and reviews. It is a full stack web application (front-end and back-end) that provides CRUD (Create, Read, Update, Delete) functionality to a database. This application uses HTML, CSS and jQuery as the front-end, Python/Flask as the back-end and MongoDB as the database.

Features that the users can utilise:
#### Books
1. Cread Book: Allows users to add a new book and add details that relate to that book, e.g. name, cover photo, genre, etc.
2. Read Book: Allows users to click into the books on the application and read more information regarding the book, as well as read reviews people have posted.
3. Update Book: Allows users to be able to update information on a book, be it one field or many fields.
4. Delete Book: Allows users to be able to remove a book from the application.

#### Genres
1. Create Genre: Allows users to add a new genre, and provide a genre name.
2. Update Genre: Allows users to update the genre, providing a new genre name.
3. Delete Genre: Allows users to delete a genre completely.
4. Browse By Genre: Allows users to browse books of only a certain genre.

#### Reviews
This feature allows users to post a review that relates to a specific book and provide a rating out of 5. Ratings are showed in the review and an average score is calculated based on the users reviews.

#### Book Search
This feature allows the user to search for books of a certain name, if they are looking for a specific book, this is how they would find it.

### Features for the Future
In the future, I would like to add a user roles to the application, so that only specific users can handle the creating, updating and deleting of books and genres. It would also be good to have the user sign up before posting a review, to limit the amount of fake reviews that may be posted on the application.

### Technologies
Here's a list of technologies used:

1. HTML5 - Used for marking up the DOM.
2. SCSS (CSS Pre Processor) - Used to create the styling.
3. jQuery - Used to provide some neat functionalities such as popup modals, toast notifications and more.
4. Gulp - Used to automate my workflow, e.g. image minification, javascript minification as well as processing my SCSS into CSS.
5. NPM - Used to pull in packages, such as Bootstrap so that I could control the SCSS more easily.
6. Git - Used to handle version control
7. Python & Flask - Python Framework to handle config, routes and more.
8. MongoDB - Database of choice

### Testing
Details of the project testing process is available inside the 'project-supplements/testing' directory.

### Deployment
To deploy the application, I chose to use Heroku, below are the steps I took to get the project up and running on Heroku.

1. Created requirements.txt `pip3 freeze --local > requirements.txt` and a Procfile `echo web: python app.py > Procfile`
2. Created the Heroku App, then followed the steps provided by Heroku to deploy using Heroku CLI (these can be found inside the 'Deploy' section of Heroku)
3. In the 'Settings' section of Heroku, add in the config vars that matched my environmental variables in app.py
4. Application now live!

### Demo
A demo of the application can be found here: [Demo](https://data-centric-dev-project-mongo.herokuapp.com)

### Credits

__Stuart Green__ - This project was created and built as a part of the Code Institute Full Stack Development course.

#### Content & Media
I took the content and media of the books on this project application from [LoveReading  UK](https://www.lovereading.co.uk/). This was used to pad out the site in terms of having some books to show, and if the project was ever taken into the real world, the images and content from this site would NOT be used.