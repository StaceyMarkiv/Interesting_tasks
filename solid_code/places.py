from abc import ABC, abstractmethod
from massmedia import *

__all__ = ['Place', 'Kostroma', 'Tokyo', 'Moscow']


class Place(ABC):
    city_name: str = ''
    mass_media: list = []

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_danger(self):
        pass

    def report_danger(self):
        print(f'In {self.city_name}:', end=' ')
        self.get_danger()

    def media_message(self, hero):
        for media in self.mass_media:
            media.create_news(hero, self)


class Kostroma(Place):
    city_name = 'Kostroma'
    mass_media = [TV(), Radio(), Newspaper(), Planet([1.2334, 4.212324, 2.343535])]

    def get_danger(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    city_name = 'Tokyo'
    mass_media = [TV(), Newspaper(), Internet()]

    def get_danger(self):
        print('Godzilla stands near a skyscraper')


class Moscow(Place):
    city_name = 'Moscow'
    mass_media = [Internet()]

    def get_danger(self):
        print('Awful Russian Bear walks along the street')
