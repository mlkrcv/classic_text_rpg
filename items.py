class Item:
    def __init__(self, *, name:str, price: int, description: str, can_be_sold: bool) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.can_be_sold = can_be_sold

    def __str__(self) -> str:
        return self.name

class Weapon(Item):
    def __init__(self, *, name: str, price: int, description: str, attack_points: int) -> None:
        super().__init__(name=name, price=price, description=description, can_be_sold=True)
        self.attack_points = attack_points

class IronSword(Weapon):
    def __init__(self) -> None:
        super().__init__(name='Iron sword', price=10, description='Old and rusty iron sword + 5 DMG', attack_points=5)

class SteelSword(Weapon):
    def __init__(self) -> None:
        super().__init__(name='A steel sword', price=100, description='A brand new steel sword. Sharp! + 25 DMG', attack_points=25)

class Potion(Item):
    def __init__(self, *, name: str, price: int, description: str, health_points: int) -> None:
        super().__init__(name=name, price=price, description=description, can_be_sold=True)
        self.health_points = health_points

class HealingPotion(Potion):
    def __init__(self) -> None:
        super().__init__(name='Healing potion', price=25, description='Small bottle of healing liquid | Fully restores Your health', health_points=10)
        #health_points is added in order for it to be an easy update when the time comes

class WorldMap(Item):
    def __init__(self) -> None:
        super().__init__(name='Map', price=50, description='A map with locations around You', can_be_sold=True)

class WolfSkin(Item):
    def __init__(self) -> None:
        super().__init__(name='A wolf skin', price= 15, description='Skin of a wolf. Smells.', can_be_sold=True)

class PileOfBones(Item):
    def __init__(self) -> None:
        super().__init__(name='A pile of bones', price=5, description='Not much use of it', can_be_sold=True)

class Goo(Item):
    def __init__(self) -> None:
        super().__init__(name='Goo', price=35, description='Gross... and costs allot', can_be_sold=True)

class AnimalHides(Item):
    def __init__(self) -> None:
        super().__init__(name='Animal hides', price=25, description= 'Sawed together animal hides', can_be_sold=True)

class GoldIngot(Item):
    def __init__(self) -> None:
        super().__init__(name='Gold ingot', price=100, description='Pure gold ingot', can_be_sold=True)

class Chest(Item):
    def __init__(self) -> None:
        super().__init__(name='Chest', price=0, description='Who knows what is inside', can_be_sold=True)

class Quest(Item):
    def __init__(self, *, name: str, price: int, description: str) -> None:
        super().__init__(name=name, price=price, description=description, can_be_sold=False)

class MountainKey(Quest):
    def __init__(self) -> None:
        super().__init__(name='Key', price=0, description='Old and rusty key. Wonder what it opens?')

class MaskOfTruth(Quest):
    def __init__(self) -> None:
        super().__init__(name='Mask of truth', price=0, description='Strange wooden mask',)

class Stick(Item):
    def __init__(self) -> None:
        super().__init__(name='Stick', price=1, description='Just a stick', can_be_sold=True)

class Stone(Item):
    def __init__(self) -> None:
        super().__init__(name='Stone', price=2, description='Regular stone', can_be_sold=True)