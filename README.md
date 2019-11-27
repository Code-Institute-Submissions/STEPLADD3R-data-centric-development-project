# Data Centric Development Project
## By Stuart Green

### Project Overview
I was tasked with creating one of three things, I decided to go with the book review and recommendationg site as it seemed like a good example of what a real world project might look like. The goal of this project was to allow users to find books that they would like to read. It would also make a good place for the creator of the app to make a bit of extra money on the side through the use of Amazon Affiliation.

### User Stories
* A user of the website wants to be able to read reviews about the latest book releases. They can do this by either checking out the books on the homepage or book page, or by searching for a specific book and clicking into it to learn more about it.

* A user would like to search for books by themselves, as oppose to the default staff selected books.
    * The user could use the search menu at the top of the application in the navigation bar. Once they input a search term and hit search, they'll have a page filled with their results.
    * The app only allows for searching by book name at the moment.

* A user would like to find out more information about a book, or many books:
    * The user could choose from either a staff selected pick, a recently uploaded book or go to the books page and view all of the books.
    * Once they have chosen a book, they simply need to click read to read more information about the book, such as author, description, publisher, isbn and more.

* A user would like to add a review to a book:
    * If the user has read the book and would like to let others know their thoughts, they could do so by following the above steps to find said book, and click on the 'Leave a Review' button to post a review.
    * They should fill out the fields, and click submit.

* A user would like to upload a book to the site:
    * Anyone can add a book to the site by clicking the 'Add a Book' button, fields with * are required, and validation is carried out on the front and back-end.

* A user would like to edit a book:
    * The user could find the book they wish to edit, hover over the book cover and select 'edit' rather than 'read'.
    * Alternatively, an 'Edit' button will appear on the page in the menu, if you are viewing the book as opposed to the book covers.
    * The form will be prepopulated with the current values, and again validation is carried out on the front and back-end.

* A user would like to delete a book:
    * Users can delete books from the app by finding the book, clicking through onto the read page, and then a menu item will appear similarly to edit but will say 'Delete'.

* A user would like to browse books by:
    * Users can browse books by genre, staff picks, user rating and upload date in the footer of the website, regardless of the page.
    * Alternatively, users could browse by searching as stated above.

* A user would like to add a genre:
    * Anyone can add a genre to the site by clicking the 'Add a Genre' button, fields with * are required, and validation is carried out on the front and back-end.

* A user would like to edit a genre:
    * The user could go to the genres route, which can be accessed by going to Genres in the menu and selecting view all, then they could select a genre and edit the name of the genre, in case there was a typo.

* A user would like to delete a genre:
    * Users can delete genres from the app by selecting the genre they wish to delete and clicking the 'Delete' button in the menu on the selected genre page.

* As the owner of the website, I'd like to help people find a good read in a place of likeminded individuals. This can be achieved by people using the site to add and review books.

* As the owner of the website, I'd also like to make a bit of money from my hobbie, and as such there is a place to add an Amazon Affiliate link when you add or edit a book. (If this was a fully fledged app with users, it'd be limited to admins, same as staff picks would).

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

I would also have created a Twitter account and utilised the Twitter API to pull in recent posts on the homepage, but for now this is just a static 'tweet'.

It would also be good to in the future instead of storing images inside of the MongoDB, to instead store them inside of an AWS Bucket using Amazon S3 (Amazon Simple Storage Service).

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
I tested the project both manually, and with automated tests.

For my automated tests, I used [Pytest](https://docs.pytest.org/en/latest/contents.html). All of my tests can be found inside of test_app.py and can be tested by running `pytest test_app.py` in the terminal.

My automated tests test the CRUD functionality as well as the search functionality. All of the tests passed as can be seeing inside the 'project-supplements/testing' directory.

Manual testing was also undertaken alongside the automated testing to ensure everything was working.

Below are some of the manual tests undertaken:

* Testing the navigation and hyperlinks (e.g. Leave a Review/Amazon URL etc.) to make sure everything was working.

* Testing the CRUD functionality by creating, reading, editing and deleting multiple books.

* Testing the validation on the CRUD forms works as intended.

* Testing the search functionality by testing book titles I know exist in the database, and book titles that don't exist.

* Testing the responsiveness of the application using a tool called [Browserstack](https://www.browserstack.com/). Using this tool, I tested my website on multiple browsers, devices and operating systems such as:
    * iPhone (5 through to X)
    * iPad
    * iPad Pro
    * Huawei P20
    * Samsung Galaxy S10
    * Samsung Galaxy Tab
    * Google Chrome, Safari, Firefox, Microsoft Edge and IE11

I have also ran my web app through the W3C Validator and it has passed with only a warning (missing a h2-h6 on the testimonial section).

I have also ran my JS through a linter (JSHint) and it comes back with no errors.

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