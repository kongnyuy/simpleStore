from peewee import SqliteDatabase
from backend.config import db_name
import sys
import logging

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
            print
