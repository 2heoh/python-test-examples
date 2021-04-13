from unittest import TestCase
from unittest.mock import MagicMock

from alarm import get_time_left, SoundPlayer, Alarm


class AlarmTest(TestCase):

    def test_get_time_left_returns_difference_with_current_time(self):
        result = get_time_left(2, 1)

        self.assertEqual(result, 1)

    def test_get_time_left_returns_zero_then_time_is_over(self):
        result = get_time_left(0, 1)

        self.assertEqual(result, 0)

    def test_calls_play_sound_then_time_is_over(self):
        player = SoundPlayer()
        player.play = MagicMock()
        alarm = Alarm(0, player)

        alarm.check()

        player.play.assert_called()
