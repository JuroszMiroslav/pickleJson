import pickle


class UserManager:
    def __init__(self, file_name='user_data.pickle'):
        self.file_name = file_name
        self.user_data = {}
        self.load_data()

    def add_user(self, username, password):
        """Add a new user with a username and password."""
        if username in self.user_data:
            print("User already exists.")
        else:
            self.user_data[username] = password
            print(f"User {username} added successfully.")

    def delete_user(self, username):
        """Delete a user by username."""
        if username in self.user_data:
            del self.user_data[username]
            print(f"User {username} deleted successfully.")
        else:
            print("User not found.")

    def find_user(self, username):
        """Find a user's password by username."""
        if username in self.user_data:
            print(f"Password for {username} is {self.user_data[username]}")
        else:
            print("User not found.")

    def edit_user(self, username, new_password):
        """Edit an existing user's password."""
        if username in self.user_data:
            self.user_data[username] = new_password
            print(f"Password for {username} updated successfully.")
        else:
            print("User not found.")

    def save_data(self):
        """Save the user data to a file using pickle."""
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.user_data, file)
            print("Data saved successfully.")

    def load_data(self):
        """Load the user data from a file using pickle."""
        try:
            with open(self.file_name, 'rb') as file:
                self.user_data = pickle.load(file)
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found. Starting with an empty database.")


def main():
    manager = UserManager()

    while True:
        print("\nAvailable actions: add, delete, find, edit, save, exit")
        action = input("Enter action: ").strip().lower()

        if action == "add":
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.add_user(username, password)
        elif action == "delete":
            username = input("Enter username to delete: ")
            manager.delete_user(username)
        elif action == "find":
            username = input("Enter username to find: ")
            manager.find_user(username)
        elif action == "edit":
            username = input("Enter username to edit: ")
            new_password = input("Enter new password: ")
            manager.edit_user(username, new_password)
        elif action == "save":
            manager.save_data()
        elif action == "exit":
            manager.save_data()  # Save before exiting
            print("Exiting program.")
            break
        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    main()
