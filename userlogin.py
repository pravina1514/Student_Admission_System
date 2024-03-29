class Authenticator:

    def __init__(self):
        self.message = None
        self.password = None
        self.valid_password_flag = False

    def display_greeting_message(self, message):

        self.message = message
        print(self.message)

    def process_password(self):
        attempts_left = 3
        while self.valid_password_flag == False and attempts_left != 0:
            self.password = input("Please enter your password: ")

            password_length = len(self.password)
            password_length_flag = False

            if password_length < 10:
                print("The password should not be less than 10 characters")
            else:
                password_length_flag = True

            capital_letters_flag = False
            special_characters_flag = False
            numbers_flag = False

            numbers_count = 0
            special_characters_count = 0

            for character in self.password:
                if character.isupper() == True and capital_letters_flag == False:
                    capital_letters_flag = True

                if character.isdigit() == True:
                    numbers_count = numbers_count + 1
                    if numbers_count == 2 or numbers_count == 3:
                        numbers_flag = True
                    else:
                        numbers_flag = False

                if character.isalnum() == False:
                    special_characters_count = special_characters_count + 1

                    if special_characters_count == 1:
                        special_characters_flag = True
                    else:
                        special_characters_flag = False

            if capital_letters_flag == False:
                print("The password should have at least one upper case letter.")

            if numbers_flag == False:
                print("The password should contain 2 or 3 numbers")

            if special_characters_flag == False:
                print("The password should contain one special character")

            if password_length_flag == True and capital_letters_flag == True and numbers_flag == True and special_characters_flag == True:
                self.valid_password_flag = True
                print("The entered password satisfies every criteria. Let's proceed to a next step...")
                break
            else:
                attempts_left = attempts_left - 1

                if attempts_left != 0:
                    print("Please enter a valid password.")
                    print("Number of attempts left: " + str(attempts_left) + "\n")
                else:
                    print("\n" + "No attempts left now! The program has been terminated")

        return self.valid_password_flag
