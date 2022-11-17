import datetime
import os


class Timer():

    def __call__(self):
        ret = {'hour': self.hour(),
               'minute': self.minute(),
               'winter': self.winter()}
        return ret

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

        suffix = '-' + ('normal' if not winter else 'snow') + '.mp3'
        return os.path.join('soundfiles', hour, hour + suffix)
