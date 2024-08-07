from utils.DateFormat import DateFormat

class Product():

    def __init__(self, id, name=None, price=None, description=None) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.description = description

    def to_JSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }