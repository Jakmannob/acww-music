from timer.timer import Timer
from player.player import Player
import time

if __name__ == '__main__':
    t = Timer()
    current = t.current_songfile()
    print(f'Here is the current songfile: {current}')
    print('I will now play it for 5 seconds...')
    player = Player()
    player.play(current)
    time.sleep(5)
    player.stop()
    print("Now wasn't that nice!")
