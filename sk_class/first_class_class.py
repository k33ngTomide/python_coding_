
class Human:
    def __init__(self, first_name, last_name, age, height, weight, country_code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.country_code = country_code

    def tell_phone_number(self, phone_number) -> str:
        return f"The phone number is: {self.country_code}-{phone_number}"

    def __str__(self) -> str:
        return f"Name : {self.first_name}  {self.last_name} \nAge: {self.age}" \
               f"\nHeight: {self.height} \nWeight: {self.weight} \n{self.tell_phone_number(8100210906)}"


if __name__ == '__main__':
    tomide = Human("Akintomide", "Muiliyu", 40, 6.8, 67.5, +234 )
    print(tomide)
    

