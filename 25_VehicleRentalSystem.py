class Vehicle:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.available = True  # Vehicle availability status

    def rent(self):
        if self.available:
            self.available = False  # Mark as rented
            return True
        else:
            print(f"{self.model} is not available.")
            return False

    def return_vehicle(self):
        self.available = True  # Mark as available again


class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)  # Add a vehicle to the agency's list

    def show_available(self):
        # Display available vehicles
        available_vehicles = ", ".join(v.model for v in self.vehicles if v.available)
        print(f"Available: {available_vehicles if available_vehicles else 'None'}")


class RentalTransaction:
    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.total = days * vehicle.price  # Calculate total rental cost

    def process_rental(self):
        if self.vehicle.rent():
            print(f"{self.customer} rented {self.vehicle.model} for {self.days} days. Cost: ${self.total}")

    def return_rental(self):
        self.vehicle.return_vehicle()
        print(f"{self.customer} returned {self.vehicle.model}.")


# Create vehicles
car1 = Vehicle("Toyota Corolla", 50)
car2 = Vehicle("Honda Civic", 60)

# Create rental agency and add vehicles
agency = RentalAgency("Quick Rentals")
agency.add_vehicle(car1)
agency.add_vehicle(car2)

# Display available vehicles
agency.show_available()

# Create and process rental transaction
rental = RentalTransaction("Pranav ", car1, 3)
rental.process_rental()

# Show available vehicles after rental
agency.show_available()

# Return vehicle and update availability
rental.return_rental()
agency.show_available()
