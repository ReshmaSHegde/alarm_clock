import random
import pywhatkit

class Video:
    def __init__(self):
        with open("you_tube_links", 'r') as file:
            self.file_contents = file.readlines()
            # Randomly picking the YouTube link from the text file (you_tube_links)
            self.random_pick = random.choice(self.file_contents)

    #  Playing the YouTube video
    def utube_video(self):
        pywhatkit.playonyt(self.random_pick)
        print(f"Video : {self.random_pick} is playing...")