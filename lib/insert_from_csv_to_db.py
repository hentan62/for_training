import mysql.connector
from mysql.connector import Error
import csv

def find_csv():
    list_one = []
    FILENAME = "July2020.csv"
    with open(FILENAME, "r", newline="",encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            list_one.append(row)
    return list_one

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


create_users = """
INSERT INTO
production (date_installation, object, section, number_floor, name_item, needed)
VALUES
"""
for value in find_csv():
    string = '("'+ str(value[1]) + '", "' + str(value[3]) + '", "' + str(value[4]) + '", '+\
    str(value[5]) + ', "' + str(value[8]) + '", ' + str(value[11]) + '),'
    if value == find_csv()[-1]:
        string = '("' + str(value[1]) + '", "' + str(value[3]) + '", "' + str(value[4]) + '", ' + \
                 str(value[5]) + ', "' + str(value[8]) + '", ' + str(value[11]) + ')'
    create_users += string
create_users+=";"
print(create_users)
execute_query(connection, create_users)
