def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            x= input("Enter the item to add: ")
            shopping_list.append(x)
            pass
        elif choice == '2':
            x= input("Enter the item to remove: ")
            if x in shopping_list:
                shopping_list.remove(x)
            else:
                print("The item deosn't exist.")
            pass
        elif choice == '3':
            for x in shopping_list:
                print(x)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()