from characters import Character
import items

class Enemy(Character):
    def __init__(self, *, xp_reward: int, gold_reward: int, drop_loot: object, level: int, health_points: int,
                 attack_points: int, name: str) -> None:
        super().__init__(level=level, health_points=health_points, attack_points=attack_points, name=name)
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.drop_loot = drop_loot

class Slime(Enemy):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=25, attack_points=5, name='Slime', xp_reward=15, gold_reward=5, drop_loot=items.Goo())

class Skeleton(Enemy):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=35, attack_points=15, name='Skeleton', xp_reward=25, gold_reward=15, drop_loot=items.PileOfBones())

class Wolf(Enemy):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=20, attack_points=15, name='Wolf', xp_reward=20, gold_reward=10, drop_loot=items.WolfSkin())

class Troll(Enemy):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=75, attack_points=20, name='Troll', xp_reward=50, gold_reward=50, drop_loot=items.GoldIngot())

class Draugr(Enemy):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=100, attack_points=25, name='Draugr', xp_reward=100, gold_reward=5, drop_loot=items.IronSword())

class Dragon(Enemy):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=250, attack_points=40, name='Dragon', xp_reward=500, gold_reward=500, drop_loot=items.Chest())

class Ogr(Enemy):
    def __init__(self) -> None:
        super().__init__(level=1, health_points=150, attack_points=30, name='Ogr', xp_reward=250, gold_reward=100, drop_loot=items.MountainKey())