#!.env/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:50:00 2023
@author: acostav747

python3 -m venv .env
source .env/bin/activate
pip3 install package
pip3 freeze > requirements

export FLASK_APP=app
export FLASK_ENV=development
flask run

"""

import os

from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(SECRET_KEY='dev')
	#app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flask.sqlite'))
	
	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)
	
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass
		
	@app.route('/')
	def home():
		return '<h1>Tempalte</h1>'
		
	from . import registerExample
	app.register_blueprint(registerExample.bp)
		
	return app
