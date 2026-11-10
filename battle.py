import time
from characters import Character

def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        print(f'{character_1.name} attacks {character_2.name}!')
        time.sleep(0.3)
        character_1.attack(target=character_2)
        print(f'{character_2.name} has {character_2.health_points} HP left!')
        time.sleep(0.3)
        if character_2.is_dead():
            print(f'{character_1.name} kills {character_2.name}!')
            time.sleep(0.3)
            break
        else:
            print(f'{character_2.name} attacks {character_1.name}!')
            time.sleep(0.3)
            character_2.attack(target=character_1)
            print(f'{character_1.name} has {character_1.health_points} HP left!')
            time.sleep(0.3)