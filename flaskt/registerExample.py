import functools

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
'''
from flaskt.database import get_mydb -> (function get database)
'''
bp = Blueprint('registerExample', __name__, url_prefix='/registerExample')

@bp.route('/test', methods=('GET','POST'))
def registerTest():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		error = None
		
		if not username:
			error = 'Username is required'
		elif not password:
			error = 'Password is required'
		
		if error is None:
			try:
				#save to db
				print('db')
			except:
				error: f"User {username} is already registered."
			else:
				return redirect(url_for("registerExample.login"))
		
		flash(error)
		
	return render_template('test.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        #validate user in db

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('login.html')
    
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = 1000
    
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('registerExample.login'))

        return view(**kwargs)

    return wrapped_view
