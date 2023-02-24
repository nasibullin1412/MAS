def map_from_sql_to_token_string(sql_string):
    sql_string = sql_string.lower()
    sql_string = sql_string.replace('select', 'S')
    sql_string = sql_string.replace('where', 'W')
    sql_string = sql_string.replace('from', 'F')
    sql_string = sql_string.replace('insert', 'I')
    sql_string = sql_string.replace('into', 'IN')
    sql_string = sql_string.replace('values', 'V')
    sql_string = sql_string.replace('delete', 'D')
    sql_string = sql_string.replace('update', 'U')
    sql_string = sql_string.replace('set', 'ST')
    sql_string = sql_string.replace('and', 'A')

    sql_string = sql_string.replace('users_info', 'TB')
    sql_string = sql_string.replace('fio', 'DT')
    sql_string = sql_string.replace('document_numb', 'DT')
    sql_string = sql_string.replace('age', 'DT')
    sql_string = sql_string.replace('active', 'DT')

    sql_string = sql_string.replace('false', 'B')
    sql_string = sql_string.replace('true', 'B')

    sql_string = sql_string.replace('=', 'C')
    sql_string = sql_string.replace('>', 'C')
    sql_string = sql_string.replace('<', 'C')

    for elem in sql_string:
        if elem.isdigit():
            sql_string = sql_string.replace(elem, 'N')

    for elem in sql_string:
        if elem.islower():
            sql_string = sql_string.replace(elem, 'L')

    return sql_string