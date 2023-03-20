import psycopg2
import datetime

DBNAME = 'postgres'
USER = 'postgres'
PASSWORD = '95233574'
HOST = 'localhost'

ERROR = 'ERROR'
WARN = 'WARNING'
INFO = 'INFO'


def create_logs_table():
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
            CREATE TABLE IF NOT EXISTS logs(
                id serial PRIMARY KEY,
                log_date TIMESTAMP,
                log_level CHARACTER VARYING(20) NOT NULL,
                log_info TEXT
                )''')


def insert_logs(log_level, log_info):
    with psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST) as conn:
        with conn.cursor() as curs:
            curs.execute('''
            INSERT INTO logs (log_date, log_level, log_info) VALUES (%s, %s, %s)
            ''',
                         (datetime.datetime.now(), log_level, log_info)
                         )


def error(log_info):
    insert_logs(log_level=ERROR, log_info=log_info)


def warn(log_info):
    insert_logs(log_level=WARN, log_info=log_info)


def info(log_info):
    insert_logs(log_level=INFO, log_info=log_info)
