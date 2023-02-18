from flask import Flask, request
import sqlite3

from alignment.check_sql import CheckingSql

conn = sqlite3.connect('users.db', check_same_thread=False)
user_db = conn.cursor()
app = Flask('victim-server')


@app.route('/User/create', methods=['POST'])
def create_user():
    """
    curl -X POST 'http://0.0.0.0:8080/User/create?fio=Testerov%20Tester%20Testerovich&document_numb=1%20564237&age=27'
    :return:
    """
    fio = request.args['fio']
    document_numb = request.args['document_numb']
    age = request.args['age']
    query = f"INSERT INTO users_info( fio, document_numb, age) VALUES ('{fio}', '{document_numb}', {age})"
    user_db.execute(query)
    print(
        f'''
            User success created!
            EXECUTED QUERY: {query}
        '''
    )
    return ''


@app.route('/User/delete/<document_numb>', methods=['GET'])
def delete_user(document_numb: int):
    """
    curl 'http://0.0.0.0:8080/User/delete/1'
    :param document_numb:
    :return:
    """
    query = f"DELETE FROM users_info WHERE document_numb={document_numb}"
    user_db.execute(query)
    print(f'Delete user with document_number={document_numb}')
    print(
        f'''
            User success deleted!
            EXECUTED QUERY: {query}
        '''
    )
    return ''


@app.route('/User/users', methods=['POST'])
def get_user_by_age():
    """
    curl -X POST 'http://0.0.0.0:8080/User/users?start_age=21'
    curl -X POST 'http://0.0.0.0:8080/User/users?end_age=22'
    curl -X POST 'http://0.0.0.0:8080/User/users?start_age=21&end_age=22'
    :return:
    """
    start_age = request.args.get('start_age')
    end_age = request.args.get('end_age')
    if start_age is not None or end_age is not None:
        start_age_query_part = '' if start_age is None else f'age > {start_age}'
        end_age_query_part = '' if end_age is None else f'age < {end_age}'
        and_phrase = ' and ' if (start_age_query_part != '' and end_age_query_part != '') else ''
        query = f"SELECT fio FROM users_info WHERE {start_age_query_part}{and_phrase}{end_age_query_part}"
        check_sql = CheckingSql(assert_threshold=5, request_id=3, db=user_db)
        check_sql.check_query(query)
        user_db.execute(query)
        users = user_db.fetchall()
        print(f'Get user by age')
        print(
            f'''
                    Users: {users}
                    EXECUTED QUERY: {query}
            '''
        )
    return ''


@app.route('/User/update-document', methods=['POST'])
def update_user_document():
    """
    curl -X POST 'http://0.0.0.0:8080/User/update-document?old_document=123&new_document=321'
    :return:
    """
    old_document_numb = request.args['old_document']
    new_document_numb = request.args['new_document']
    query = f"UPDATE users_info SET document_numb={new_document_numb} WHERE document_numb={old_document_numb}"
    user_db.execute(query)
    print(f'Delete user with userId={id}')
    print(
        f'''
                Document success updated!
                EXECUTED QUERY: {query}
            '''
    )
    return ''
