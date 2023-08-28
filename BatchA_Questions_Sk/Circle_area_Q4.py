import math

# radius = float(input("Enter the radius of a circle: "))
#
# area = math.pi * (radius**2)
#
# print(f"Area =  {area:.2f}")


class Circle:

    def __init__(self, radius:float):
        self.radius = radius
        self.area = 0
    def calc_area(self):
        self.area = math.pi * (self.radius ** 2)

    def print_area(self):
        print(f"Area =: {self.area: .2f}")

if __name__ == '__main__':
    first_circle = Circle(2.1)
    first_circle.calc_area()
    first_circle.print_area()