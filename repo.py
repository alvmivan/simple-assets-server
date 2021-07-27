import sqlite3

db_location = "static/db_test.db"


def create_tables():
    connection = sqlite3.connect(db_location)
    connection.execute("""
                       create table if not exists assets (
                       code text key unique , 
                       data_type text key unique ,
                       content text) 
                       """)
    connection.close()


def save_data(code, content, data_type):
    connection = sqlite3.connect(db_location)

    connection.execute("insert or replace into assets(code,content,data_type) values (?,?,?)",
                       (code, content, data_type))
    connection.commit()
    connection.close()


def retrieve_data(name, data_type):
    connection = sqlite3.connect(db_location)
    pointer = connection.execute("select content from assets where code =? where data_type=?", (name, data_type))
    content = pointer.fetchone()
    connection.close()
    return (content or ("",))[0]


def get_codes_for_type(data_type):
    connection = sqlite3.connect(db_location)
    pointer = connection.execute("select code from assets where data_type=?", (data_type,))
    content = pointer.fetchall()
    connection.close()
    return str({"options": [x[0] for x in content]})


create_tables()
