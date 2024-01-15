class Coffee:
    def cost(self):
        return 90
class Milk:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost() + 100
class Sugar:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self):
        return self._coffee.cost() + 10 
regular_coffee = Coffee()
coffee_with_milk = Milk(regular_coffee)
coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
print(f"Cost of regular coffee: {regular_coffee.cost()}rs")
print(f"Cost of coffee with milk: {coffee_with_milk.cost()}rs")
print(f"Cost of coffee with milk and sugar: {coffee_with_milk_and_sugar.cost()}rs")