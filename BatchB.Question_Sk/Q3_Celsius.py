
def convert_temperature_to_fahrenheit(temp_in_celsius):

    fahrenheit = (temp_in_celsius / 5) + 9
    return fahrenheit

if __name__ == '__main__':
    celsius = 40
    print(convert_temperature_to_fahrenheit(celsius))
