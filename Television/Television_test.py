import unittest
from Television import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        sony = Television()

    def test_that_television_can_be_created(self):
        sony = Television()
        self.assertIsNotNone(sony)

    def test_that_television_is_off(self):
        sony = Television()
        self.assertFalse(sony.on)

    def test_that_television_can_be_on(self):
        sony = Television()

        sony.turn_on()
        self.assertTrue(sony.on)

    def test_that_television_can_be_turned_off(self):
        sony = Television()
        sony.turn_on()

        sony.turn_off()
        self.assertFalse(sony.on)

    def test_that_television_can_set_channel(self):
        sony = Television()
        sony.turn_on()

        sony.set_channel(5)
        self.assertEqual(sony.get_channel(), 5)

    def test_that_television_can_set_volume(self):
        sony = Television()
        sony.turn_on()

        sony.set_volume(15)
        self.assertEqual(sony.get_volume(), 15)

    def test_that_channel_can_be_increased(self):
        sony = Television()
        sony.turn_on()

        sony.set_channel(10)

        sony.channel_up()
        self.assertEqual(sony.get_channel(), 11)

    def test_that_channel_can_be_reduced(self):
        sony = Television()
        sony.turn_on()

        sony.set_channel(11)

        sony.channel_down()
        self.assertEqual(sony.get_channel(), 10)

    def test_that_television_volume_can_be_increased(self):
        sony = Television()
        sony.turn_on()

        sony.set_volume(15)

        sony.volume_up()
        self.assertEqual(sony.get_volume(), 16)

    def test_that_television_volume_can_be_decreased(self):
        sony = Television()
        sony.turn_on()

        sony.set_volume(15)

        sony.volume_down()
        self.assertEqual(sony.get_volume(), 14)

    def test_that_television_cannot_set_volume_to_negative_value(self):
        sony = Television()
        sony.turn_on()

        self.assertRaises(ValueError, sony.set_volume, -15)

    def test_that_television_cannot_set_channel_to_negative_value(self):
        sony = Television()
        sony.turn_on()

        self.assertRaises(ValueError, sony.set_channel, -10)

    def test_that_television_cannot_be_operated_on_if_off(self):
        sony = Television()
        self.assertFalse(sony.on)

        self.assertRaises(ValueError, sony.set_channel, 10)
        self.assertRaises(ValueError, sony.set_volume, 30)


if __name__ == '__main__':
    unittest.main()
