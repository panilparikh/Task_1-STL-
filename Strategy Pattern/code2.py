from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount}rs using Credit Card")
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount}rs using PayPal")
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
credit_card_payment.pay(50000)
paypal_payment.pay(3000)