import mysql.connector
from mysql.connector import Error

#введите название элементов, которые надо найти в таблице,
#а также номер этажа для которого осуществляется выборка
name_first_element = "РОР"
name_second_element = "РДР"
number_floor = "2"

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

connection = create_connection("localhost", "admin", "password",
                               "for_pik",'mysql_native_password')

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def selector(connection, name_one, name_two, number_floor):
    selector = f"select name_item, count(needed) from production where number_floor={number_floor} " \
               f"and (select name_item like '{name_one}%' " \
               f"or name_item like '{name_two}%') " \
               "group by name_item;"
    users = execute_read_query(connection, selector)
    for user in users:
        print(user[0], user[1])


selector(connection, name_first_element, name_second_element, number_floor)
