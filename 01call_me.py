def get_contact(contacts, name):
    return contacts[name]
contacts = {
  "Carly": "333-3333",
  "Blondie": "444-4444",
  "Jenny": "867-5309"
}
name = "Jenny"

phone_number = get_contact(contacts, name)

print("The phone number of", name, "is", phone_number)
