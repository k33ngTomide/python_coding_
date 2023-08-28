def validate_if_value_is_not_negative(value):
    if value < 0: raise ValueError("Value cannot be Negative")


class Television:
    channel = 0
    volume_level = 0
    on = False

    def __init__(self) -> None:
        super().__init__()

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def validate_if_tv_is_On(self):
        if not self.on: raise ValueError("Television is off")

    def set_channel(self, channel_number):
        self.validate_if_tv_is_On()
        validate_if_value_is_not_negative(channel_number)
        self.channel = channel_number

    def get_channel(self) -> int:
        return self.channel

    def set_volume(self, volume_level):
        self.validate_if_tv_is_On()
        validate_if_value_is_not_negative(volume_level)
        self.volume_level = volume_level

    def get_volume(self):
        return self.volume_level

    def channel_up(self):
        if self.channel < 1000:
            self.channel += 1

    def channel_down(self):
        if self.channel > 0:
            self.channel -= 1

    def volume_up(self):
        if self.volume_level < 100:
            self.volume_level += 1

    def volume_down(self):
        if self.volume_level > 0:
            self.volume_level -= 1
