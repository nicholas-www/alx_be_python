def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    

shopping_list = []

while True:
    display_menu()
    
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input('Input item: ')
        shopping_list.append(item)
    elif choice == '2':
        item = input('Input item: ')
        shopping_list.remove(item)
    elif choice == '3':
        print(shopping_list)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

