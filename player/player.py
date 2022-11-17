import vlc
import os


class Player():

    def __init__(self):
        self.player = None

    def play(self, filename):
        # Stop previous playback
        self.stop()

        # Resolve the soundfile path
        path = os.path.join(os.getcwd(), filename)
        vlc_filename = f'file://{path}'

        # Instantiate the instance, media player, list and media
        instance = vlc.Instance()
        media_list = instance.media_list_new()
        media_player = instance.media_list_player_new()
        media = instance.media_new(vlc_filename)

        # Set the media player into loop mode
        media_player.set_playback_mode(1)

        # Add the media to the list, and the list to the media player
        media_list.add_media(media)
        media_player.set_media_list(media_list)

        # Start playback
        media_player.play()

    def stop(self):
        if isinstance(self.player, vlc.MediaPlayer):
            self.player.stop()
