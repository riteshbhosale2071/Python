def songs():
    songs = input("Enter song names separated by comma: ").split(",")

    songs.sort()

    print("\nPlaylist:")

    for song in songs:
        print(song.strip())

songs()