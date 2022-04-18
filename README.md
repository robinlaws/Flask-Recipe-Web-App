# python-recipes-web-app

“EGG-2-Z” is a recipe website which includes recipes fit for everyone. It is a web-based application written with Python, JavaScript, and html languages using the flask python web app framework. Once the user has signed up, 3 default recipes will be added to their account. From here, the user can add recipes, delete recipes, leave recipe reviews, and view their previous reviews. Login is required to view recipes, and if the user does not have an account, the signup page will allow registration. The home page displays a short message and will give links to either login or sign up.

Pages included with this app are as follows:
•	Home page
o	Displays a welcome message and general information about the web app
o	If the user is signed in, the home page will display a personalized greeting with username.
o	If the user is not signed in, the home page will allow the user to either sign up or login.
•	Login page
o	User login to access personal recipe page
o	includes a link to sign up and home page from navigation bar
o	Asks user for email and password. If correct, it will direct user to their recipe page.
•	Signup page
o	If the user does not have an account, they will be able to create one on the sign-up page
o	Requires email, password, password confirmation, and first name
o	Includes link to home or login page on nav bar.
•	Recipe page
o	This is the page where all recipes in user account are displayed.
o	includes links to my account and logout page.
o	Requires login to access recipes
•	My  account page
o	Page where the user can add recipes or remove recipes from their account. 
o	User can leave reviews and view reviews for any recipe in their account.
o	Includes links recipes and logout page.
o	Requires login to access this page
Description

	To run this application locally, the app will be created using the main.py file found in the package. With the directory in place as described below, run main.py to create the flask app at http://127.0.0.1:5000/. Type this link into your browser or click the link in your IDE and you will be able to view the full application.

	Recipe database is saved in a CSV file named ‘recipes.csv’. This is located in the same directory as the main python file. When a user signs up, their account details are saved in a database.db file which is in the website folder.


Summary of files in package

•	Main Directory:
•	Main.py – used to create the application 
•	Recipes.csv – stores website database for displaying recipes
•	Website Folder:
o	Database.db – used for user accounts
o	Models.py – includes objects and methods to write and read from csv
o	Views.py – blueprint for each website link and handles form data 
o	__init__.py – called from main.py, creates app, database, initializes the site
•	Static Folder:
o	Stylesheet.css – used for website styling
o	Index.js – JavaScript for data handling
•	Template Folder:
o	Base.html – main template which will style all website pages
o	Home.html – home html template
o	Login.html – login html template
o	my_account.html – account html template
o	recipes.html – recipes html template
o	sign_up.html – sign up html template


