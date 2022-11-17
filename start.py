from timer.timer import Timer
from player.player import Player
import time

if __name__ == '__main__':
    t = Timer()
    current = t.current_songfile()
    print(f'Here is the current songfile: {current}')
    t = 10
    print(f'I will now play it for {t} seconds...')
    player = Player()
    player.play(current)
    time.sleep(t)
    player.stop()
    print("Now wasn't that nice!")
