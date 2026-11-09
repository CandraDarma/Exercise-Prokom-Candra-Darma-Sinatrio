def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album


print(make_album("Queen", "A Night at the Opera"))
print(make_album("Coldplay", "Parachutes"))
print(make_album("Adele", "21"))
print(make_album("Adele", "21", 11))
