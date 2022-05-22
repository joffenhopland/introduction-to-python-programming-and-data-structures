def create_dict():
    with open("USCapitals.txt", "r") as file:
        dictionary = {}
        for line in file:
            line = line.strip()
            (key, val) = line.split(", ")
            dictionary[key] = val
    return dictionary


def main():
    user_input = input("Enter a state to display its capital: ")
    user_input = user_input.title()

    end_loop = True
    while end_loop == True:
        if user_input in create_dict().keys():
            print(
                f"{create_dict()[user_input]} is the capital in {user_input}.")
            end_loop = False
        else:
            print(f"Your input is not a state")
            user_input = input("Enter a state to display its capital: ")
            user_input = user_input.title()


main()
