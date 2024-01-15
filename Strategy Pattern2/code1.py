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