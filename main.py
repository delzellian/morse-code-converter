import string

is_on = True

def welcome():
    print("Welcome to the Morse Code Converter!")

def convert_to_morse(message):
    morse_message = ""
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }

    for char in message.upper():
        morse_text = morse_dict.get(char, "")
        morse_message += morse_text + " "

    return print(f"Your message in morse code is: {morse_message}")

def check_input(message):
    is_valid = None
    for char in message:
        if char in string.punctuation:
            print("Please enter either letters or numbers! Thank You.")
            is_valid = False
        else:
            is_valid = True
    if is_valid == True:
        print("Thank You.")
        convert_to_morse(message)

while is_on:
    welcome()
    message = input("Please enter a message: ")
    check_input(message)
    user_input = input("Would you like to convert another message? (y/n): ")
    if user_input == "n":
        print("Goodbye!")
        is_on = False

