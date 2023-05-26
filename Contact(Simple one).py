'''
Contact Book: Build a simple contact book program that allows users to store and manage their contacts.
Allow users to add new contacts, search for contacts by name, display all contacts, and remove contacts.
'''

contact = {}

while True:


    name = input("Enter the contact name : ")
    number = input("Enter the contact number : ")
    add_contact = input("Do you want to add to the contact : YES/NO ").upper()

    if add_contact == 'YES':
        contact[name] = number
    elif add_contact == 'NO':
        pass
    search_contact = input("Do you want to search the contact : YES/NO").upper()
    if search_contact == 'YES':
        tosearch = input("Enter the name you want to search : ")
        if tosearch in contact:
            print(f" {tosearch} is in your contact list  ")
        else:
            print(f"Sorry {tosearch} is not inside your contact list")
    elif search_contact =='NO':
        pass
    remove_contact = input("Do you want to remove a contact : YES/NO").upper()
    if remove_contact == 'YES':
        toremove = input("Enter the name of the contact to remove")
        if toremove in contact:
            dict.pop(toremove)
            print(f"{toremove} has been removed from your contact list ")
        else:
            print(f"{toremove} is not in the contact")
    elif remove_contact =='NO':
        pass
    close_contact = input("Do you want to close the contact : Yes/NO").upper()
    if close_contact == 'YES':
        break
    else:
        pass
print(contact)






