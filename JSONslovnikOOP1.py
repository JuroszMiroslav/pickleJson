import json
import os

# Class to handle file operations
class FileOperations:
    # Static method to create a file path
    @staticmethod
    def create_path(file_name):
        # Get the directory of the script being run
        script_dir = os.path.dirname(os.path.realpath(__file__))
        # Join the script directory with the filename
        return os.path.join(script_dir, file_name)

    # Static method to save data to a file
    @staticmethod
    def save(file_name, data):
        # Create a full file path
        path = FileOperations.create_path(file_name)
        # Open the file and write data to it
        with open(path, "w") as file:
            file.write(data)

    # Static method to load data from a file
    @staticmethod
    def load(file_name):
        # Create a full file path
        path = FileOperations.create_path(file_name)
        # Open the file and read data from it
        with open(path, "r") as file:
            data = file.read()
        # Return the data read from the file
        return data

# Class to define a football club
class FootballClub:
    # Constructor to initialize a football club with name, city, and country
    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country

    # Method to get full information about the club
    def get_full_information(self):
        return f"{self.name} {self.city} {self.country}"

    # Method to convert the object to JSON
    def to_json(self):
        # Convert the object's dictionary to JSON
        return json.dumps(self.__dict__)

    # Static method to create a football club object from JSON
    @staticmethod
    def create_from_json(json_obj):
        # Convert JSON to dictionary
        dict = json.loads(json_obj)
        # Create a new football club object using the dictionary
        return FootballClub(dict["name"], dict["city"], dict["country"])

# Create a new football club object
obj = FootballClub("Dynamo", "Kyiv", "Ukraine")
# Print the full information of the club
print(obj.get_full_information())

# Define the filename for saving
file_name = "person.json"
# Save the football club object to file in JSON format
FileOperations.save(file_name, obj.to_json())

# Load the JSON data from file
json_data = FileOperations.load(file_name)

# Create a new football club object from the loaded JSON data
obj2 = FootballClub.create_from_json(json_data)

# Print the full information of the newly created club
print(obj2.get_full_information())