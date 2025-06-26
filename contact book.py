# Contact Book using dictionary

contact_book = {}

def add_contact():
    name = input("Enter Name: ").strip()
    if name in contact_book:
        print("Contact already exists.")
    else:
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email (optional): ").strip()
        contact_book[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"  Phone: {details['Phone']}")
            print(f"  Email: {details['Email']}\n")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contact_book:
        print(f"Name: {name}")
        print(f"  Phone: {contact_book[name]['Phone']}")
        print(f"  Email: {contact_book[name]['Email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contact_book:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email (optional): ").strip()
        contact_book[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
