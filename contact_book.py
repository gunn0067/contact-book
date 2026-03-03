# ============================================
# Task 3: Contact Book (CLI)
# Built by: Gunn Fulwani
# ============================================

contacts = []


def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Contact '{name}' already exists.")
            return

    contacts.append({'name': name, 'phone': phone, 'email': email})
    print(f"Contact '{name}' added successfully!")


def view_contacts():
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(
            f"{i}. Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")


def search_contact():
    print("\n--- Search Contact ---")
    name = input("Enter name to search: ").strip()
    results = [c for c in contacts if name.lower() in c['name'].lower()]
    if not results:
        print(f"No contact found with name '{name}'.")
    else:
        for contact in results:
            print(
                f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")


def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter name to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully!")
            return
    print(f"No contact found with name '{name}'.")


def contact_book():
    print("=" * 40)
    print("           CONTACT BOOK")
    print("=" * 40)

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


contact_book()
1
