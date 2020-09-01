import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name, auth_plugin):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            auth_plugin=auth_plugin
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "admin_here", "password_here",
                               "for_pik",'mysql_native_password')


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_production_table = """
CREATE TABLE IF NOT EXISTS production (
  id INT NOT NULL AUTO_INCREMENT,
  date_installation VARCHAR(15) NOT NULL,
  object VARCHAR(100) NOT NULL,
  section VARCHAR(20),
  number_floor INT,
  name_item VARCHAR(30) NOT NULL,
  needed INT NOT NULL,
  PRIMARY KEY(id)
);
"""
execute_query(connection, create_production_table)
