from __init__ import *
from forms.forms import *
from werkzeug.security import generate_password_hash, check_password_hash

def index():
    return make_response(render_template('index.html'))

def login():
    form = login_form()
    if form.validate_on_submit():
        try:
            user = Users.query.filter_by(email=form.email.data).first()
            if user:
                if check_password_hash(user.pwd, form.pwd.data):
                    login_user(user)
                    if request.args.get('next'):
                        return redirect(request.args.get('next'))
                    else:
                        return redirect(url_for('dashboard'))
                else:
                    flash("Invalid Username or password!", "danger")
            else:
                flash("User does not exist!", "danger")
        except Exception as e:
            flash(e, "danger")
    return make_response(render_template('auth.html', form = form))
def register():
    form = register_form()
    if form.validate_on_submit():
        try:
            email = form.email.data
            pwd = form.pwd.data
            username = form.username.data
            
            newuser = Users(
                username=username,
                email=email,
                pwd=generate_password_hash(pwd),
            )
    
            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))

        except Exception as e:
            flash(e, "danger")
    return make_response(render_template('auth.html', form = form))

@login_required
def dashboard():
    print(current_user.email)
    return make_response(render_template('admin/ndc/index.html'))


@login_required
def settings():
    return render_template('admin/ndc/settings.html')
@login_required
def logs():
    return render_template('admin/ndc/logs.html')

@login_required
def dc_white_space():
    return render_template('admin/ndc/dc_white_space.html')
@login_required
def comments():
    return render_template('admin/ndc/comments.html')
@login_required
def power_rooms():
    return render_template('admin/ndc/power_rooms.html')
@login_required
def generators():
    return render_template('admin/ndc/generators.html')

@login_required
def urlf(urls):
    return render_template(f'admin/pages/{urls}.html')

@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))