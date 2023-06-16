def length_validation(password):
    if len(password) < 6 or len(password) > 10:  # if len(password) not in range(6,11)
        print("Password must be between 6 and 10 characters")
        return False
    return True


def symbols_validation(password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        return False
    return True


def two_digits_validation(password):
    counter_of_digits = 0
    for character in password:
        if character.isdigit():
            counter_of_digits += 1
    if counter_of_digits < 2:
        print("Password must have at least 2 digits")
        return False
    return True


some_password = input()
password_is_valid = [length_validation(some_password),
                     symbols_validation(some_password),
                     two_digits_validation(some_password)]

if all(password_is_valid):
    print("Password is valid")

