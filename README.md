
# Flask Project Template
This project was created how template for
future projects


## Table of Contents
- [Used Technologies](#used-technologies)
- [Environment Variables](#environment-variables)
- [Run Locally](#run-locally)
- [Additional Functions](#additional-functions)


## Used Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)


## Environment Variables
To run this project, you will need to add the 
following environment variables 
to your .env file

***
    HOST=
    PORT=
    FLASK_DEBUG=
    SECRET_KEY=
    SQLALCHEMY_TRACK_MODIFICATIONS=
    DB=
***


## Run Locally
Clone the project

```bash
git clone git@github.com:Danila0987654/python_flask_test_project.git
```

Go to the project directory

```bash
cd python_flask_test_project
```

Create venv, activate it and upgrade pip:

```bash
python3 -m venv venv
. ./venv/bin/activate
pip install -U pip
```

Install dependences:

```bash
pip install -r requirements.txt
```

Init and migrate db:

```bash
flask db init
flask db migrate
flask db upgrade
```

Run project:

```bash
flask run
```


## Additional Functions
Fill a database from a file

```bash
python3 fill_db.py
```