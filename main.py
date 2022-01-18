from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("test1.mp3")

# Setting the volume
mixer.music.set_volume(1)

# Start playing the song
mixer.music.play()

# infinite loop
while True:
    query = input("  ")
    print(query)
    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
        # Stop the mixer
        mixer.music.stop()
        break
    elif query == 'a':
        mixer.music.queue("test.mp3", "nice", -1)
        mixer.music.play()
    elif query == '+':
        current_volume = mixer.music.get_volume()
        mixer.music.set_volume(current_volume + 0.1)
    elif query == '-':
        current_volume = mixer.music.get_volume()
        mixer.music.set_volume(current_volume - 0.1)
