def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError as e:
            return e
        except IndexError:
            return "Contact not found"
    return wrapper

class ContactAssistant:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, name, phone):
        if name in self.contacts:
            raise ValueError(f"Contact with name {name} already exists. Use 'change' command to update the phone number.")
        else:
            self.contacts[name] = phone
            return f"Contact {name} added with phone {phone}"

    @input_error
    def change_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Phone number for {name} changed to {phone}"
        else:
            raise IndexError

    @input_error
    def get_phone(self, name):
        if name in self.contacts:
            return f"The phone number for {name} is {self.contacts[name]}"
        else:
            raise IndexError

    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts found"
        else:
            result = "All contacts:\n"
            for name, phone in self.contacts.items():
                result += f"{name}: {phone}\n"
            return result.strip()

def main():
    assistant = ContactAssistant()

    while True:
        try:
            user_input = input("Enter command: ").lower().split(" ", 1)

            if not user_input:
                raise ValueError("Invalid command. Please try again.")

            command = user_input[0]

            if command == "hello":
                print("How can I help you?")
            elif command == "add":
                if len(user_input) == 1:
                    raise ValueError("Invalid command. Please try again. Use 'add <name> <phone>'")
                _, contact_info = user_input
                if len(contact_info.split()) != 2:
                    raise ValueError("Invalid command. Please try again. Use 'add <name> <phone>'")
                name, phone = contact_info.split(" ", 1)
                print(assistant.add_contact(name, phone))
            elif command == "change":
                if len(user_input) == 1:
                    raise ValueError("Invalid command. Please try again. Use 'change <name> <phone>'")
                _, contact_info = user_input
                name, phone = contact_info.split(" ", 1)
                print(assistant.change_contact(name, phone))
            elif command == "phone":
                if len(user_input) == 1:
                    raise ValueError("Invalid command. Please try again. Use 'phone <name>'")
                _, name = user_input
                print(assistant.get_phone(name))
            elif command == "show":
                if len(user_input) == 1 or (len(user_input) == 2 and user_input[1] == "all"):
                    print(assistant.show_all_contacts())
                else:
                    raise ValueError("Invalid command. Please try again.")
            elif command in ["close", "exit"] or (user_input[0] == 'good' and user_input[1] == 'bye'):
                print("Good bye!")
                break
            else:
                raise ValueError("Invalid command. Please try again.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
