#  Setup and Running 
### Setup
extract all the file and use pip to download all the libraries to execute the project
```console
$ pip install -r requirements.txt
```
### First time FLASK create DB
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=DEVELOPMENT
$ flask run
```
once you get the URL for the created flask environment user ctrl+click (if you are using VSC)

### to create the database
This is to ensure that the database is created on the system and also to ensure that if there is any updation in code the database can be updated to 
```console
$ python
>>> from app import db
>>> db.create_all()
>>> exit()
```
###  execution of python project 
you can use the normal python app.py
```console
$ python app.py
```


