from alignment.alignment import needle
from alignment.mapper import map_from_sql_to_token_string


class CheckingSql:

    def __init__(self, assert_threshold, request_id):
        self.enabled = False
        self.assert_threshold = assert_threshold
        self.request_id = request_id
        self.mapper = {
            #  "INSERT INTO users_info( fio, document_numb, age) VALUES ('test', '3465', 324)",
            1: "I IN TB( DT, DT, DT) V ('LLLL', 'NNNN', NNN)",
            #  "DELETE FROM users_info WHERE document_numb=345",
            2: "D F TB W DTCNNN",
            #  Несколько запросов смерженных в один с помощью прогрессивного алгоритма
            # S DT F TB W DT C NN
            # S DT F TB W DT C NN A DT C NN
            # S DT F TB W DT C NN A DTCB
            3: "S DT F TB W DT C NN A DT C   ",
            #  "UPDATE users_info SET document_numb=543 WHERE document_numb=124"
            4: "U TB ST DTCNNN W DTCNNN"
        }

    def check_query(self, checking_query):
        if not self.enabled:
            return True
        check_string = map_from_sql_to_token_string(checking_query)
        assert_string = self.mapper[self.request_id]

        if self.assert_threshold > round(needle(check_string, assert_string)[0]):
            return False

        return True
