import pickle

# Dictionary to store usernames (keys) and passwords (values)
user_data = {}


def add_user(username, password):
    """Add a new user with a username and password."""
    if username in user_data:
        print("User already exists.")
    else:
        user_data[username] = password
        print(f"User {username} added successfully.")


def delete_user(username):
    """Delete a user by username."""
    if username in user_data:
        del user_data[username]
        print(f"User {username} deleted successfully.")
    else:
        print("User not found.")


def find_user(username):
    """Find a user's password by username."""
    if username in user_data:
        print(f"Password for {username} is {user_data[username]}")
    else:
        print("User not found.")


def edit_user(username, new_password):
    """Edit an existing user's password."""
    if username in user_data:
        user_data[username] = new_password
        print(f"Password for {username} updated successfully.")
    else:
        print("User not found.")


def save_data(file_name='user_data.pickle'):
    """Save the user data to a file using pickle."""
    with open(file_name, 'wb') as file:
        pickle.dump(user_data, file)
        print("Data saved successfully.")


def load_data(file_name='user_data.pickle'):
    """Load the user data from a file using pickle."""
    global user_data
    try:
        with open(file_name, 'rb') as file:
            user_data = pickle.load(file)
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found. Starting with an empty database.")


def main():
    """Main function to interact with the user data system."""
    load_data()  # Load data at the start (if available)

    while True:
        print("\nAvailable actions: add, delete, find, edit, save, exit")
        action = input("Enter action: ").strip().lower()

        if action == "add":
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif action == "delete":
            username = input("Enter username to delete: ")
            delete_user(username)
        elif action == "find":
            username = input("Enter username to find: ")
            find_user(username)
        elif action == "edit":
            username = input("Enter username to edit: ")
            new_password = input("Enter new password: ")
            edit_user(username, new_password)
        elif action == "save":
            save_data()
        elif action == "exit":
            save_data()  # Save before exiting
            print("Exiting program.")
            break
        else:
            print("Invalid action. Please try again.")


if __name__ == "__main__":
    main()
