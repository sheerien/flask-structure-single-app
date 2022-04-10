from flask import Flask, render_template
from dotenv import load_dotenv
import os
import config


app = Flask(__name__)

APP_ROOT=os.path.abspath(os.path.dirname(os.path.dirname(__name__)))
dotenv_path = os.path.join(APP_ROOT, ".env")

if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path) 

app.config.from_object('config.settings.' + os.environ.get('FLASK_ENV'))

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')

@app.errorhandler(500)
def not_found(error):
    return render_template('errors/500.html')

from app.views.home import home_blueprint

app.register_blueprint(home_blueprint, url_prefix="")