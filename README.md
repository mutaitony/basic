# Simple Python Flask App with Login

### Flask
Flask is a web application framework written in Python. It is developed by Armin Ronacher, who leads an international group of Python enthusiasts named Pocco. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.

### WSGI
Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a specification for a universal interface between the web server and the web applications.

### Werkzeug
It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.

### Jinja2
Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.

Flask is often referred to as a micro framework. It aims to keep the core of an application simple yet extensible. Flask does not have a built-in abstraction layer for database handling, nor does it have form validation support. Instead, Flask supports the extensions to add such functionality to the application. Some of the popular Flask extensions are discussed later in the tutorial.
# Our Project
The project is a basic Flask application with login, register and a dummy Bootstrap Dashboard. You will have to edit that part for your own needs.
## Installation
### Environment
It's a good practice to create a python environment for every python project you'll ever ake for easier management of libraries and requirements.

For this project create an environment using:
```bash
python -m venv myenv
```
And then activate it in Windows using:
```bash
myenv\Scripts\activate
```
Or activate it in Unix Based OS such as MACOS and Linux, using:
```bash
source myenv/bin/activate
```
### Requirements 
We have a requirements.txt file in the project files and that's what we'll use to install all the necessary libraries for the project.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

### Database
Before running anything project-based, we need to set up our database. I prefer using MySQL database for such endeavours because of its simplicity and availability of resources.

First, install XAMPP or WAMP on your computer and start it. Start both apache and MySQL services so that you can get access to the phpMySQL dashboard.

On phpMySQL create a new database and name it ndc_daily_checklist. Or if you prefer a different name, create the DB with that name and then go to the settings folder in the project files, and find settings.py file and edit it to map to the created database 
```python

#the original line
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/ndc_daily_checklist"

#your new line with your <<database name>>
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/<<database name>>"


```


## Usage
After all the installation is done, it's time to run the project.
On your computer bash, CMD, terminal or Powershell navigate to the folder in which your project is situated or if you are using an IDE like Visual Studio Code, open the terminal and run the following command.

```bash
python manage.py
```
If you get this feedback:
```bash
 * Serving Flask app '__init__'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5050
 * Running on http://192.168.43.223:5050
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 516-229-776
```

If not so then, check your requirements or installations.

Thank you

For any support find me using mutai.tony@yahoo.com 
