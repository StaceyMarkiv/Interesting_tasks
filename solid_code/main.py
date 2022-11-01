from heroes import *
from places import *


def save_the_place(hero: SuperHero, place: Place):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    place.media_message(hero)


if __name__ == '__main__':
    save_the_place(Superman(), Tokyo())

    print('-' * 20)
    save_the_place(SuperHero('Terminator', False), Kostroma())

    print('-' * 20)
    save_the_place(TexasRanger(), Moscow())
