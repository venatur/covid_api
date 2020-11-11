import pandas as pd
import psycopg2
import pandas.io.sql as psql
import sys


def postgresql_to_dataframe(conn, select_query, headers):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor('testCursor')
    cursor.itersize = 100000
    try:
        cursor.execute(select_query)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()

    conn.commit()
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=headers)
    df = df.astype(object)
    return df


def psql_pandas(conn, select_query):
    dfl = []
    chunk_size = 10000
    offset = 0
    while True:
        query = "select * from estados limit %d offset %d" % (chunk_size, offset)
        dfl.append(psql.read_sql(query, conn))
        offset += chunk_size

    return dfl


def get_headers(conn, table):
    cursor = conn.cursor()
    col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
    col_names_str += "table_name = '{}';".format(table)
    cursor.execute(col_names_str)
    col_names = [x[0] for x in cursor.fetchall()]
    conn.commit()
    return col_names
