import pygame

pygame.init()

# Load the MP3 file into the Pygame music mixer
pygame.mixer.music.load('Radiohead_-_Let_Down___Choir__Complete__NEW_VERSION(128k).mp3')

# Start playing the music
pygame.mixer.music.play()

# Keep the program running until the user presses Enter
input()