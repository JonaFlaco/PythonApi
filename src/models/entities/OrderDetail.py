class OrderDetail():

    def __init__(self, id, amount=None, unitPrice=None, personId=None) -> None:
        self.id = id
        self.amount = amount
        self.unitPrice = unitPrice
        self.personId = personId # LLAVE FORANEA

    def to_JSON(self):
        return{
            'id': self.id,
            'amount': self.amount,
            'unitPrice': self.unitPrice,
            'personId': self.personId # LLAVE FORANEA
        }