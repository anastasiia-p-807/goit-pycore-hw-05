def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no such name in contacts."
        except ValueError:
            return "Give me valid name and phone please."
        except IndexError:
            return "Please provide all necessary arguments."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner

@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args[0].rstrip(), args[1].rstrip()
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, new_phone = args[0].rstrip(), args[1].rstrip()
    
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts: dict) -> str:
    if not contacts:
        return "Empty list."
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        try:
            if command in ["hi", "hello", "whatsup"]:
                print("How can I help you?")
            elif command in ["new", "add"]:
                if len(args) < 2:
                    print("Give me name and phone please e.g add Anna 3245465.")
                else:
                    print(add_contact(args, contacts))
            elif command in ["change", "update", "edit"]:
                if len(args) < 2:
                    print("Give me name and phone please e.g. update Anna 243546.")
                else:
                    print(change_contact(args, contacts))
            elif command in ["phone", "find"]:
                if len(args) < 1:
                    print("Enter user name e.g. find Annd.")
                else:
                    print(show_phone(args, contacts))
            elif command in ["all", "show", "list"]:
                print(show_all(contacts))
            elif command in ["close", "exit", "bye"]:
                print("Good bye!")
                break
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An error occurred: {e}. Try again.")

if __name__ == "__main__":
    main()