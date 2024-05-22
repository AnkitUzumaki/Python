import csv

def add_contact():
    """Add a new contact to the CSV file."""
    with open('contacts.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'name': input('Enter name: '),
                         'phone': input('Enter phone: '),
                         'email': input('Enter email: '),
                         'address': input('Enter address: ')})

def view_contacts():
    """View all contacts in the CSV file."""
    with open('contacts.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

def update_contact():
    """Update an existing contact in the CSV file."""
    with open('contacts.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        contacts = list(reader)

    name_to_update = input('Enter name of contact to update: ')
    found = False
    for contact in contacts:
        if contact['name'] == name_to_update:
            contact['name'] = input('Enter new name: ')
            contact['phone'] = input('Enter new phone: ')
            contact['email'] = input('Enter new email: ')
            contact['address'] = input('Enter new address: ')
            found = True

    if found:
        with open('contacts.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'phone', 'email', 'address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)
    else:
        print('Contact not found.')

def delete_contact():
    """Delete a contact from the CSV file."""
    with open('contacts.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        contacts = list(reader)

    name_to_delete = input('Enter name of contact to delete: ')
    new_contacts = []
    for contact in contacts:
        if contact['name'] != name_to_delete:
            new_contacts.append(contact)

    with open('contacts.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_contacts)

def search_contact():
    """Search for a contact by name or other details."""
    with open('contacts.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        contacts = list(reader)

    search_term = input('Enter search term: ')
    found = False
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone'] or \
           search_term in contact['email'] or search_term in contact['address']:
            print(contact)
            found = True

    if not found:
        print('Contact not found.')

def main():
    """Main function to run the Contact Book application."""
    while True:
        print('\nContact Book\n')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Update Contact')
        print('4. Delete Contact')
        print('5. Search Contact')
        print('6. Exit')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            update_contact()
        elif choice == 