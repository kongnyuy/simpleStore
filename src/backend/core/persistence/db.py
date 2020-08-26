from peewee import SqliteDatabase
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
import sys

from backend.config import db_name
#from backend.config import *


class Database:
    _db = SqliteDatabase(db_name)

    @staticmethod
    def get_db_handle():
        return Database._db

    @staticmethod
    def connect():
        try:
            Database._db.connect()
        except Exception as ex:
            print(f"exceptio: {ex}", file=sys.stderr)

        return Database._db

    @staticmethod
    def get_db():
        #if 'db' not in g:
        #    g.db = sqlite3.connect(current_app.config['DATABASE'],detect_types=sqlite3.PARSE_DECLTYPES)
        #g.db.row_factory = sqlite3.Row

        #return g.db
        if 'db' not in g:
            g.db = Database.get_db_handle()
        return g.db

    @staticmethod
    def close_db(e=None):
        db = g.pop('db', None) #TODO ORM db now returned, CAUTION!

        if db is not None:
            db.close()

    @staticmethod
    def init_db():
        db = get_db()

        #TODO current the resource location
        #with current_app.open_resource('store.db.schema.sql') as f:
        with open(current_app.config['SCHEMA_PATH'], 'r') as f:
            db.executescript(f.read().decode('utf8'))

    @staticmethod
    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        """[flask cli interface command]Clear the existing data and create new tables."""
        init_db()
        click.echo('Initialized the database.')

    @staticmethod
    def init_app_db(app):
        app.teardown_appcontext(Database.close_db)
        app.cli.add_command(Database.init_db_command)
