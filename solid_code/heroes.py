from antagonistfinder import AntagonistFinder
from places import Place
from attack import *

__all__ = ['SuperHero', 'Superman', 'TexasRanger']


class SuperHero:

    def __init__(self, name='Super Hero', can_use_ultimate_attack=True):
        self.hero_name: str = name
        self.can_use_ultimate_attack: bool = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place: Place):
        self.finder.get_antagonist(place)

    def attack(self):
        print('Simple punch')

    def ultimate(self):
        print('Multi-kick')


class Superman(SuperHero, EyeLasers):

    def __init__(self):
        super().__init__()
        self.hero_name = 'Clark Kent'
        self.can_use_ultimate_attack = True

    def ultimate(self):
        self.incinerate_with_lasers()


class TexasRanger(SuperHero, SuperKick, GunFire):

    def __init__(self):
        super().__init__()
        self.hero_name = 'Chuck Norris'
        self.can_use_ultimate_attack = True

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        self.roundhouse_kick()
