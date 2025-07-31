def display_menu():
    """
    Displays the main menu for the Shopping List Manager application.

    The menu includes the following options:
    1. Add Item - Allows the user to add an item to the shopping list.
    2. Remove Item - Allows the user to remove an item from the shopping list.
    3. View List - Displays the current shopping list.
    4. Exit - Exits the application.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to manage a shopping list.
    This function provides a menu-driven interface for users to manage their shopping list.
    Users can add items, remove items, view the current list, or exit the program.
    Features:
    1. Add an item to the shopping list.
    2. Remove an item from the shopping list.
    3. Display the current shopping list.
    4. Exit the program.
    The function runs in a loop until the user chooses to exit.
    Raises:
        ValueError: If the user enters an invalid choice outside the range 1-4.
    """
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item cannot be empty.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "_main_":
    main()