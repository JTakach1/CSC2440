def addEntry(name, phoneNumber):
    phonebook[name] = phoneNumber
    print(f"Added entry: {name} - {phoneNumber}")

def searchEntry(name):
    if name in phonebook:
        return f"{name}'s phone number is {phonebook[name]}"
    else:
        return f"{name} not found in the phonebook."

def deleteEntry(name):
    if name in phonebook:
        del phonebook[name]
        return f"Deleted entry for {name}."
    else:
        return f"{name} not found in the phonebook."

if __name__ == "__main__":
    phonebook = {}

    addEntry("Alice", "123-456-7890")
    addEntry("Bob", "356-367-8878")
    print()

    print(searchEntry("Alice"))
    print(searchEntry("Charlie"))
    print()

    print(deleteEntry("Bob"))
    print(deleteEntry("Charlie"))
