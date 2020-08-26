import os,sys
import json
from flask import Flask, render_template
from .config import *
from backend.core.persistence.db import Database


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'store.sqlite'),
        DATABASE=db_name(),
        SCHEMA_PATH = schema_path()
    )

    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    #initialize the database
    Database.init_app_db(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as err:
        print(f"OS error> {err}", file=sys.stderr)
        print("Flask requires instance folder")
        #sys.exit(1)    

    return app



