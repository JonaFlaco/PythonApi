from utils.DateFormat import DateFormat

class Request():

    def __init__(self, id, state=None, date=None) -> None:
        self.id = id
        self.state = state
        self.date = date

    def to_JSON(self):
        return{
            'id': self.id,
            'state': self.state,
            'date': DateFormat.convert_date(self.date)
        }