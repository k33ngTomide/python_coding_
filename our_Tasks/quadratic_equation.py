def main() -> None:
    a_, b_, c_ = input('Enter the value of a, b and c: ').split(" ", 2)

    a = float(a_)
    b = float(b_)
    c = float(c_)
    discriminant = (b * b) - (4 * a * c)

    r1 = (-b + (discriminant ** 0.5)) / (2 * a)
    r2 = (-b - (discriminant ** 0.5)) / (2 * a)

    if discriminant > 0:
        print("The equation has two roots of ", r1, " and ", r2)
    elif discriminant == 0:
        print("The equation has one root ", r1)
    else:
        print("The equation has no roots")


if __name__ == '__main__':
    main()
