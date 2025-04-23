
class Product:
    def __init__(self, name, price, stock):  
        self.name = name  # Added assignment to self.name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity  # Reduce stock by quantity
            return True
        else:
            print(f"Insufficient stock for {self.name}")
            return False

class Customer:
    def __init__(self, name):  
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.update_stock(quantity):
            self.cart.append((product, quantity))
            print(f"{quantity} x {product.name} added to {self.name}'s cart.")

    def checkout(self):
        total_cost = sum(product.price * quantity for product, quantity in self.cart)  
        print(f"{self.name}'s total bill: ${total_cost:.2f}")
        self.cart.clear()  # Clear the cart after checkout
        print("Order processed successfully!")


# Example usage:
product1 = Product("Laptop", 1000, 5)
product2 = Product("Headphones", 200, 10)
product3 = Product("Mouse", 700, 10)

customer1 = Customer("Dhawal")
customer1.add_to_cart(product1, 1)
customer1.add_to_cart(product2, 2)
customer1.add_to_cart(product3, 1)
customer1.checkout()