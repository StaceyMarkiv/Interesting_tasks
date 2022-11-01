from abc import ABC
from typing import List

__all__ = ['Media', 'Newspaper', 'TV', 'Radio', 'Internet', 'Planet']


class Media(ABC):
    media_name: str = ''

    def __init__(self):
        super().__init__()
        self.message_text: str = f'{self.media_name} reported:'

    def create_news(self, hero, place):
        place_name: str = getattr(place, 'city_name', 'place')
        hero_name: str = getattr(hero, 'hero_name', 'hero')

        print(self.message_text, end=' ')
        print(f'{hero_name} saved {place_name}!')


class Newspaper(Media):
    media_name = 'Newspaper'


class TV(Media):
    media_name = 'TV'


class Radio(Media):
    media_name = 'Radio'


class Internet(Media):
    media_name = 'Internet'


class Planet(Media):
    media_name = 'Planet'

    def __init__(self, coordinates: List[float]):
        super().__init__()
        self.coordinates = coordinates
        self.message_text = f'{self.media_name} at {self.coordinates} reported:'
