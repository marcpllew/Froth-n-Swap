from flask import Flask, redirect
import os
from flask.templating import render_template
import psycopg2
from controllers.beer_controller import beer_controller
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller

DB_URL = os.environ.get("DATABASE_URL", "dbname=project2")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
# original code 
# app.config['SECRET_KEY'] = SECRET_KEY
app.config['SECRET_KEY'] = os.environ.get("DATABASE_URL")
# postgresql://project_2_database_user:vwgeQjZGDnWpkzvij7x5FjuzaqhRNfXh@dpg-cgmc46bhp8ua8vpbk0mg-a.singapore-postgres.render.com/project_2_database

@app.route('/')
@app.route('/beerlist')
def beerlist():
    # return render_template('/base.html')
    return redirect('/beers')


# Register Controllers
app.register_blueprint(beer_controller)
app.register_blueprint(session_controller)
app.register_blueprint(user_controller)

if __name__ == "__main__":
    app.run(debug=True)

