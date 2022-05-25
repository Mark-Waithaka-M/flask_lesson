from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, current_user, login_required
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['name']
        password = request.form['psw']
        
        User = User.query.filter_by(name = user_name).first()
        
        if User:
            if check_password_hash(User.password, password) == True:
                login_user(User)
                return redirect(url_for('views.index'))
            
            else:
                flash('Wrong password', category='error')
                
        else:
            flash('User could not be found', category='error')
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signUp', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        userName = request.form.get ('name')
        email = request.form.get ('email')
        password = request.form.get(psw)
        confirm_password = request.form.get (psw-repeat)
        
        if len (email)< 10:
            flash ("email must be greater than 9 characters", category = 'error')
            
        elif len(userName) < 2:
            flash('User name must be greater than one character', category = 'error')
            
        elif password != confirm_password:
            flash ('password don\'t match', category = 'error')
            
        elif len(password) <= 7:
            flash('password must be more than 7 charaters')
            
        else:
            try:
                #add the User to the db
                new_user = User(email=email, name=userName, password= generate_password_hash(password))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('you have successfully created an account', category = 'success')
                return redirect(url_for('views.home'))
            except sqlalchemy.exc.IntegrityError:
                return render_template('signUp.html', message='email already exists in the database!')
            
    return render_template('signUp.html')