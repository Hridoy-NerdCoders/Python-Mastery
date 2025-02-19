class CreditCard:
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

class PayPal:
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

class Bitcoin:
    def pay(self, amount):
        print(f"Paid ${amount} using Bitcoin")

def process_payment(payment_method, amount):
    payment_method.pay(amount)  # We don’t care which class, just that it has a pay() method

cc = CreditCard()
pp = PayPal()
btc = Bitcoin()

process_payment(cc, 100)   # Output: Paid $100 using Credit Card
process_payment(pp, 50)    # Output: Paid $50 using PayPal
process_payment(btc, 200)  # Output: Paid $200 using Bitcoin

