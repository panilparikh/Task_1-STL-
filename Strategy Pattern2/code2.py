from abc import ABC, abstractmethod
class BillingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, amount):
        pass
class NormalBilling(BillingStrategy):
    def calculate_price(self, amount):
        return amount
class DiscountBilling(BillingStrategy):
    def calculate_price(self, amount):
        return amount * 0.9
class BillingSystem:
    def __init__(self, billing_strategy):
        self._billing_strategy = billing_strategy

    def set_billing_strategy(self, billing_strategy):
        self._billing_strategy = billing_strategy

    def calculate_total(self, amount):
        return self._billing_strategy.calculate_price(amount)
normal_billing_strategy = NormalBilling()
discount_billing_strategy = DiscountBilling()
billing_system = BillingSystem(normal_billing_strategy)
amount_to_pay = 100000
total_with_normal_billing = billing_system.calculate_total(amount_to_pay)
print(f"Total with Normal Billing: {total_with_normal_billing}Rs")
billing_system.set_billing_strategy(discount_billing_strategy)
total_with_discount_billing = billing_system.calculate_total(amount_to_pay)
print(f"Total with Discount Billing: {total_with_discount_billing}Rs")