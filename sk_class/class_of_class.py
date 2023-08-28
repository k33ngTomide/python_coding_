
class Poster:
    poster_colour = "Green"

    def __init__(self, poster_one, poster_two):
        self.__first_poster = poster_one
        self.__second_poster = poster_two

    @property
    def first_poster(self):
        return self.__first_poster

    @first_poster.setter
    def first_poster(self, size):
        if size < 0:
            raise ValueError('Value can not be negative')
        self.__first_poster = value

    @property
    def second_poster(self):
        return self.__second_poster

    @second_poster.setter
    def second_poster(self, size):
        if size < 0:
            raise ValueError ('Value can not be negative')
        self.__second_poster = value

    def draw_poster(self):
        print(f'Drawing from point {self.__first_poster} to {self.__second_poster}')

    def __add__(self, other):
        return f'({self.__first_poster + other.__first_poster} , {self.__second_poster + other.__second_poster})'


if __name__ == '__main__':

    Poster.poster_colour = "White"

    street_poster = Poster(10, 20)
    pole_poster = Poster(56, 30)

    print(street_poster.first_poster)
    print(pole_poster.first_poster)

    print(street_poster + pole_poster)