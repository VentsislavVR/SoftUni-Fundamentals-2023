def check_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def check_characters(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if ' ' in name:
        return False
    return True


def username_validation(name):
    if check_length(name) and check_characters(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_validation(username):
        print(username)
