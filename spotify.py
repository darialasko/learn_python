playlist = {
    "titile": "chill",
    "author": "Daria Lasko",
    "songs": [
        {
            "title": "song1",
            "artist": ["blue"],
            "duration": 2.5
        },
        {
            "title": "song2",
            "artist": ["red", "green"],
            "duration": 3.5
        },
        {
            "title": "song3",
            "artist": ["yellow"],
            "duration": 2.0
        }
    ]
}
total_length = 0
for song in playlist["songs"]:
    total_length += song["duration"]
print(total_length)
