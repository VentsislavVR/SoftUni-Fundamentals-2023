def add_func(album, song, composer, key):
    if song in album:
        print(f"{song} is already in the collection!")
        return album
    else:
        album[song] = {"composer": composer, "key_note": key}
        print(f"{song} by {composer} in {key} added to the collection!")
        return album


def remove_func(album, song):
    if song in albums:
        albums.pop(song)
        print(f"Successfully removed {song}!")
        return album
    else:
        print(f"Invalid operation! {song} does not exist in the collection.")
        return album


def change_func(album, song, key):
    if song in album:
        album[song]["key_note"] = key
        print(f"Changed the key of {song} to {key}!")
        return album
    else:
        print(f"Invalid operation! {song} does not exist in the collection.")
        return album



pieces_in_album = int(input())

albums = {}

for tracks in range(pieces_in_album):
    pieces = input().split("|")
    song_name = pieces[0]
    composer = pieces[1]
    key_note = pieces[2]
    albums[song_name] = {"composer": composer, "key_note": key_note}

while True:
    data = input()
    if data == "Stop":
        break
    data = data.split("|")
    command = data[0]

    if command == "Add":
        song_name = data[1]
        composer = data[2]
        key_note = data[3]
        albums = add_func(albums, song_name, composer, key_note)
    elif command == "Remove":
        song_name = data[1]
        albums = remove_func(albums, song_name)
    elif command == "ChangeKey":
        song_name = data[1]
        key_note = data[2]
        albums = change_func(albums, song_name, key_note)

# sorted_albums = sorted(albums.items(), key=lambda x: (x[0], x[1]['composer']))
# for key, value in sorted_albums:
#     song_name = key
#     composer = value['composer']
#     key_note = value['key_note']
#     print(f"{song_name} -> Composer: {composer}, Key: {key_note}")

# for key,value in sorted(albums.items(),reverse=False):
#     print(f"{key} -> Composer: {albums[key]['composer']}, Key: {albums[key]['key_note']}")
for key,value in albums.items():
    print(f"{key} -> Composer: {albums[key]['composer']}, Key: {albums[key]['key_note']}")