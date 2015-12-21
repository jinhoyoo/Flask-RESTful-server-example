RESTful and Web server with Flask example
===================
 
 The prototyping of web server and RESTful server with Flask framework in Python.

Run service
----------------
* Run ```python web_server.py```.
 - Will use ngnix server.


Test service
----------------
* Run ```run_test.sh```.
 - Uses ```uniitest``` and ```nosetest``` framework.


Plug-ins that I used.
-------------------

### RESTful API framework ###
 * [Flask-restful](http://flask-restful-cn.readthedocs.org/en/0.3.4/)

### DB###
  * We uses Mongo db. Flask has plugin for mongodb, [Flask-PyMongo](https://flask-pymongo.readthedocs.org/en/latest/).

### Test framework ###
 * [Flask-Testing](https://flask-testing.readthedocs.org/en/latest/#installing-flask-testing)
 * [Nose test framework](https://nose.readthedocs.org/en/latest/)


Reference
---------
1. [Project structure of flask framework](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
2. [PEP008: Python code convention](https://www.python.org/dev/peps/pep-0008/#code-lay-out)
