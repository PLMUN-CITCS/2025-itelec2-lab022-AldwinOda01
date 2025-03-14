def display_menu() -> None:
    
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user() -> None:
    
    print("Hello! Welcome!")


def get_integer_input(prompt: str) -> int:
    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def check_even_odd(number: int) -> str:
 
    return f"{number} is an {'Even' if number % 2 == 0 else 'Odd'} number."


def handle_menu_choice(choice: int) -> bool:
   
    if choice == 1:
        greet_user()
    elif choice == 2:
        num = get_integer_input("Enter an integer: ")
        print(check_even_odd(num))
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
    return False  


while True:
    display_menu()
    user_choice = get_integer_input("Enter your choice (1-3): ")
    if handle_menu_choice(user_choice):
        break 
