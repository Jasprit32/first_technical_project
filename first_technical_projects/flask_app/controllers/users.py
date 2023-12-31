from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.employee import Employee
from flask_app.models.location import Location
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/registration')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/registration')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/registration')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    location = Location.get_all()


    return render_template("dashboard.html",user=User.get_by_id(data),all_location=Location.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')