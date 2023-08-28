
class Gun:

    bullet = 50

    def __init__(self, color: str, size:int, number_of_rounds, length, type, weight):
        self.color = color
        self.size = size
        self.number_of_rounds = number_of_rounds
        self.length = length
        self.type = type
        self.weight = weight

    def __str__(self) -> str:
        stars = "*" * 20
        return f"{stars}" \
               f"\nColor: {self.color} \nSize: {self.size}" \
               f"\nBullet Capacity: {self.number_of_bullet} Bullets" \
               f"\nThe length is: {self.length}Inches \nType: {self.type} \nWeight: {self.weight}Kg\n{stars}"

    def pull_trigger(self):
        self.bullet -= 1

    def add(self, reload):
        self.bullet += reload


if __name__ == '__main__':
    gun1 = Gun("Black", 23, 60, 40.9, "Ak-47 Super", 30)
    gun2 = Gun("White", 29, 40, 35.5, "Ak-50 Alpha", 20)

    print(Gun.bullet)
    Gun.pull_trigger(gun1)
    Gun.pull_trigger(gun1)
    Gun.pull_trigger(gun1)
    Gun.pull_trigger(gun1)
    print(gun1)
    Gun.pull_trigger(gun1)
    Gun.pull_trigger(gun1)
    Gun.pull_trigger(gun1)
    Gun.pull_trigger(gun1)

    print(gun1.bullet)
    print(gun2.bullet)


