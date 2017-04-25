# rest_employee
A REST API using Flask and Flasgger 


# Dependencies
 The app depends on multiple packages;

   1. [**Flask Framework**](http://flask.pocoo.org/)- A web micro-framework for Python.
   2. [**Flasgger**](https://pypi.python.org/pypi/flasgger/0.5.2)-A Flask extension that creates Swagger 2.0 API documentation       for all your Flask views extracting specs from docstrings or referenced YAML files. The Swagger UI is embedded and docs         by default available in **/apidocs/index.html**. flasgger provides an extension (Swagger) that inspects the Flask app for       endpoints that contain YAML docstrings with Swagger 2.0 
      [Operation](https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md#operation-object) objects.

**Installation**
```sh
$ git clone https://github.com/BethMwangi/rest_employee.git
$  pip install virtual env
$ . venv/bin/activate
$  cd rest-employee/
$ pip install -r requirements.txt
```


***Now run:***
```sh
$ python app.py
```
  And go to: http://localhost:5000/apidocs/index.html?url=/spec

  
