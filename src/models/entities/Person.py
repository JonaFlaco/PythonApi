from utils.DateFormat import DateFormat

class Person():

    def __init__(self, id, name=None, userName=None, birthday=None) -> None:
        self.id = id
        self.name = name
        self.userName = userName
        self.birthday = birthday

    def to_JSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'userName': self.userName,
            'birthday': DateFormat.convert_date(self.birthday)
        }