# Name: Ahmed Ashraf
class Card:
 def __init__(self,value,suit):
     self.value = value
     self.suit = suit
 def __repr__(self):
     return f"Card(value={self.value},suit={self.suit})"
 def __str__(self):
     return f"{self.value} of {self.suit}"
 def __eg__(self,other):
    return f"{self.value == other.value}  {self.suit == other.suit}"