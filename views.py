from __init__ import *
from forms.forms import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
# from fpdf import FPDF, HTMLMixin 

def index():
    return make_response(render_template('index.html'))

def login():
    form = login_form()
    if form.validate_on_submit():
        try:
            user = Users.query.filter_by(email=form.email.data).first()
            if user:
                if check_password_hash(user.pwd, form.pwd.data):
                    # user.id = user.email
                    login_user(user)
                    if request.args.get('next'):
                        return redirect(request.args.get('next'))
                    else:
                        return redirect(url_for('dashboard'))
                else:
                    flash("Invalid Username or password!", "error")
            else:
                flash("User does not exist!", "error")
        except Exception as e:
            flash('Error during login!', "error")
    return make_response(render_template('auth.html', form = form))
def validEmail(email):
    valid = False
    user = Users.query.filter_by(email=email).first()
    if user:
        valid = True
    return valid

def EnterLogs(logs_type, logs_id):
    try:
        new = LogsModel(
            user = current_user.id,
            logs_type = logs_type,
            log_id = logs_id, 
        )
        db.session.add(new)
        db.session.commit()
        return True
    except Exception as e:
        return False

def register():
    if request.method == 'POST':
        try:
            values = request.form
            
            if validEmail(values.get('email')):
                flash('Email address already used by another account', "error")
                return redirect(url_for("settings"))
            
            email = values.get('email')
            name = values.get('name')
            username = f"ndc{values.get('job_id')}"
            pwd = "123456789"
            
            newuser = Users(
                username=username,
                name=name,
                email=email,
                phone = values.get('phone'),
                job_id = values.get('job_id'),
                job_title = values.get('job_title'),
                pos = values.get('usertype'),
                pwd=generate_password_hash(pwd),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Succesful. Default password is 123456789 and username is {username}", "success")
            return redirect(url_for("settings"))

        except Exception as e:
            flash('Error adding user', "error")
            return redirect(url_for("settings"))
        
    flash('An Unknown error occured', "error")
    return redirect(url_for("settings"))

@login_required
def dashboard():
    return make_response(render_template('admin/ndc/index.html'))

@login_required
def delete_account():
    if request.method == 'POST':
        data = request.form
        
        flash('Successfully deleted the account', 'success')
        return redirect(url_for('logout'))
    
    flash('Account not deleted', 'error')
    return make_response(redirect('settings'))
@login_required
def change_email():
    if request.method == 'POST':
        data = request.form
        user = Users.query.filter_by(email=current_user.email).first()
        user.email = data.get('new_email')
        
        db.session.commit()
        flash('Email changed successfully', 'success')
        current_user.email = data.get('new_email')
    return make_response(redirect('settings'))

@login_required
def change_password():
    if request.method == 'POST':
        data = request.form
        user = Users.query.filter_by(email=current_user.email).first()
        if check_password_hash(user.pwd, data.get('old_password')):
            user.pwd = generate_password_hash(data.get('new_password'))
            db.session.commit()
            flash('Password changed successfully', 'success')
        else:
            flash('The old password is incorrect!', 'error')
    return make_response(redirect('settings'))

@login_required
def change_username():
    if request.method == 'POST':
        data = request.form
        user = Users.query.filter_by(email=current_user.email).first()
        user.username = data.get('username')
        
        db.session.commit()
        flash('Username changed successfully', 'success')
        current_user.username = data.get('username')
    
    return make_response(redirect('settings'))

@login_required
def change_name():
    if request.method == 'POST':
        data = request.form
        user = Users.query.filter_by(email=current_user.email).first()
        user.name = f"{data.get('first_name')} {data.get('last_name')}"
        
        db.session.commit()
        flash('Name changed successfully', 'success')
        current_user.name = f"{data.get('first_name')} {data.get('last_name')}"
    
    return make_response(redirect('settings'))

@login_required
def settings():
    return render_template('admin/ndc/settings.html')
@login_required
def logs():
    logs = db.session.query(LogsModel.id, 
                            LogsModel.date, 
                            LogsModel.log_id, 
                            LogsModel.logs_type,
                            Users.name,
                            Users.email)\
                                .outerjoin(Users, Users.id == LogsModel.user)\
                                .order_by(LogsModel.id.desc())\
                                .all()
    
    return render_template('admin/ndc/logs.html', logs = logs)
@login_required
def priview_logs():
    if request.method == 'POST':
        data = request.values
        if data.get('logs_type') == 'power_rooms_logs':
            log_data = PowerRooms.query.filter_by(id = data.get('log_id')).first()
            return make_response(jsonify(log_data.data))
        if data.get('logs_type') == 'generators_logs':
            log_data = Generators.query.filter_by(id = data.get('log_id')).first()
            return make_response(jsonify(log_data.data))
        if data.get('logs_type') == 'white_spaces_logs':
            log_data = WhiteSpace.query.filter_by(id = data.get('log_id')).first()
            return make_response(jsonify(log_data.data))

@login_required
def new():
    return render_template('admin/ndc/new.html')

@login_required
def dc_white_space():
    return render_template('admin/ndc/dc_white_space.html')
@login_required
def comments():
    midnight = datetime.combine(date.today(), datetime.min.time())
    generators = Generators.query.filter(Generators.date <= datetime.now()).filter(Generators.date >= midnight).order_by(Generators.id.desc()).first()
    whitespace = WhiteSpace.query.filter(WhiteSpace.date <= datetime.now()).filter(WhiteSpace.date >= midnight).order_by(WhiteSpace.id.desc()).first()
    power_rooms =  PowerRooms.query.filter(PowerRooms.date <= datetime.now()).filter(PowerRooms.date >= midnight).order_by(PowerRooms.id.desc()).first()

    
    if not generators:
        flash('No generators information available today', 'error')
        return redirect(url_for('generators'))
    if not whitespace:
        flash('No DC white space information available today', 'error')
        return redirect(url_for('dc_white_space'))
    if not power_rooms:
        flash('No power room information available today', 'error')
        return redirect(url_for('power_rooms'))
    
    t,h = 0,0
    for key, value in power_rooms.data.items():
        t += float(value.get('temperature'))
        h += float(value.get('humidity'))
    avg_tempPw = t/(len(power_rooms.data))
    avg_humPw = h/(len(power_rooms.data))
    
    today = date.today()
    
    return render_template('admin/ndc/comments.html', 
                           generators=generators, 
                           whitespace = whitespace, 
                           power_rooms = power_rooms,
                           avg_tempPw = avg_tempPw, 
                           avg_humPw = avg_humPw, today = today)
@login_required
def power_rooms():
    return render_template('admin/ndc/power_rooms.html')
@login_required
def generators():
    return render_template('admin/ndc/generators.html')

@login_required
def urlf(urls):
    return render_template(f'admin/pages/{urls}.html')

def make_pdf(data, date, name, email):
    rendered_template = render_template('admin/ndc/generate_pdf-min.html', data = data,date = date.strftime('%c'), name = name, email = email)
    return rendered_template

@login_required
def download_comments(logs):
    log = db.session.query(CommentsModel.data, 
                            CommentsModel.date,
                            Users.name, Users.email)\
                                .outerjoin(Users, Users.id == CommentsModel.user)\
                                .filter(CommentsModel.id == logs).first()
    rendered_template = make_pdf(log.data, log.date, log.name, log.email)
    return make_response(rendered_template)
    

@login_required
def generate_pdf():
    data = request.json
    date = datetime.now()
    rendered_template = make_pdf(data, date, current_user.name, current_user.email)
    new = CommentsModel(
            data = data,
            user = current_user.id,
            
        )
    db.session.add(new)
    db.session.commit()
    EnterLogs("comments_logs", new.id)
    return make_response(rendered_template)
    

@login_required
def containment_data():
    data = request.json
    try:
        new = WhiteSpace(
            data = data,
            user = current_user.id,
            
        )
        db.session.add(new)
        db.session.commit()
        EnterLogs("white_spaces_logs", new.id)
        return make_response(jsonify({'success': True, 'message': 'Data saved successfully', 'data': data}))
    except Exception as e:
        return make_response(jsonify({'success': False, 'message': 'Error saving your data'}))
@login_required
def generators_data():
    data = request.json
    try:
        new = Generators(
            data = data,
            user = current_user.id,
            
        )
        db.session.add(new)
        db.session.commit()
        EnterLogs("generators_logs", new.id)
        return make_response(jsonify({'success': True, 'message': 'Data saved successfully', 'data': data}))
    except Exception as e:
        return make_response(jsonify({'success': False, 'message': 'Error saving your data'}))
    
@login_required
def power_rooms_data():
    data = request.json
    try:
        new = PowerRooms(
            data = data,
            user = current_user.id,
            
        )
        db.session.add(new)
        db.session.commit()
        EnterLogs("power_rooms_logs", new.id)
        return make_response(jsonify({'success': True, 'message': 'Data saved successfully', 'data': data}))
    except Exception as e:
        return make_response(jsonify({'success': False, 'message': 'Error saving your data'}))

@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))