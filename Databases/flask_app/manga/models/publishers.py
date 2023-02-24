from manga import connection
from psycopg2 import sql

def add_Publisher(publisher):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Publishers(publisher)
    VALUES (%s)
    """)
    cursor.execute(user_sql, (publisher,))
    connection.commit()
    cursor.close()

def delete_Publisher(publisher):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    DELETE FROM Publishers
    WHERE publisher=%s
    """)
    cursor.execute(user_sql, (publisher,))
    connection.commit()
    cursor.close()

def select_Publishers():
    cursor = connection.cursor()
    sql = """
    SELECT publisher FROM Publishers
    ORDER BY publisher ASC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    publishers = []
    for publisher in results:
        publishers.append(publisher[0])
    return publishers

def connect_Publisher(series, series_year, publisher):
    if series == "" or series_year == "" or publisher == "":
        return
    if check_Publisher_Exists(publisher) == False:
        add_Publisher(publisher)

    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    INSERT INTO Publisher_Of(series, series_year, publisher)
    VALUES (%s, %s, %s)
    """)
    cursor.execute(user_sql, (series, series_year, publisher))
    connection.commit()
    cursor.close()

def check_Publisher_Exists(publisher):
    cursor = connection.cursor()
    user_sql = sql.SQL ("""
    SELECT * FROM Publishers
    WHERE publisher=%s
    """)
    cursor.execute(user_sql, (publisher,))
    result = cursor.fetchone()
    cursor.close()
    return (result != None)