
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
#
# area = 0.5*base*height
# print(f"The area of the triangle is: {area: .2f}")

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calc_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    new_triangle = Triangle(4.5, 3.8)
    print(new_triangle.calc_area())