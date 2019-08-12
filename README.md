# CrystaBloges

### 09/08/2019

## By **[Brian Sunday](https://github.com/Sundaybrian/blogger-fest)**

## Description

This is a flask web app that allows users to post blogs,users can comment on them and the owner of the post can delete user comments 

## User Stories

As a user I would like:
* to sign up for an account
* to create blogs
* to update my blog post
* to delete blogs
* to delete comments
* to read other blogs
* to delete comments that are associated with my blog
* to comment on other blogs



## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : john@doe.com  Username : jonDoo  Password : doe | New user is registered |
| User Log in | Your email : john@doe.com  Password : doe | Logged in |
| Create Blog | Click Create Post |Authenticated User is redirected to a form page to create a new Blog |
| View Blog | Click on Blog's title | Redirected to a page that has that single Blog|
| Comment on Blog | Click Comment | Authenticated user is redirected to a form to comment about that Blog|
| Delete a Blog | Click Delete Blog | Authenticated user i.e owner of the blog is prompted to delete|
| Delete a comment | Click Delete Under the comment| Blog Owner is prompted to delete a comment|
| Update profile | click your name while logged in | Redirected to a profile page to set your details |


## Setup/Installation Requirements

* `$ git clone` [Bloger Fest](https://github.com/Sundaybrian/blogger-fest)
* `$ cd bloger-fest`
* `$ touch start.sh ` to create the start.sh file
    ```python
    #set your start.sh as follows and remember to gitignore this file
    export SECRET_KEY='<type some gibberish or random hex values>'
    export MAIL_USERNAME='<your email address>'
    export MAIL_PASSWORD='<your email password>'

    python3.6 manage.py server
    ```    
* `$ python3.6 -m venv virtual` to create a  virtual environment
* `$ source virtual/bin/activate` to activate the virtual environment
* `$ psql` to activate the postgres server
* `$ username=create database blogfest` create db with the name blogfest
* run `$ python3.6 -m pip install -r requirements.txt ` to install dependencies
* `$ python3.6 manage.py db init` to initialize database migrations
* `$ python3.6 manage.py db migrate -m"your commit"` to commit the migration you are running
* `$ python3.6 manage.py db upgrade` to set you models in sync with you database
* In the manage.py change `app = create_app('production')` to `app = create_app('development')`
* Edit `config.py` the propertie ` SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://username:password@localhost/blogfest'` to match you local db credentials where username is the name of your machine(laptop) and password is the password of your db
* Finally run `$ chmod a+x start.sh` to make the start.sh file executable
* `$ ./start.sh` to start the application

## Known Bugs

Profile pictures,display but fail to update
You can't update any of your profile details once registered


## Technologies Used

* Python3.6
* Flask
* Bootstrap
* Postgres Database
* CSS
* HTML

### License

MIT (c) 2019 **[Brian Sunday](https://github.com/Sundaybrian/blogger-fest)**


