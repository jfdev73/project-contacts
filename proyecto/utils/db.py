import os
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="dbcontacts",
        user="postgres",
        password="1234",
        port="5433"

    )

    return conn
