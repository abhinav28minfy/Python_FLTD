def add_contacts(contacts,name,phone, email, address):
    contacts[name]={"phone": phone, "email": email, "address": address}
    return contacts

contacts={}
print(add_contacts(contacts, "Alice", "123-456-7890", "alice@example.com", "America"))
print(add_contacts(contacts, "Adam", "123-456-7890", "adamexample.com", "America"))