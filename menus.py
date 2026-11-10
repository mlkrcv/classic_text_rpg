import world_map
import validators
import items
import story
from utils import pause

def player_menu(player, trader) -> None:
    print(f"""
    Current location: {player.current_location}
        
    1. Explore ...
    
    2. Move to ...
    
    3. Inventory
    
    4. Character
    
    5. Map
""")
    choice = input('> ')

    if choice == '1':
        explore_menu(player, trader)

    elif choice == '2':
        move_menu(player)

    elif choice == '3':
        while True:
            print(f"""
=========================================
                Inventory
=========================================
        """)
            print(player.check_inventory())
            print("""
=========================================
    What would You like to do?
        
    1. Equip item
    
    2. Take off item
    
    3. Heal
    
    4. Back 
""")
            choice = input('> ')
            if choice == '1':
                print('What do you want to equip?')

                count = len(player.inventory)

                item_index = validators.get_valid_index('> ', count)

                item = player.inventory[item_index]

                player.equip(item)

            elif choice == '2':
                print(f'What do you want to take off?')

                if not player.equipment['Weapon']:
                    print('You dont have weapon equipped')

                else:
                    count = len(player.inventory)

                    item_index = validators.get_valid_index('> ', count)

                    item = player.inventory[item_index]

                    player.unequip(item)


            elif choice == '3':
                if player.health_points == player.max_health_points:
                    print('You already at full health')
                elif player.use_healing_potion():
                    print('You have been fully healed')
                else:
                    print('You do not have a healing potion')

            elif choice == '4':
                return

            else:
                print('You cannot choose from what You cannot do')

    elif choice == '4':
        print(f"""
=========================================
                {player.name}
=========================================
    You are now currently at -> {player.current_location} 
    
    {player.level} | lvl
    {player.health_points}/{player.max_health_points} | HP
    {player.attack_points} | DMG
    {player.gold} | G
    {player.xp} / {player.xp_needed} | XP
""")
        pause()

    elif choice == '5':
        if any(isinstance(item, items.WorldMap) for item in player.inventory):
            print(world_map.world_map)
        else:
            print('You do not have a map')

    else:
        print('You cannot choose from what You cannot do')

def move_menu(player) -> None:
    print('\nWhere do you want to go?\n')

    player.current_location.show_connections()

    count = len(player.current_location.connected_locations)

    choice = validators.get_valid_index('> ', count)

    chosen_location = player.current_location.connected_locations[choice]

    player.move(chosen_location)

    print(f'\nYou moved to {player.current_location}')

def explore_menu(player, trader) -> None:
    player.current_location.explore(player, trader)

def loading_screen_menu() -> bool:
    print("""
1. Try again?

2. Exit the game
""")

    while True:
        choice = input('> ')
        if choice == '1':
            return True
        if choice == '2':
            return False
        print('Please enter 1 or 2.')

def village_menu(player, trader) -> None:
    print("""
You walk into the village and see a small shop 
and a beggar nearby

What will You do?

1. Enter shop

2. Go to beggar        
""")

    choice = input('> ')
    if choice == '1':
        trade_menu(player, trader)

    elif choice == '2':
        beggar_menu(player)

    else:
        print('You cannot choose from what You cannot do')

def wizard_tower_menu(player) -> None:
    print(f'{story.WIZARD_DIALOG_INTRO}')
    pause()
    print(f'{story.WIZARD_DIALOG_1}')
    pause()
    print(f'{story.WIZARD_DIALOG_2}')
    pause()
    print(f'{story.WIZARD_DIALOG_OUTRO}')
    player.max_health_points += 100
    player.heal()
    player.attack_points += 50

def beggar_menu(player) -> None:
    print(story.BEGGAR_DIALOG_1)
    print("""
What will You do?

1. Help old men | - 15G

2. Ignore him
""")
    choice = input('> ')
    if choice == '1':
        if player.gold >= 15:
            player.gold -= 15
            print(story.BEGGAR_DIALOG_2)
            pause()
            print(story.BEGGAR_DIALOG_3)
            player.inventory.append(items.MaskOfTruth())
            print('You got... a mask?')
        else:
            print('You do not have enough')

    elif choice == '2':
        return

    else:
        print('You cannot choose from what You cannot do')

def trade_menu(player, trader) -> None:
    while True:
        print(f"""
    Welcome to the shop Traveller!
        
    Do You want to buy something or sell?
        
    1. Buy
    
    2. Sell
    
    3. Leave
""")

        choice = input('> ')
        if choice == '1':
            if not trader.inventory:
                print('Sorry, You bought all of the items')
            else:
                print('Choose whatever You want!')
                print(f'You have: {player.gold} | G')
                for index, item in enumerate(trader.inventory, start=1):

                    print(f"""
    {index}. {item.name}
    {item.description}
    Price: {item.price} G
""")

                count = len(trader.inventory)
                index = validators.get_valid_index('> ', count)
                item = trader.inventory[index]

                trader.buy(player, item)

        elif choice == '2':
            if not player.inventory:
                print('You dont have anything to sell')
            else:
                print('What do You want to sell?')
                for index, item in enumerate(player.inventory, start=1):
                    print(f'{index}. {item.name} | {item.price} G')

                count = len(player.inventory)
                index = validators.get_valid_index('> ', count)
                item = player.inventory[index]
                trader.sell(player, item)

        elif choice == '3':
            return

        else:
            print('You cannot choose from what You cannot do')