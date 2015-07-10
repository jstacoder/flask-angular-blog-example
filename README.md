##Flask-Angular-Blog (Example heroku deploy button app)

a fun little blog with a Flask backend and AngularJs frontend.
try out the [demo app](https://phlaskr.herokuapp.com) on heroku


or just start the demo on your own heroku account with __One Click__!
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

####TravisCI Build Status
---
[![Build Status](https://travis-ci.org/jstacoder/flask-angular-blog.svg?branch=master)](https://travis-ci.org/jstacoder/flask-angular-blog)

to hack after youve launched, first install everything in a virtualenv:
```bash
virtualenv venv
. ./venv/bin/activate
pip install -I -r requirements.txt
```
then clone from heroku
```bash
heroku git:clone --app APP_NAME
cd APP_NAME
```
then, just create a file called `local_settings.py` and just add a class for your sensitive settings ie:

```python
class LocalConfig(object):
    SECRET_KEY = 'somesecret'
    DATABASE_URI = 'sqlite:///test.db
```
Dont forget the database part

then run 
```bash
python phlaskr/seed_db.py
```
You setup you `DATABASE_URI` earlier right?

ok... then, (as long as you installed everything inside of a virtualenv (lets hope so) ) 
to get things started you just need to run:

```bash
honcho -f localProcfile start local
```

