def store_data_func(number):
    data = {}
    for _ in range(number):
        current_data = input().split("|")
        piece = current_data[0]
        composer = current_data[1]
        key = current_data[2]
        data[piece] = [composer, key]
    return data


def add_command_function(piece, composer, key, data):
    if piece not in data:
        data[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_command_function(piece, data):
    if piece in data:
        print(f"Successfully removed {piece}!")
        del data[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_function(piece, new_key, data):
    if piece in data:
        # Our dictionary for example --> {"Fur Elise":['Beethoven', 'A Minor']}
        # At index 0 in list is composer at index 1 is the key
        data[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_function(data):
    result = ""
    for piece in data:
        composer = data[piece][0]
        key = data[piece][1]
        result += f"{piece} -> Composer: {composer}, Key: {key}\n"
    return result


# Our core function that navigates our entire program.Each time in it,
# we will accept one element as a parameter --> number of pieces
def the_pianist_func(number):
    # store_data_func returns a dictionary containing as key the name of
    # pieces and as value containing a list of two elements. At index 1 in
    # the list is the name of the composer,and at index 2 in the list
    # the specific key.
    data = store_data_func(number)

    while True:
        command = input().split("|")

        if command[0] == "Stop":
            print(print_function(data))
            break
        current_command = command[0]
        piece = command[1]

        if current_command == "Add":
            composer = command[2]
            key = command[3]
            add_command_function(piece, composer, key, data)

        elif current_command == "Remove":
            remove_command_function(piece, data)
        elif current_command == "ChangeKey":
            new_key = command[2]
            change_key_function(piece, new_key, data)


number_of_pieces = int(input())
the_pianist_func(number_of_pieces)
