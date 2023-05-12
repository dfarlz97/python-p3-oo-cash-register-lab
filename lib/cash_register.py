class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.last_transaction = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    for _ in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if (self.discount > 0):
      discount_as_percent = (100 - float(self.discount)) / 100
      self.total = int(self.total * discount_as_percent)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    self.total -= self.last_transaction