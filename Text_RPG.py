import pygame
import sys
import random

pygame.init()
game_font = pygame.font.Font('font/Pixeltype.ttf', 50)
screen = pygame.display.set_mode([800, 500])
timer = pygame.time.Clock()

# Enemies
enemies = ["Dire Wolf", "Goblin", "Bandit"]
enemyhp = 1
enemy_attack = 1
club = random.randint(7, 9)
dagger = random.randint(5, 8)
axe = random.randint(6, 7)
selected_enemy = random.choice(enemies)

if selected_enemy == "Dire Wolf":
    enemyhp = 30
if selected_enemy == "Goblin":
    enemyhp = 20
if selected_enemy == "Bandit":
    enemyhp = 25

enemies2 = ["Skeleton", "Zombie", "Banshee"]
# Skeleton has 25 HP and DMG range of 8 to 9
# Zombie has 35 HP and DMG range of 9 to 11
# Banshee has 40 HP and DMG range of 5 to 15

enemies3 = ["Possessed Knight", "Evil Mage", "Ghoul"]

# Bosses
boss1 = "Giant"
boss1_hp = 100

boss2 = "Vampire"

boss3 = "Dragon"

player_attack = None
player_hp = 1
enemy_count = 0

# Encounter messages are 9 and 14
messages = ['Select a class from below',
            'You have chosen the knight',
            'You have chosen the archer',
            'You chose to attack!',
            'You chose to Shield Bash!',
            'You chose to use Double Shot!',
            'Are you ready to start the run?',
            'Bold of you to assume you had a choice',
            'ACT 1',
            'You have encountered a ' + str(selected_enemy),
            'The ' + str(selected_enemy) + ' has taken ' + str(player_attack) + ' DMG!',
            'The ' + str(selected_enemy) + ' has dealt ' + str(enemy_attack) + ' DMG!',
            'You have been slain',
            'You have slain the ' + str(selected_enemy),
            'You have encountered a ' + str(selected_enemy),
            'Ability on cooldown for rest of combat',
            'You have encountered a ' + str(boss1),
            'ACT 2',
            'Your stats have increased!',
            'You have encountered a ' + str(boss2),
            'ACT 3',
            'You have encountered a ' + str(boss3),
            'Congratulations, you have beat the game!'
            ]

snip = game_font.render('', True, 'white')
counter = 0
max_counter = len(messages) * 0.1
speed = 3
active_message = 0
message = messages[active_message]
done = False

# Attack
button_width = 150
button_height = 50
button_color = (0, 0, 0)
outline_color = (255, 255, 255)
button_rect = pygame.Rect(150, 200, button_width, button_height)
text = "Attack"
text_color = (207, 0, 0)

# Ability
button_width_2 = 150
button_height_2 = 50
button_color_2 = (0, 0, 0)
outline_color_2 = (255, 255, 255)
button_rect_2 = pygame.Rect(500, 200, button_width_2, button_height_2)
text_2 = "Ability"
text_color_2 = (66, 181, 27)

# Knight
button_width_3 = 150
button_height_3 = 50
button_color_3 = (0, 0, 0)
outline_color_3 = (255, 255, 255)
button_rect_3 = pygame.Rect(325, 390, button_width_3, button_height_3)
text_3 = "Knight"
text_color_3 = (255, 255, 255)
knight = False
sword = random.randint(5, 10)
knight_hp = 100

# Archer
button_width_4 = 150
button_height_4 = 50
button_color_4 = (0, 0, 0)
outline_color_4 = (255, 255, 255)
button_rect_4 = pygame.Rect(500, 390, button_width_4, button_height_4)
text_4 = "Archer"
text_color_4 = (255, 255, 255)
archer = False
archer_hp = 60
bow = random.randint(10, 15)

# Yes
button_width_5 = 150
button_height_5 = 50
button_color_5 = (0, 0, 0)
outline_color_5 = (255, 255, 255)
button_rect_5 = pygame.Rect(450, 425, button_width_4, button_height_4)
text_5 = "Yes"
text_color_5 = (48, 191, 86)

# No
button_width_6 = 150
button_height_6 = 50
button_color_6 = (0, 0, 0)
outline_color_6 = (255, 255, 255)
button_rect_6 = pygame.Rect(625, 425, button_width_4, button_height_4)
text_6 = "No"
text_color_6 = (176, 26, 26)


text_info = game_font.render("Click SPACE to proceed", True, (255, 255, 255))
text_choose = game_font.render("Choose a class:", True, (255, 255, 255))
text_cont = game_font.render("Space", True, (255, 255, 255))
text_enc = game_font.render("Backspace", True, (255, 255, 255))

show_button = True
run = True
hp_show = False
ready = False
message_shown = False
space_prompt = False
space_pressed = False
player_turn = False
attack_message_shown = False
button_active = False
enemy_turn = False
encounter = False
act_1 = True
active_message_11_playing = False
player_dead = False
enemy_dead = False
shield_bash = False
double_shot = False
cooldown = False
enemyhp_show = False
new_enemy = False
attack_valid = False
hint_recieved = False

boss1_spawn = False
boss1_dead = False
boss1_hp = 1
boss1_turn = False
boss1_attack = random.randint(10, 15)

boss2_spawn = False
boss2_dead = False
boss2_hp = 20
boss2_turn = False
boss2_attack = random.randint(15, 20)

boss3_spawn = False
boss3_dead = False
boss3_turn = False

act_2 = False
test_flag = False
hp_info_prompt = False
flicker_fix = False
knight_upgrade = False
knight_upgrade2 = False
archer_upgrade = False
archer_upgrade2 = False
enemies_set2 = False
enemies_set3 = False
act2_boss = False
act_3 = False
no_stat = False
act_3_gameloop = False
end_game = False
attack_invalid = False

def generate_attack_message(player_attack):
    return "The " + str(selected_enemy) + " has taken " + str(player_attack) + " DMG!"

def enemy_generate_attack_message(enemy_attack):
    return "The " + str(selected_enemy) + " has dealt " + str(enemy_attack) + " DMG!"

def boss1_generate_attack_message(boss1_atttack):
    return "The Giant has dealt " + str(boss1_atttack) + " DMG!"

def new_encounter(selected_enemy):
    return "You have encountered a " + str(selected_enemy)
    enemy_count += 1

def new_boss(boss2_spawn):
    return "You have encountered a " + str(boss2)
    enemy_count += 1

def enemy_slain(selected_enemy):
    return "You have slain the " + str(selected_enemy)

def is_message_complete(counter, message_length, speed):
    return counter >= speed * message_length

while run:
    screen.fill('dark grey')
    timer.tick(60)
    pygame.draw.rect(screen, 'black', [0, 0, 800, 500])
    pygame.display.set_caption('Pygame RPG')

    if counter < speed * len(message):
        counter += 1
    elif counter >= speed * len(message):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if not ready and not message_shown:

            if event.type == pygame.MOUSEBUTTONDOWN:

                if button_rect_3.collidepoint(event.pos) and not knight and not archer:
                    active_message = 1
                    message = messages[active_message]
                    counter = 0
                    show_button = False
                    print("You chose the knight")
                    player_hp =+ knight_hp
                    hp_show = True
                    knight = True
                    text_2 = "Shield Bash"
                    button_width_2 = 225
                    button_height_2 = 50
                    button_rect_2 = pygame.Rect(485, 200, button_width_2, button_height_2)
                    ready = True
                    space_prompt = True

                if button_rect_4.collidepoint(event.pos) and not archer and not knight:
                    active_message = 2
                    message = messages[active_message]
                    counter = 0
                    show_button = False
                    player_hp =+ archer_hp
                    hp_show = True
                    archer = True
                    text_2 = "Double Shot"
                    button_width_2 = 200
                    button_height_2 = 50
                    button_rect_2 = pygame.Rect(492, 200, button_width_2, button_height_2)
                    print("You chose the archer")
                    ready = True
                    space_prompt = True

        # Asks player if they want to start the run, ready is a trigger for this indicating that the class has been chosen.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not message_shown and ready:
                active_message = 6
                done = False
                space_prompt = False
                message = messages[active_message]
                counter = 0
                message_shown = True

        # After yes or no prompt, ready becomes false as a trigger for the transition to message to work.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect_5.collidepoint(event.pos) and button_active:
                active_message = 8
                message = messages[active_message]
                counter = 0
                message_shown = False
                ready = False
                space_prompt = True
                button_active = False

            elif button_rect_6.collidepoint(event.pos) and button_active:
                active_message = 7
                message = messages[active_message]
                counter = 0
                message_shown = False
                ready = False
                space_prompt = True
                button_active = False

        if event.type == pygame.KEYDOWN and not ready and act_1:
            if event.key == pygame.K_SPACE and knight or archer:
                active_message = 8
                message = messages[active_message]
                counter = 0

        if event.type == pygame.KEYDOWN and not ready and not encounter:
            if event.key == pygame.K_SPACE and knight or archer:
                active_message = 9
                message = messages[active_message]
                counter = 0
                enemy_count += 1
                print("Enemy count is " + str(enemy_count))
                space_prompt = False
                player_turn = True
                enemy_turn = False
                encounter = True
                act_1 = False
                enemyhp_show = True

            # Attacks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and knight and player_turn and not enemy_turn and not attack_invalid:
                # You chose to attack message
                active_message = 3
                message = messages[active_message]
                counter = 0
                space_prompt = True
                attack_message_shown = True
                player_turn = False
                enemy_turn = True
                act_1 = False
                attack_valid = True

            if button_rect.collidepoint(event.pos) and archer and player_turn and not enemy_turn and not attack_invalid:
                active_message = 3
                message = messages[active_message]
                counter = 0
                space_prompt = True
                attack_message_shown = True
                player_turn = False
                enemy_turn = True
                act_1 = False
                attack_valid = True

        if event.type == pygame.KEYDOWN:
            if space_prompt and attack_message_shown and attack_valid and not new_enemy:
                if event.key == pygame.K_SPACE:
                    # Display message for damage dealt to enemy
                    if knight and not knight_upgrade:
                        player_attack = random.randint(5, 10)
                    if knight_upgrade and knight:
                        player_attack = random.randint(10, 15)
                    if knight_upgrade2 and knight:
                        player_attack = random.randint(15, 20)
                    if archer and not archer_upgrade:
                        player_attack = random.randint(10, 15)
                    if archer_upgrade and archer:
                        player_attack = random.randint(15, 20)
                    if archer_upgrade2 and archer:
                        player_attack = random.randint(20, 25)

                    enemyhp -= player_attack
                    print("The enemy hp is " + str(enemyhp))

                    messages[10] = generate_attack_message(player_attack)
                    active_message = 10
                    message = messages[active_message]
                    counter = 0
                    attack_message_shown = False
                    space_prompt = True
                    enemy_turn = True
                    player_turn = False

            elif enemy_turn and enemyhp > 0:
                if event.key == pygame.K_SPACE:
                    # Display message for enemy's attack
                    if selected_enemy == "Dire Wolf":
                        enemy_attack = random.randint(7, 9)
                    elif selected_enemy == "Goblin":
                        enemy_attack = random.randint(5, 8)
                    elif selected_enemy == "Bandit":
                        enemy_attack = random.randint(6, 7)
                    if selected_enemy == "Skeleton":
                        enemy_attack = random.randint(8, 12)
                    elif selected_enemy == "Zombie":
                        enemy_attack = random.randint(9, 11)
                    elif selected_enemy == "Banshee":
                        enemy_attack = random.randint(10,15)
                    if selected_enemy == "Possessed Knight":
                        enemy_attack = random.randint(15, 20)
                    elif selected_enemy == "Evil Mage":
                        enemy_attack = random.randint(18, 23)
                    elif selected_enemy == "Ghoul":
                        enemy_attack = random.randint(20, 23)

                    messages[11] = enemy_generate_attack_message(enemy_attack)
                    player_hp -= enemy_attack
                    active_message = 11
                    message = messages[active_message]
                    counter = 0
                    space_prompt = False
                    enemy_turn = False
                    player_turn = True
                    if player_hp < 1:
                        player_dead = True
                        space_prompt = True

            if enemyhp < 1 and not new_enemy:
                enemy_dead = True
                enemy_attack = 0
                active_message = 10
                attack_message_shown = True
                message = messages[active_message]
                counter = 0
                space_prompt = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and attack_message_shown and not new_enemy and active_message == 10:
                        messages[13] = enemy_slain(selected_enemy)
                        active_message = 13
                        message = messages[active_message]
                        counter = 0
                        attack_message_shown = False
                        new_enemy = True
                        space_prompt = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and new_enemy and not boss1_spawn and not boss2_spawn and not boss3_spawn and enemies:

                    selected_enemy = random.choice(enemies)
                    if selected_enemy == "Dire Wolf":
                        enemyhp = 30
                    elif selected_enemy == "Goblin":
                        enemyhp = 20
                    elif selected_enemy == "Bandit":
                        enemyhp = 25

                    if enemies_set2:
                        selected_enemy = random.choice(enemies2)

                    if selected_enemy == "Skeleton":
                        enemyhp = 25
                    elif selected_enemy == "Zombie":
                        enemyhp = 35
                    elif selected_enemy == "Banshee":
                        enemyhp = 40

                    if enemies_set3:
                        selected_enemy = random.choice(enemies3)

                    if selected_enemy == "Possessed Knight":
                        enemyhp = 45
                    elif selected_enemy == "Evil Mage":
                        enemyhp = 50
                    elif selected_enemy == "Ghoul":
                        enemyhp = 40

                    enemyhp_show = True
                    cooldown = False
                    messages[14] = new_encounter(selected_enemy)
                    active_message = 14
                    message = messages[active_message]
                    enemy_count += 1
                    print("Enemy count is " + str(enemy_count))
                    counter = 0
                    new_enemy = False
                    space_prompt = False
                    player_turn = True
                    enemy_turn = False

        # Abilities
        #Shield bash
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect_2.collidepoint(event.pos) and knight and player_turn and not cooldown and not attack_invalid:
                active_message = 4
                message = messages[active_message]
                counter = 0
                shield_bash = True
                space_prompt = True
                player_turn = False


            if button_rect_2.collidepoint(event.pos) and cooldown and player_turn:
                active_message = 15
                message = messages[active_message]
                counter = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if shield_bash and space_prompt:
                    shield_bash = False
                    player_turn = False
                    enemy_turn = True
                    cooldown = True
                    space_prompt = True
                    if knight and not knight_upgrade:
                        player_attack = random.randint(10, 20)
                    if knight and knight_upgrade:
                        player_attack = random.randint(20, 25)
                    if knight_upgrade2 and knight:
                        player_attack = random.randint(25, 30)
                    messages[10] = generate_attack_message(player_attack)
                    enemyhp -= player_attack

                    active_message = 10
                    message = messages[active_message]
                    counter = 0

        # Double shot
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect_2.collidepoint(event.pos) and archer and player_turn and not cooldown and not attack_invalid:
                active_message = 5
                message = messages[active_message]
                counter = 0
                double_shot = True
                space_prompt = True
                player_turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if double_shot and space_prompt:
                    player_turn = False
                    enemy_turn = True
                    double_shot = False
                    cooldown = True
                    space_prompt = True
                    if archer and not archer_upgrade:
                        player_attack = random.randint(15, 25)
                    if archer and archer_upgrade:
                        player_attack = random.randint(20, 30)
                    if archer and archer_upgrade2:
                        player_attack = random.randint(30, 35)
                    messages[10] = generate_attack_message(player_attack)
                    enemyhp -= player_attack

                    active_message = 10
                    message = messages[active_message]
                    counter = 0

        if enemyhp < 1 and not new_enemy:
            enemy_dead = True
            enemy_attack = 0
            attack_message_shown = True
            space_prompt = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and attack_message_shown and not new_enemy:
                    messages[13] = enemy_slain(selected_enemy)
                    active_message = 13
                    message = messages[active_message]
                    counter = 0
                    attack_message_shown = False
                    new_enemy = True
                    space_prompt = False

        # Boss 1
        if enemy_count == 3 and enemyhp < 1:
            boss1_spawn = True
            enemy_turn = False
            cooldown = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if enemy_count == 3 and active_message == 13 and enemyhp < 1 and boss1_spawn:
                    active_message = 16
                    message = messages[active_message]
                    counter = 0
                    selected_enemy = "Giant"
                    new_enemy = False
                    enemyhp = 50  # CHANGE VALUE LATER
                    enemyhp_show = True
                    player_turn = True
                    enemy_turn = False
                    test_flag = True
                if boss1_spawn:
                    enemy_attack = random.randint(10, 15)
                    messages[11] = enemy_generate_attack_message(enemy_attack)
                    counter = 0

        if enemyhp < 1 and boss1_spawn and test_flag:
            act_2 = True
            boss1_dead = True
            boss1_spawn = False
            space_prompt = False
            new_enemy = True
            test_flag = False

        # ACT 2
        if act_2 and boss1_dead and not flicker_fix and not no_stat:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    active_message = 17
                    message = messages[active_message]
                    counter = 0
                    enemyhp_show = False
                    enemyhp = 2
                    space_prompt = True
                    enemy_text_hp = False
                    enemies_set2 = True
                    boss1_dead = False
                    no_stat = True
                    attack_invalid = True
                    print("The no stat is ")

        # Player upgrade handling
        if event.type == pygame.KEYDOWN and act_2 and active_message == 17:
            if event.key == pygame.K_SPACE:
                active_message = 18
                message = messages[active_message]
                counter = 0
                flicker_fix = True
                boss1_spawn = False
                boss1_dead = False
                boss1_turn = False
                new_enemy = True
                attack_invalid = False
                if knight:
                    player_hp = 125
                    knight_upgrade = True
                elif archer:
                    player_hp = 70
                    archer_upgrade = True

        if enemy_count == 7 and enemyhp < 1:
            boss2_spawn = True
            enemy_turn = False
            cooldown = False
            flicker_fix = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if enemy_count == 7 and active_message == 13 and enemyhp < 1 and boss2_spawn:
                    print("Boss work")
                    no_stat = True
                    selected_enemy = "Vampire"
                    messages[19] = new_encounter(selected_enemy)
                    active_message = 19
                    message = messages[active_message]
                    enemy_count += 1
                    print("The enemy count is " + str(enemy_count))
                    counter = 0
                    new_enemy = False
                    enemyhp = 65
                    print(enemyhp)
                    enemyhp_show = True
                    player_turn = True
                    enemy_turn = False
                    test_flag = True
                    act_3 = True
                if boss2_spawn:
                    enemy_attack = random.randint(15, 20)
                    messages[11] = enemy_generate_attack_message(enemy_attack)
                    counter = 0

                    print("The boss2 spawn is " + str(boss2_spawn))

        # Check if the boss is dead
        if active_message == 13 and boss2_spawn and test_flag and enemy_count == 8:
            print("The boss 2 has died")
            act_3 = True
            print("test")
            boss2_dead = True
            boss2_spawn = False
            space_prompt = False
            new_enemy = True
            test_flag = False

        # ACT 3
        if boss2_dead and act_3:
            print("act 3 work")
            space_prompt = True
        if event.type == pygame.KEYDOWN and act_3 and space_prompt and not act_3_gameloop:
            if event.key == pygame.K_BACKSPACE:
                print("message displayed")
                active_message = 20
                message = messages[active_message]
                counter = 0
                enemyhp_show = False
                enemyhp = 2
                space_prompt = True
                enemy_text_hp = False
                enemies_set3 = True
                attack_invalid = True

                boss2_dead = False
                boss2_spawn = False
                boss2_turn = False

                no_stat = True
                act_3_gameloop = True

        # Player upgrade handling
        if event.type == pygame.KEYDOWN and act_3 and active_message == 20:
            if event.key == pygame.K_SPACE:
                active_message = 18
                message = messages[active_message]
                counter = 0
                attack_invalid = False
                flicker_fix = True
                boss2_spawn = False
                new_enemy = True
                if knight:
                    player_hp = 150
                    knight_upgrade = False
                    knight_upgrade2 = True
                elif archer:
                    player_hp = 100
                    archer_upgrade = False
                    archer_upgrade2 = True


        if enemy_count == 13 and enemyhp < 1:
            boss3_spawn = True
            enemy_turn = False
            cooldown = False
            flicker_fix = False

        # Boss 3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if enemy_count == 13 and active_message == 13 and enemyhp < 1 and boss3_spawn:
                    print("Boss 3 work")
                    no_stat = True
                    selected_enemy = "Dragon"
                    messages[21] = new_encounter(selected_enemy)
                    active_message = 21
                    message = messages[active_message]
                    enemy_count += 1
                    print("The enemy count is " + str(enemy_count))
                    counter = 0
                    new_enemy = False
                    enemyhp = 99
                    print(enemyhp)
                    enemyhp_show = True
                    player_turn = True
                    enemy_turn = False
                    test_flag = True
                    # Maybe add flag later for ending
                if boss3_spawn:
                    enemy_attack = random.randint(20, 25)
                    messages[11] = enemy_generate_attack_message(enemy_attack)
                    counter = 0
                    print("The boss3 spawn is " + str(boss3_spawn))

        if active_message == 13 and boss3_spawn and test_flag and enemy_count == 14:
            print("The boss 3 has died")
            print("test")
            boss3_dead = True
            boss3_spawn = False
            space_prompt = False
            new_enemy = True
            test_flag = False

        if boss3_dead and active_message == 13:
            print("close")
            enemies_set2 = False
            enemies_set3 = False
            enemies = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    active_message = 22
                    message = messages[active_message]
                    counter = 0
                    end_game = True
                    new_enemy = False
                    enemyhp = 2
                    enemyhp_show = False
                    hp_show = False




        # Spacekey handling and hint prompt
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not hint_recieved and knight or archer:
                hint_recieved = True

            if event.key == pygame.K_SPACE and not hp_info_prompt and knight or archer:
                hp_info_prompt = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not active_message_11_playing and player_hp < 1 and active_message != 12 and counter >= speed * len(message):
                    active_message = 12
                    message = messages[active_message]
                    counter = 0
                    space_prompt = False
                    knight = False
                    archer = False
                    act_1 = False

    if space_prompt:
        text_cont = game_font.render("> SPACE", True, (255, 255, 255))
        screen.blit(text_cont, (625, 425))
        space_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space_prompt = False
                    space_pressed = True

        if space_pressed:
            continue

    if new_enemy:
        space_prompt = False
        text_enc = game_font.render("> BACKSPACE", True, (255, 255, 255))
        screen.blit(text_enc, (560, 425))

    if ready and not hint_recieved:
        text_info = game_font.render("Click SPACE to continue", True, (255, 222, 38))
        screen.blit(text_info, (425, 350))

    if ready and not hp_info_prompt:
        test_infohp = game_font.render("Player Vitality", True, (255, 222, 38))
        screen.blit(test_infohp, (50, 350))



    if message_shown:
        button_active = True
        # Yes
        pygame.draw.rect(screen, button_color_5, button_rect_5)
        pygame.draw.rect(screen, outline_color_5, button_rect_5, 3)
        text_surface_5 = game_font.render(text_5, True, text_color_5)
        text_rect_5 = text_surface_5.get_rect(center=button_rect_5.center)
        text_rect_5.y += 5
        screen.blit(text_surface_5, text_rect_5)

        # No
        pygame.draw.rect(screen, button_color_6, button_rect_6)
        pygame.draw.rect(screen, outline_color_6, button_rect_6, 3)
        text_surface_6 = game_font.render(text_6, True, text_color_6)
        text_rect_6 = text_surface_6.get_rect(center=button_rect_6.center)
        text_rect_6.y += 5
        screen.blit(text_surface_6, text_rect_6)

    # Player HP handling
    if hp_show:
        text_hp = game_font.render("HP: " + str(player_hp), True, (73, 209, 27)) # Default Green
        screen.blit(text_hp, (50, 425))
    if player_hp < 71 and hp_show and knight:
        text_hp = game_font.render("HP: " + str(player_hp), True, (242, 221, 29)) # Yellow
        screen.blit(text_hp, (50, 425))
    if player_hp < 31 and hp_show and knight:
        text_hp = game_font.render("HP: " + str(player_hp), True, (207, 0, 0)) # Red
        screen.blit(text_hp, (50, 425))
    if player_hp < 41 and hp_show and archer:
        text_hp = game_font.render("HP: " + str(player_hp), True, (242, 221, 29))  # Yellow
        screen.blit(text_hp, (50, 425))
    if player_hp < 26 and hp_show and archer:
        text_hp = game_font.render("HP: " + str(player_hp), True, (207, 0, 0))  # Red
        screen.blit(text_hp, (50, 425))


    if enemyhp_show:
        enemy_text_hp = game_font.render("HP: " + str(enemyhp), True, (214, 4, 4))
        screen.blit(enemy_text_hp, (350, 130))
    if enemyhp < 1:
        enemy_text_hp = game_font.render("SLAIN", True, (214, 4, 4))
        screen.blit(enemy_text_hp, (350, 130))
        enemyhp_show = False
        space_prompt = False
    if player_dead:
        hp_show = False
        text_php = game_font.render("SLAIN", True, (206, 48, 209))
        screen.blit(text_php, (50, 425))
        enemyhp_show = False

    if not player_dead and not end_game:
        # Attack button
        pygame.draw.rect(screen, button_color, button_rect)
        pygame.draw.rect(screen, outline_color, button_rect, 3)  # Thickness of 3 pixels
        text_surface = game_font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        text_rect.y += 5
        screen.blit(text_surface, text_rect)


        # Ability button
        pygame.draw.rect(screen, button_color_2, button_rect_2)
        pygame.draw.rect(screen, outline_color_2, button_rect_2, 3)  # Thickness of 3 pixels
        text_surface_2 = game_font.render(text_2, True, text_color_2)
        text_rect_2 = text_surface_2.get_rect(center=button_rect_2.center)
        text_rect_2.y += 5
        screen.blit(text_surface_2, text_rect_2)


    if show_button:
        # Classes

        # Knight
        pygame.draw.rect(screen, button_color_3, button_rect_3)
        pygame.draw.rect(screen, outline_color_3, button_rect_3, 3)  # Thickness of 3 pixels
        text_surface_3 = game_font.render(text_3, True, text_color_3)
        text_rect_3 = text_surface_3.get_rect(center=button_rect_3.center)
        text_rect_3.y += 5
        screen.blit(text_surface_3, text_rect_3)

        screen.blit(text_choose, (50, 400))

        # Archer
        pygame.draw.rect(screen, button_color_4, button_rect_4)
        pygame.draw.rect(screen, outline_color_4, button_rect_4, 3)  # Thickness of 3 pixels
        text_surface_4 = game_font.render(text_4, True, text_color_4)
        text_rect_4 = text_surface_4.get_rect(center=button_rect_4.center)
        text_rect_4.y += 5
        screen.blit(text_surface_4, text_rect_4)

    snip = game_font.render(message[0:counter//speed], True, 'white')
    text_rect = snip.get_rect(center=(screen.get_width() // 2, 100))
    screen.blit(snip, text_rect)

    pygame.display.flip()


pygame.quit()
