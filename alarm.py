import time


def get_time_left(end_time, start_time=time.time()):
    return max(end_time - start_time, 0)


class SoundPlayer(object):

    def play(self):
        pass


class Alarm(object):
    did_ring: bool
    player: SoundPlayer

    def __init__(self, end_time, player):
        self.end_time = end_time
        self.did_ring = False
        self.player = player

    def check(self):
        if get_time_left(self.end_time) == 0:
            if not self.did_ring:
                self.player.play()
                self.did_ring = True
