# Import json module for serialization/deserialization
import json

# Define the Address class
class Address:
    # Initialize an Address instance
    def __init__(self, city, street, apartment):
        self.city = city
        self.street = street
        self.apartment = apartment

    # Define string representation of Address instance
    def __str__(self):
        return f"{self.city}{self.street}{self.apartment}"

    # Convert the Address object to a dictionary
    def to_dict(self):
        return {
            "city": self.city,
            "street": self.street,
            "apartment": self.apartment
        }

# Define the Human class
class Human:
    # Initialize a Human instance
    def __init__(self, name, last_name, address):
        self.name = name
        self.last_name = last_name
        self.address = address

    # Define string representation of Human instance
    def __str__(self):
        return f"{self.name}{self.last_name}{self.address}"

    # Convert the Human object to a dictionary
    def to_dict(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "address": self.address.to_dict()
        }

# Create a Human instance
first_obj = Human("Marc", "Dylan", Address("New York", "Mulberry Street 162", "33b"))

# Serialize the Human instance to a JSON string
serialized = json.dumps(first_obj.to_dict())
print(f"Serialized object:\n\n{serialized}\n\n")

# Deserialize the JSON string back into a dictionary
deserialized = json.loads(serialized)

# Create a new Human instance from the deserialized dictionary
second_obj = Human(deserialized["name"], deserialized["last_name"], Address(**deserialized["address"]))

# Print the deserialized Human instance
print(f"Deserialized object:\n\n{second_obj}")