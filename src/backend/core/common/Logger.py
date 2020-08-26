import logging

#Loggers = {db_logger: build_logger(name="db-logger", logType=logging.INFO)}


def build_logger(name: str = "app-logger", logType=logging.DEBUG):
    l = logging.getLogger('db-peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logType)


class Loggers:
    _db_logger = None

    @staticmethod
    def dbLogger():
        if Loggers._db_logger == None:
            Loggers._db_logger = build_logger(name="db-logger",
                                              logType=logging.INFO)
        return Loggers._db_logger

