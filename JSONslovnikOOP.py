# Import the json module for handling JSON data
import json

# Define a FootballClub class
class FootballClub:
    # Initialize an instance of the class
    def __init__(self, name, city, country):
        # Define the name, city, and country attributes of the class instance
        self.name = name
        self.city = city
        self.country = country

    # Define a method that returns a formatted string with full club information
    def get_full_information(self):
        return f"{self.name}{self.city}{self.country}"

    # Define a method that serializes the instance attributes into a JSON string
    def to_json(self):
        # Use the __dict__ attribute to access the instance attributes
        # Then use the json.dumps() function to convert the dictionary
        return json.dumps(self.__dict__)

# Create a FootballClub instance
obj = FootballClub("Dynamo", "Kyiv", "Ukraine")

# Print the full club information
print(obj.get_full_information())

# Serialize the instance into a JSON string
serialized_obj = obj.to_json()

# Print the serialized JSON string
print(serialized_obj)