from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import UserMixin,login_user,login_required,logout_user,current_user,LoginManager
import os, pymysql
from flask_toastr import Toastr
from werkzeug.exceptions import HTTPException

app = Flask(__name__, template_folder= 'Templates')

from settings.settings import *

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

db = SQLAlchemy(app)
toastr = Toastr(app)

app.app_context().push()

# engine_container = db.get_engine(app)

app.config['SESSION_SQLALCHEMY'] = db
Session(app)

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "/login"
# login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from models.models import *

@login_manager.user_loader
def load_user(user_id):
    if user_id:
        return Users.query.get(user_id)
    
# @login_manager.request_loader
# def request_loader(request, user):
#     return user
    
@app.errorhandler(HTTPException)
def error_handler(e):
    response = e.get_response()
    agent = request.environ.get('HTTP_USER_AGENT')
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
        'source': agent
    })
    # response.content_type = "application/json"
    # return make_response(response, e.code)
    return make_response(render_template('admin/pages/404.html', code = e.code, name = e.name,description = e.description,))



