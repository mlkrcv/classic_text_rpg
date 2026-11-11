import characters
import items


def test_use_healing_potion_heals_and_remove_it():
    player = characters.Player()
    potion = items.HealingPotion()
    player.inventory.append(potion)
    player.health_points = 10

    result = player.use_healing_potion()

    assert result is True
    assert player.health_points == player.max_health_points
    assert potion not in player.inventory