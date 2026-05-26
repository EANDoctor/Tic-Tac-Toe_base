def get_menu_option():
    """
    Prints a menu with the following options:
      1. Human vs Human
      2. Random AI vs Random AI
      3. Human vs Random AI
      4. Human vs Unbeatable AI

    Returns a number between 1-4.
    Keeps asking if the user enters invalid data.
    """
    print("\n=== Tic-Tac-Toe ===")
    print("1. Human vs Human")
    print("2. Random AI vs Random AI")
    print("3. Human vs Random AI")
    print("4. Human vs Unbeatable AI")

    while True:
        user_input = input("Select an option (1-4): ").strip()

        if user_input in ('1', '2', '3', '4'):
            return int(user_input)

        print("Invalid option. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # Run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option)