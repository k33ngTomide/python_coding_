import math


def main() -> None:
    r, l = input("Enter the radius of the cylinder: ").split(" ", 1)

    radius = float(r)
    length = float(l)

    area = radius * radius * math.pi
    volume = area * length

    print(f"The area is {area} \nThe volume is {volume}")


if __name__ == '__main__':
    main()
