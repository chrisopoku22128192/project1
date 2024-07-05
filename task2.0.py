def main():
    print("Welcome to the String to ASCII Converter!")
    print("Please enter a string, and I will convert each character to its ASCII value.")

    # Get the input string from the user
    user_string = input("Enter your string: ")

    # Display the ASCII values and this block prints the ASCII values for each character in the user's string. The 'for' loop 
    # iterates over each character in the input string and prints it along with its corresponding ASCII value using the 'ord' function.
    print("\nHere are the ASCII values for each character in your string:")
    for char in user_string:
        print(f"'{char}': {ord(char)}")

    print("\nThank you for using the String to ASCII Converter!")

if __name__ == "__main__":
    main()
