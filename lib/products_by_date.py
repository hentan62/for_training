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

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def select_date(connection):
    selector = "SELECT date_installation from production " \
               "group by date_installation;"
    dates = execute_read_query(connection, selector)
    arr_of_date = []
    for date in dates:
        arr_of_date.append(date[0])
    return arr_of_date


dates = select_date(connection)

def select_date(connection, dates):
    for date in dates:
        print("к числу " + date)
        selector = "SELECT name_item, sum(needed) as result  " \
                   "from production  where date_installation='"+str(date)+ \
                "' group by name_item;"
        prod = execute_read_query(connection, selector)
        for items in prod:
            print("изделий " + str(items[0]) + "в количестве\t" + str(items[1]))
        print("\n")


res = select_date(connection, dates)

