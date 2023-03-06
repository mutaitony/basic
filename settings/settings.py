from __init__ import app   

app.config["PROJECT_NAME"] = "NDC Daily Checklist"
app.config["PROJECT_AUTHOR"] = "Mutai Tony"
app.config["VERSION"] = "1.0"
app.config["SECRET_KEY"] = "vscdc7823239<?/./evccsicfvvk-fv8fy8943fdh348gc7ercgcgerukfu3f_efvfiurfh2374ry0349r83493g0234tcne834014hr234r13r91347r43134r"
app.config["TIMEZONE"] = "Africa/Nairobi"
app.config["HOST"] = "localhost:5050"
app.config["SERVER_NAME"] = "localhost:5050"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/ndc_daily_checklist"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 50
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 50
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["MAX_CONTENT_LENGTH"] = 10485760
app.config["ALLOWED_EXTENSIONS"] = {'txt','pdf','png','jpg','jpeg','gif'}
app.config["UPLOAD_FOLDER"] = "static/uploads"