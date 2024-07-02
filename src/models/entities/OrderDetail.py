class OrderDetail():

    def __init__(self, id, amount=None, unitPrice=None, personId=None, productId=None) -> None:
        self.id = id
        self.amount = amount
        self.unitPrice = unitPrice
        self.personId = personId
        self.productId = productId

    def to_JSON(self):
        return{
            'id': self.id,
            'amount': self.amount,
            'unitPrice': self.unitPrice,
            'personId': self.personId,
            'productId': self.productId
        }