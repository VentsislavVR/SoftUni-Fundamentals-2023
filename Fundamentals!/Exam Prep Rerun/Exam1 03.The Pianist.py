def add(album, info):
    if info[0] not in album.keys():
        album[info[0]] = [info[1], info[2]]
        return album
    return False


def remove(album, info):
    if info[0] in album.keys():
        del album[info[0]]
        return album
    return False


def change_key(album, info):
    if info[0] in album:
        album[info[0]][1] = info[1]
        return album
    return False


def store_data(data):
    album = {}
    for d in range(data):
        piece, composer, key_note = input().split("|")
        album[piece] = [composer, key_note]
    return album


def results(album):
    for key, val in album.items():
        print(f"{key} -> Composer: {val[0]}, Key: {val[1]}")


def the_pianist_func(data):
    album = store_data(data)

    while True:
        command, *info = input().split("|")
        if command == "Stop":
            results(album)
            break
        elif command == "Add":
            # add(album,info)
            if add(album,info):
                print(f"{info[0]} by {info[1]} in {info[2]} added to the collection!")
            else:
                print(f"{info[0]} is already in the collection!")
        elif command == "Remove":
            # remove(album,info)
            if remove(album,info):
                print(f"Successfully removed {info[0]}!")
            else:
                print(f"Invalid operation! {info[0]} does not exist in the collection.")
        elif command == "ChangeKey":
            # change_key(album,info)
            if change_key(album,info):
                print(f"Changed the key of {info[0]} to {info[1]}!")
            else:
                print(f"Invalid operation! {info[0]} does not exist in the collection.")

number_of_pieces = int(input())
the_pianist_func(number_of_pieces)
