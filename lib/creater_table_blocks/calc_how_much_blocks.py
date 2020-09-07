def single_block():
    import re
    import mysql.connector
    from mysql.connector import Error
    import sys

    #функция подключение к БД
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
                                   "test_database", 'mysql_native_password')

    #Отправка запроса
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    #считалка блоков из txt файла
    def sch():
        f = open('entered.txt', 'r')
        a = {}
        for line in f:
            n = line.rstrip()
            if n not in a:
                a[n] = 1
            else:
                a[n] += 1
        f.close()
        return (a)

    nblock = sch()

    h1 = int(input("Введите высоту ряда блоков,мм: "))
    h = int(round(h1 / 100, 0))
    n = 0
    create_blocks = """
    INSERT INTO
    for_block (pos, name_block, length, width, height, quantity, v, v_full)
    VALUES
    """

    for k in sorted(nblock.keys()):
        print(re.findall('\d+', k))
        digit = re.findall('\d+', k)[0]
        try:
            letter = re.findall('\D+', k)[0]
        except IndexError:
            letter = ""
        print("количество блоков ", k, "равно ", nblock[k], "шт.")
        name = "П " + str(digit) + ".4." + str(h) + letter
        length = int(digit) * 100
        width = 400
        v1 = round(length * width * h1 / 10 ** 9, 2)
        vtotal = round(nblock[k] * v1, 2)
        n += 1
        string = ("('" + str(k) + "'," + "'" + str(name) + "'," +
                str(length) + "," + "" + str(width) + "," + str(h1) + "," +
                str(nblock[k]) + "," + "'"
                + str(v1) + "'," + "'" + str(vtotal) + "'),")
        if n == len(nblock.keys()):
            string = ("('" + str(k) + "'," + "'" + str(name) + "'," +
                      str(length) + "," + "" + str(width) + "," + str(h1) + "," +
                      str(nblock[k]) + "," + "'"
                      + str(v1) + "'," + "'" + str(vtotal) + "')")
        create_blocks += string
    create_blocks += ";"
    print(create_blocks)

    execute_query(connection, "DELETE FROM for_block")
    execute_query(connection, create_blocks)


single_block()
