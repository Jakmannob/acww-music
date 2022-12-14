import datetime
import os


class Timer():

    def hour(self):
        now = datetime.datetime.now()
        return now.hour

    def minute(self):
        now = datetime.datetime.now()
        return now.minute

    def winter(self):
        now = datetime.datetime.now()
        return now.month in [1, 2, 12]

    def current_songfile(self):
        hour = str(self.hour()).zfill(2)
        winter = self.winter()

        suffix = '-' + ('normal' if not winter else 'snow')
        songpath = os.path.join('soundfiles', hour, hour + suffix)
        suffix = '-loop.mp3'
        if not os.path.exists(songpath + suffix):
            suffix = '.mp3'
        print(songpath + suffix)
        return songpath + suffix
