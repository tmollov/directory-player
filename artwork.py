import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

# Get picture bytes from mp3 file
song_path = os.path.join("./krisko.mp3")
track = MP3(song_path)
tags = ID3(song_path)
pict = tags.getall("APIC")[0].data

# Write bytes to file
f = open("sample.jpg", "wb")
f.write(pict)
