from timer.timer import Timer
from player.player import Player
import time
import schedule


if __name__ == '__main__':
    t = Timer()
    current = t.current_songfile()
    player = Player()
    player.play(current)

    def music_job(timer, player):
        player.stop()
        current = timer.current_songfile()
        player.play(current)

    schedule.every().hour.at(':00').do(lambda: music_job(t, player))

    while True:
        schedule.run_pending()
        time.sleep(1)
