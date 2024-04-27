'''
Assistant bot module
'''

def parse_input(user_input: str) -> str:
    '''
    Parses the user input from the command line
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: slice, contacts: dict) -> str:
    '''
    Adds a phone for a specific user
    '''
    if len(args) != 2:
        return "There should be two arguments, name and phone"
    name, phone = args
    if contacts.get(name) is not None:
        return "Contact already exists"
    contacts[name] = phone
    return "Contact added."

def change_contact(args: slice, contacts: dict) -> str:
    '''
    Changes a phone for a specific user
    '''
    if len(args) != 2:
        return "There should be two arguments: name and phone"
    name, phone = args
    if contacts.get(name) is None:
        return "Contact doesn't exist"
    contacts[name] = phone
    return "Contact added."

def get_phone(args: slice, contacts: dict) -> str:
    '''
    Lists a phone for a specific user
    '''
    if len(args) != 1:
        return "There should be one argument: user's name"
    name = args[0]
    return contacts.get(name)

def get_all_phones(contacts: dict) -> str:
    '''
    Lists all the phones in the contacts
    '''
    phones = ""
    for name, phone in contacts.items():
        phones += f"Name: {name}, Phone: {phone}\n"
    return phones

def main():
    '''
    Main function
    '''
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_phones(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
