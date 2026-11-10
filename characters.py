import items
import story
from utils import pause
from items import Weapon

class Character:
    def __init__(self, *, level: int, health_points: int, attack_points: int, name: str) -> None:
        self.level = level
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points

    def get_attack(self):
        return self.attack_points

    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage=self.get_attack())

    def got_damage(self, *, damage: int) -> None:
        self.health_points -= damage

    def is_dead(self) -> bool:
        return self.health_points <= 0

    def is_alive(self) -> bool:
        return self.health_points > 0

class Player(Character):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=75, attack_points=15, name='Player')
        self.max_health_points = 75
        self.xp_needed = 25
        self.xp = 0
        self.gold = 0
        self.inventory = [items.IronSword()]
        self.current_location = None
        self.equipment = {'Weapon': None}
        self.victory = False

    def use_healing_potion(self) -> bool:
        for item in self.inventory:
            if isinstance(item, items.HealingPotion):
                self.heal()
                self.inventory.remove(item)
                return True

        return False

    def has_won(self) -> bool:
        return self.victory == True

    def get_attack(self):
        attack = super().get_attack()
        if self.equipment['Weapon']:
            attack += self.equipment['Weapon'].attack_points

        return attack

    def heal(self) -> None:
        self.health_points = self.max_health_points

    def equip(self, item) -> None:
        if isinstance(item, Weapon):
            self.equipment['Weapon'] = item
            print(f'You equipped {item}')
        else:
            print('You cannot equip this item')

    def unequip(self, item) -> None:
        if isinstance(item, Weapon):
            self.equipment['Weapon'] = None
            print(f'You unequipped {item}')

    def gain_rewards(self, enemy) -> None:

        self.gain_xp(enemy.xp_reward)
        self.gain_gold(enemy.gold_reward)
        self.gain_loot(enemy.drop_loot)

        print(f"""
    You have {self.health_points} HP left

    You got:
    {enemy.xp_reward} XP 
    {enemy.gold_reward} G
    And a item - {enemy.drop_loot}
    
    {self.xp} / {self.xp_needed} XP | {self.health_points} / {self.max_health_points} HP | {self.gold} G
""")
        pause()

    def gain_xp(self, xp_reward: int) -> None:
        self.xp += xp_reward
        while self.xp >= self.xp_needed:
            self.level_up()
            self.xp -= self.xp_needed
            self.xp_needed = self.level * self.level * 25
            print(f"""
            {self.health_points} / {self.max_health_points} HP 
            {self.attack_points} DMG
            {self.xp} / {self.xp_needed} XP
""")

    def gain_gold(self, gold_reward: int) -> None:
        self.gold += gold_reward

    def gain_loot(self, loot_reward: str) -> None:
        self.inventory.append(loot_reward)

    def level_up(self) -> None:
        self.level += 1
        self.max_health_points += 15
        self.health_points = self.max_health_points
        self.attack_points += 5
        print(story.LEVEL_UP)
        print(f"""
Congratulations! You reached level {self.level}!

You have been fully healed

Max health + 15
Attack + 5""")
        pause()

    def has_item(self, item_types):
        return any(
            isinstance(item, item_type)
            for item in self.inventory
            for item_type in item_types
        )

    def move(self, location):
        if location.locked:
            if self.has_item(location.required_items):
                print(f'You now has access to: {location.name}')
                location.locked = False

            else:
                print(f'You cannot enter {location.name}')
                return

        self.current_location = location

    def set_location(self, location):
        self.current_location = location
        location.visited = True

    def check_inventory(self) -> None:
        for index, item in enumerate(self.inventory, start=1):
            print(f'{index}. {item}')

class NPC:
    def __init__(self, *, name: str) -> None:
        self.name = name

class Trader(NPC):
    def __init__(self) -> None:
        super().__init__(name='Trader')
        self.inventory = [
            items.WorldMap(),
            items.HealingPotion(),
            items.SteelSword()
        ]

    def buy(self, player, item) -> None:
        if player.gold >= item.price:
            player.gold -= item.price
            player.inventory.append(item)
            self.inventory.remove(item)
            print(f'You bought {item.name}')

            pause()

        else:
            print('Sorry, You dont have enough gold!')

    def sell(self, player, item) -> None:
        if item == player.equipment['Weapon']:
            print('Take that off and then I will buy it')

        elif item.can_be_sold:
            self.inventory.append(item)
            player.gold += item.price
            player.inventory.remove(item)
            print(f'You sold {item.name}')

        else:
            print('Sorry, but I will not buy this item')

            pause()