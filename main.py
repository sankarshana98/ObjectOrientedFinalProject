from user_login import Invoker, LoginCommand, LogoutCommand
from authentication import AuthSingleton

def main():
    auth_instance = AuthSingleton()
    invoker = Invoker()

    while True:
        print("\n1. Create User Account")
        print("2. Log In")
        print("3. Log Out")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth_instance.create_user(username, password)

        elif choice == "2":
            if auth_instance.get_logged_in_user():
                print("Already logged in.")
            else:
                username = input("Enter username: ")
                password = input("Enter password: ")
                login_command = LoginCommand(auth_instance, username, password)
                invoker.set_command(login_command)
                invoker.execute_command()

                # Display welcome message and log out option
                if auth_instance.get_logged_in_user():
                    print(f"Welcome, {username}!")
                    logout_choice = input("Do you want to log out? (y/n): ")
                    if logout_choice.lower() == 'y':
                        logout_command = LogoutCommand(auth_instance)
                        invoker.set_command(logout_command)
                        invoker.execute_command()

        elif choice == "3":
            logout_command = LogoutCommand(auth_instance)
            invoker.set_command(logout_command)
            invoker.execute_command()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
