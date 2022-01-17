from flask import Blueprint, request, session, redirect, render_template
import bcrypt 
from models.user import get_user_by_email

session_controller = Blueprint("session_controller", __name__, template_folder="../templates/session")

@session_controller.route('/login')
def loginpage():
    return render_template('login.html')

@session_controller.route('/sessions/create', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = get_user_by_email(email)
    valid = user and bcrypt.checkpw(password.encode(), user['password'].encode())
    if valid:
        # if they are in the database, we update the session
        session['user_id'] = user['id']
        print(user['id'])
        return redirect('/')
    else:
        #
        return redirect('/login?')
        #
    pass

@session_controller.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect ('/')