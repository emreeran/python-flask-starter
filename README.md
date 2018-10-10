# Python Flask Starter Project

A Python starter project using Flask and SQLAlchemy ready for use with AWS. Has default user model and login route set up with Flask-Login as an example.

### Development Environment Setup

---

#### Creating a virtual environment
- If not installed already install virtualenv:
    - Mac OSX `$ sudo easy_install virtualenv`
    - Linux `$ sudo apt-get install python-virtualenv`
    - Windows `$ pip install virtualenv`

- Create python virtual environment `$ python3 -m venv <env_path>`
- Switch to virtual environment `$ source <env_path>/bin/activate`
- Install requirements with `$ pip install -r requirements.txt`

#### Setting up a local database
- Create local MySQL database:
    - Install and run mysql server
    - Execute mysql statement `CREATE DATABASE <database_name>;` to create an empty database.
    - If having problems with queries using `group_by` Execute `SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));`to disable full group by mode.

- Running a local MySQL database on OSX with brew:
    - Launch instance `$ mysql.server start`
    - Launch as a service `$ brew services start mysql`
- Connecting to mysql server with default configurations `$ mysql -u root`
- To quit `> quit;`

- Upgrade pip `$ pip install --upgrade pip`
- After adding new dependencies run in virtual environment: `$ pip freeze > requirements.txt` to add newly added dependencies to requirements.txt.

#### Using AWS Profile
- Install AWS CLI `$ pip3 install awscli --upgrade --user`
- If installed python with brew and `aws` returns "command not found" error, add `export PATH="/Users/<user>/Library/Python/3.6/bin:$PATH"` to your .bash_profile and load it again with
`source .bash_profile`.
- Create AWS profile with `$ aws configure --profile <profile_name>` and enter AWS credentials.

### Included Dependencies

---

#### [Flask][flask]
Flask is a micro-framework for Python based on [Werkzeug][werkzeug] and [Jinja 2][jinja2]
- To install run `$ pip install flask`

##### Requirements that are installed:
- Click
- Flask
- itsdangerous
- Jinja2
- MarkupSafe
- Werkzeug

#### [Flask-SQLAlchemy][flask-sqlalchemy]
An extension for Flask that adds support for SQLAlchemy to your  application.
SQLAlchemy is an open source SQL toolkit and object-relational mapper (ORM) for Python 
- To install run `$ pip install Flask-SQLAlchemy`
- Install mysqlclient `$ pip install mysqlclient`

##### Requirements that are installed:
- SQLAlchemy
- Flask-SQLAlchemy
- mysqlclient

#### [Flask-Login][flask-login]
Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.
- To install run `$ pip install flask-login`

##### Requirements that are installed:
- Flask-Login

#### [Bcrypt][bcrypt]
- To install run `$ pip install bcrypt`

##### Requirements that are installed:
- bcrypt
- cffi
- pycparser
- six

[flask]: http://flask.pocoo.org/
[flask-sqlalchemy]: http://flask-sqlalchemy.pocoo.org/
[flask-login]: https://flask-login.readthedocs.io/en/latest/
[bcrypt]: https://github.com/pyca/bcrypt/
[werkzeug]: http://werkzeug.pocoo.org/
[jinja2]: http://jinja.pocoo.org/
