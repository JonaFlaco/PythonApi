class OrderDetail():

    def __init__(self, id, amount=None, unitPrice=None) -> None:
        self.id = id
        self.amount = amount
        self.unitPrice = unitPrice

    def to_JSON(self):
        return{
            'id': self.id,
            'amount': self.amount,
            'unitPrice': self.unitPrice,
        }