import vlc
import os


class Player():

    def __init__(self):
        self.player = None

    def play(self, filename):
        self.stop()
        path = os.path.join(os.getcwd(), filename)
        self.player = vlc.MediaPlayer(f'file://{path}')
        self.player.play()

    def stop(self):
        if isinstance(self.player, vlc.MediaPlayer):
            self.player.stop()
