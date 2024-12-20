class MainBase:
    def __init__(self, id):
        self.id = id


class TimeStamp:
    def __init__(self, created_at, updated_at):
        self.created_at = created_at
        self.updated_at = updated_at


class Users(MainBase, TimeStamp):
    def __init__(self, id, created_at, updated_at, chat_id, first_name, last_name, role):
        MainBase.__init__(self, id)
        TimeStamp.__init__(self, created_at, updated_at)
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role


class Books(MainBase, TimeStamp):
    def __init__(self, id, created_at, updated_at, photo_url, book_part):
        MainBase.__init__(self, id)
        TimeStamp.__init__(self, created_at, updated_at)
        self.photo_url = photo_url
        self.book_part = book_part



class Units(MainBase, TimeStamp):
    def __init__(self, id, created_at, updated_at, unit_num, book_id):
        MainBase.__init__(self, id)
        TimeStamp.__init__(self, created_at, updated_at)
        self.unit_num = unit_num
        self.book_id = book_id


class Tests(MainBase):
    def __init__(self, id, part_test_id, question, a, b, c, d, right):
        super().__init__(id)
        self.part_test_id = part_test_id
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.right = right


class PartTests(MainBase, TimeStamp):
    def __init__(self, id, created_at, updated_at, part_name):
        MainBase.__init__(self, id)
        TimeStamp.__init__(self, created_at, updated_at)
        self.part_name = part_name


class Vocabulary(MainBase):
    def __init__(self, id, unit_id, eng, uzb):
        super().__init__(id)
        self.unit_id = unit_id
        self.eng = eng
        self.uzb = uzb

