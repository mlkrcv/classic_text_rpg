import characters
import items
import locations


import pytest

@pytest.fixture(autouse=True)
def clean_world():
    locations.reset_world()
    yield
    locations.reset_world()


def test_use_healing_potion_heals_and_remove_it():
    player = characters.Player()
    potion = items.HealingPotion()
    player.inventory.append(potion)
    player.health_points = 10

    result = player.use_healing_potion()

    assert result is True
    assert player.health_points == player.max_health_points
    assert potion not in player.inventory


def test_player_has_no_healing_potion():
    player = characters.Player()

    result = player.use_healing_potion()

    assert result is False


def test_world_resets():
    locations.forest.visited = True
    locations.mountain.locked = False
    locations.forest_lake.connected_locations.append(locations.secret_location)

    locations.reset_world()

    assert not locations.forest.visited
    assert locations.mountain.locked
    assert locations.secret_location not in locations.forest_lake.connected_locations