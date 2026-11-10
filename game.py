import characters
import story
import menus
import locations
from utils import pause
import validators

while True:
    trader = characters.Trader()
    player = characters.Player()

    print(story.INTRO_1)
    pause()
    print(story.INTRO_2)
    pause()
    print(story.INTRO_3)

    player.name = validators.get_non_empty_string('\nEnter your name: ')
    player.current_location = locations.spawn

    locations.reset_world()

    while True:
        menus.player_menu(player, trader)
        if player.is_dead():
            print("""
=========================================
                You died!
=========================================
""")
            play_again = menus.loading_screen_menu()
            break

        elif player.has_won():
            print(story.DRAGON_FINAL)
            pause()
            print("""
=========================================
             You have won!
=========================================
""")
            print(f"""
=========================================
             Player stats:
=========================================            

    {player.max_health_points} | HP
    {player.attack_points} | DMG
    {player.level} | lvl
    {player.gold} | G
""")
            play_again = menus.loading_screen_menu()
            break

    if not play_again:
        print('Thank You for playing!')
        break