import psycopg2
import pandas as pd
import sys
# Connection parameters, yours will be different


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    params_dic = {
        "host": "localhost",
        "database": "covid",
        "user": "postgres",
        "password": "12345"
        }
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn