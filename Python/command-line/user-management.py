class UserManagement:
    def __init__(self) -> None:
        self.users = []
        self.is_running = True

    def show_menu(self) -> None:
        print("\n=== User Management ===")
        print("1. Add new user")
        print("2. Show all users")
        print("q. Quit")

    def add_user(self) -> None:
        name = input("Enter name: ")
        age = input("Enter age: ")
        self.users.append({"name": name, "age": age})

    def show_users(self) -> None:
        if not self.users:
            print("\nNo users found.")
            return
        print("\n--- Users ---")
        for idx, user in enumerate(self.users, start=1):
            print(f"{idx}. Name: {user['name']}, Age: {user['age']}")

    def process_choice(self, choice):
        if choice == "1":
            self.add_user()
        elif choice == "2":
            self.show_users()
        elif choice == "q":
            self.is_running = False
        else:
            print("Invalid choice. Please try again.")

    def run(self):
        while self.is_running:
            self.show_menu()
            choice = input("Enter your choice: ").strip().lower()
            self.process_choice(choice)
        print("\nSee you later!")


if __name__ == "__main__":
    user_management = UserManagement()
    user_management.run()
