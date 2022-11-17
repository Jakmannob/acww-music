import datetime


class Timer():

    def __call__(self):
        ret = {'hour': self.get_hour(),
               'minute': self.get_minute(),
               'winter': self.is_winter()}
        return ret

    def get_hour(self):
        now = datetime.datetime.now()
        return now.hour

    def get_minute(self):
        now = datetime.datetime.now()
        return now.minute

    def is_winter(self):
        now = datetime.datetime.now()
        return now.month in [1, 2, 12]
