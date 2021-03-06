WebApp to get all the GitHub Users stored on a local sqllite database
=====================================================================


# WebApp GitHub Users

WebApp to get all the GitHub Users stored on a local sqllite database. Using Flask, SQLAlchemy, Jinja2.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
- Python 3.7
- Pip
- Virtual Enviroment
- Libraries:
    alembic==1.4.3
    aniso8601==8.1.0
    certifi==2020.12.5
    chardet==4.0.0
    click==7.1.2
    Flask==1.1.2
    flask-marshmallow==0.14.0
    Flask-Migrate==2.5.3
    Flask-RESTful==0.3.8
    Flask-SQLAlchemy==2.4.4
    idna==2.10
    itsdangerous==1.1.0
    Jinja2==2.11.2
    Mako==1.1.3
    MarkupSafe==1.1.1
    marshmallow==3.10.0
    marshmallow-sqlalchemy==0.24.1
    python-dateutil==2.8.1
    python-editor==1.0.4
    pytz==2020.4
    requests==2.25.1
    six==1.15.0
    SQLAlchemy==1.3.22
    urllib3==1.26.2
    Werkzeug==1.0.1
```

### Installing

You need to have a python virtual environment for the project that uses python version 3.7

```
C:\Users\franciscoyu\PycharmProjects\apifrancsicoyu>python -m venv venv
```

Before to enable the virtual enviroment, you need to add the next Enviroment Variables on the file C:\Users\franciscoyu\PycharmProjects\apifrancsicoyu\vev\Scripts\activate.bat if you are using Windows at the end of file.

```
if not defined FLASK_APP (
    set "FLASK_APP=entrypoint:app"
)

if not defined FLASK_ENV (
    set "FLASK_ENV=development"
)

if not defined APP_SETTINGS_MODULE (
    set "APP_SETTINGS_MODULE=config.default"
)
```
Or /usr/[Home]/[Project]/venv/bin/activate if you are using Linux. With the next lines at the end of file.

```
export FLASK_APP = "entrypoint:app"
export FLASK_ENV = "development"
export APP_SETTINGS_MODULE = "config.default"
```

Enable the virtual enviroment already created

```
C:\Users\franciscoyu\PycharmProjects\apifrancsicoyu>venv\Scripts\activate
```

Deploy the application on the directory where you created the venv enviroment, and install the requirements that the application need using the next command

```
(venv) C:\Users\franciscoyu\PycharmProjects\apifrancsicoyu>pip install -r requirements.txt
```


To populate the SQLite database you need to use the proyect webappfranciscoyu in this <a href="https://github.com/fyudelgado/webappfranciscoyu">link</a>

You could run both proyects and only have the references between both databases. (Only you need to change the port used by each application)

To run the API Rest proyect, you could use the following command.

```
(venv) C:\Users\franciscoyu\PycharmProjects\apifrancsicoyu>flask run
```

You can see that the server is running and waiting for requests when you see the next information on the console

```
(venv) C:\Users\franciscoyu\PycharmProjects\apifranciscoyu>flask run
 * Serving Flask app "entrypoint:app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 497-891-302
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

## Running the tests

You could check and test the web application opening a browser like Google Chrome or Firefox and enter the next URL

You need to provide an a Id or a username parameter on the query parameter, to get the details of the User (Profile) on JSON format.

```
http://127.0.0.1:5000/api/v1/profiles/?id=3
```

### Filters

You could test the filters using the next parameters on the URL

You need to provide an id or a username parameter
```
http://127.0.0.1:5000/api/v1/profiles/?id=2
or
http://127.0.0.1:5000/api/v1/profiles/?username=defunkt
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org/) - Python 3.7
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - Flask-RESTful extension
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask Framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM Database

## Authors

* **Francisco Yu** - *Initial work* - [fyudelgado](https://github.com/fyudelgado)

See also the list of [contributors](https://github.com/fyudelgado/apifranciscoyu/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
