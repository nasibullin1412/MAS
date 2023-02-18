from alignment.alignment import needle
from alignment.mapper import map_from_sql_to_token_string


class CheckingSql:

    def __init__(self, assert_threshold, request_id, db):
        self.assert_threshold = assert_threshold
        self.request_id = request_id
        self.db = db

    def check_query(self, checking_query):
        self.db.execute(f"SELECT value FROM sql_assert WHERE request_id = {self.request_id}")
        check_string = map_from_sql_to_token_string(checking_query)
        assert_string = map_from_sql_to_token_string(self.db.fetchall()[0][0])
        needle(check_string, assert_string)
