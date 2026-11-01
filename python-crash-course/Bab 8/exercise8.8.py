def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album


while True:
    artist = input("Artist name (type 'q' to quit): ")
    if artist == "q":
        break
    title = input("Album title (type 'q' to quit): ")
    if title == "q":
        break
    print(make_album(artist, title))