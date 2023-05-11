#!/usr/bin/env python3
class CashRegister:
  def __init__(self, discount=0, total=0, price=0):
    self.discount = discount 
    self._total = total
    self.price = price

  def get_total(self):
    return self._total 
  
  def set_total(self, total):
    self._total = total 
  
  total = property(get_total, set_total)

  def add_item(self, item='', price=0, quantity=None):
    if isinstance(quantity, int):
      self._total = self._total + (price * quantity)
    else:
      self._total = self._total + price
  
  def apply_discount(self, discount=None):
    if discount is not None:
      self.discount = discount
    if isinstance(self.discount, float) and self.discount > 0:
      self._total = self._total - (self._total * self.discount)
      self.set_total(self._total)  # call set_total method to update total property
