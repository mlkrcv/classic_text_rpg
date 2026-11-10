import random
import enemies
import battle
import characters
import menus
import items
import story
from utils import pause

class Location:
    def __init__(
            self,
            name: str,
            description: str,
            enemies: list,
            npc: list,
            connected_locations: list,
            locked: bool, visited: bool,
            required_items: list,
            quest: list,
            trader: list,
            first_visit: str
    ) -> None:

        self.name = name
        self.description = description
        self.enemies = enemies
        self.npc = npc
        self.connected_locations = connected_locations
        self.visited = visited
        self.locked = locked
        self.required_items = required_items
        self.quest = quest
        self.trader = trader
        self.first_visit = first_visit

    def save_start_state(self) -> None:
        self._start_locked = self.locked
        self._start_visited = self.visited
        self._start_connections = list(self.connected_locations)

    def reset(self) -> None:
        self.locked = self._start_locked
        self.visited = self._start_visited
        self.connected_locations = list(self._start_connections)

    def enter(self, player) -> None:
        if not self.visited:
            print(self.first_visit)
            self.visited = True
            if player.current_location == mountain:
                pause()
                print(f'{story.MOUNTAIN_INTRO_2}')
                self.fight_happens(player)

            elif player.current_location == wizard_tower:
                pause()
                menus.wizard_tower_menu(player)

    def found_something(self, player) -> None:
        variants = [
            items.Stone(),
            items.Stick(),
            items.PileOfBones(),
            items.Goo()
        ]
        item = random.choice(variants)
        print(f'You found {item.name}')
        player.inventory.append(item)

    def fight_happens(self, player) -> None:
        pause()
        if not self.enemies:
            print('There is nobody to attack You')
        else:
            enemy_class = random.choice(self.enemies)
            enemy = enemy_class()
            battle.fight(character_1=player, character_2=enemy)
            if player.is_alive():
                player.gain_rewards(enemy)
                if player.current_location == mountain:
                    player.victory = True

    def nothing_happens(self) -> None:
        pause()
        print('You search around but do not see anything special')

    def interact(self, player, trader) -> None:
        if player.has_item([items.MaskOfTruth]) and player.current_location == forest_lake:
            print(f'{story.FOREST_LAKE_PATH}')
            forest_lake.connect(secret_location)

        elif player.current_location == village:
            pause()
            menus.village_menu(player, trader)

        elif player.current_location == cave:
            self.fight_happens(player)

        else:
            possibility = [
            (self.nothing_happens, ()),
            (self.fight_happens, (player,)),
            (self.found_something, (player,)),
        ]
            func, args = random.choice(possibility)
            func(*args)


    def explore(self, player, trader) -> None:
        print(self.description)

        self.enter(player)
        self.interact(player, trader)

    def connect(self, location: 'Location') -> None:
        if location not in self.connected_locations:
            self.connected_locations.append(location)

        if self not in location.connected_locations:
            location.connected_locations.append(self)

    def show_connections(self) -> None:
        for index, location in enumerate(self.connected_locations, start=1):
            print(f'{index}. {location.name}')

    def __str__(self) -> str:
        return self.name

spawn = Location(
    'A strange place',
    'A small meadow in the middle of forest',
    [enemies.Slime],
    [],
    [],
    False,
    False,
    [],
    [],
    [],
    f'{story.SPAWN_FIRST_VISIT}'
)

forest = Location(
    'Forest',
    'A beautiful sunny forest',
    [enemies.Slime, enemies.Wolf],
    [],
    [],
    False,
    False,
    [],
    [],
    [],
    f'{story.FOREST_FIRST_VISIT}'
)

deep_forest = Location(
    'Deep forest',
    'Dark and scary place',
    [enemies.Skeleton, enemies.Troll, enemies.Draugr],
    [],
    [],
    False,
    False,
    [],
    [],
    [],
    f'{story.DEEP_FOREST_FIRST_VISIT}'
)

village = Location(
    'Village',
    'A small village with a travelling merchant',
    [],
    [],
    [],
    False,
    False,
    [],
    [],
    [characters.Trader()],
    f'{story.VILLAGE_FIRST_VISIT}'
)

secret_location = Location(
    'Secret path',
    'A small hidden path. Where does it lead?',
    [enemies.Slime],
    [],
    [],
    True,
    False,
    [items.MaskOfTruth],
    [],
    [],
    f'{story.SECRET_LOCATION_FIRST_VISIT}'
)

wizard_tower = Location(
    'Ruined tower',
    'Old and heavily damaged tower',
    [],
    [],
    [],
    False,
    False,
    [],
    [],
    [],
    f'{story.WIZARD_TOWER_FIRST_VISIT}'
)

forest_lake = Location(
    'Forest lake',
    'A small lake',
    [enemies.Skeleton, enemies.Troll, enemies.Wolf],
    [],
    [],
    False,
    False,
    [],
    [],
    [],
    f'{story.FOREST_LAKE_FIRST_VISIT}'
)

cave = Location(
    'Cave',
    'An old mining shaft now seats abandoned. Right...?',
    [enemies.Ogr],
    [],
    [],
    False,
    False,
    [],
    [],
    [],
    f'{story.CAVE_FIRST_VISIT}'
)

mountain = Location(
    'Mountain',
    'A mountain where the beast rest',
    [enemies.Dragon],
    [],
    [],
    True,
    False,
    [items.MountainKey],
    [],
    [],
    f'{story.MOUNTAIN_INTRO}'
)

spawn.connect(forest)
forest.connect(village)
forest.connect(deep_forest)
forest.connect(forest_lake)
village.connect(cave)
deep_forest.connect(mountain)
#forest_lake.connect(secret_location)
secret_location.connect(wizard_tower)

all_locations = [
    spawn, forest, deep_forest, village, secret_location,
    wizard_tower, forest_lake, cave, mountain
]

for location in all_locations:
    location.save_start_state()


def reset_world() -> None:
    for location in all_locations:
        location.reset()