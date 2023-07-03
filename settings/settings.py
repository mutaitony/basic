from __init__ import app   
from datetime import datetime

app.config["PROJECT_NAME"] = "NDC Daily Checklist"
app.config["PROJECT_AUTHOR"] = "Mutai Tony"
app.config["VERSION"] = "1.0"
app.config["YEAR"] = datetime.now().strftime('%Y')
app.config["SECRET_KEY"] = "vscdc7823239<?/./evccsicfvvk-fv8fy8943fdh348gc7ercgcgerukfu3f_efvfiurfh2374ry0349r83493g0234tcne834014hr234r13r91347r43134r"
app.config["TIMEZONE"] = "Africa/Nairobi"
# app.config["HOST"] = "localhost.localdomain:5050"
app.config["PORT"] = 5050
# app.config["SERVER_NAME"] = "localhost.localdomain:5050"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:AutoLinkAWS2022@autolink.crc1i8e8xwee.af-south-1.rds.amazonaws.com/ndc_daily_checklist"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://rentnasi_ndc_admin:gX35(svBNZYb@localhost/rentnasi_ndc"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/ndc_daily_checklist"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 50
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 50
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["MAX_CONTENT_LENGTH"] = 10485760
app.config["ALLOWED_EXTENSIONS"] = {'txt','pdf','png','jpg','jpeg','gif'}
app.config["UPLOAD_FOLDER"] = "static/uploads"

# BJegdw6e0(CS