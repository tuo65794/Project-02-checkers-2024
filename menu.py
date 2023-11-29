# Contains menu functions for main.py
# Currently NOT BEING USED as having issues with building application with multiple files

import pygame
Width, Height = 1000, 700 # match size from main.py
screen = pygame.display.set_mode([Width, Height])

# function to display menu
def menu_buttons():
    # PvP button
    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2-150, Height // 3-25)
    size = (300, 50)  # width, height
        
    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Start Game Against Player", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3))
    
    # Create button on screen using position and size parameters
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect = pygame.Rect(position, size)
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect) # stay original color if cursor not hovering over

    screen.blit(button_text, button_text_rect)
    
    # Settings Button    
    settings_icon = pygame.image.load('pics/settings_icon.png')

    button_height = 50
    spacing = 10

    position = (Width // 2 - 150, Height // 3 + button_height + spacing)
    size = (300, button_height)  # width, height

    button_text = button_font.render("Settings", True, (255, 255, 255))  # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))

    # Set the desired size for the icon
    icon_size = (45, 45)  # Adjust the size of the icon as needed

    # Draw the icon next to the text with the specified size
    settings_icon_resized = pygame.transform.scale(settings_icon, icon_size)
    settings_icon_rect = settings_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + button_height + spacing + (button_height - icon_size[1]) // 2))

    # Create button on screen using position and size parameters
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Used to indicate if the cursor is hovering over the button. If so, the button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_2 = pygame.Rect(position, size)
    if button_rect_2.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_2)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_2)  # Stay the original color if the cursor is not hovering over

    screen.blit(settings_icon_resized, settings_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    # Tutorial button
    tutorial_icon = pygame.image.load('pics/tutorial_icon.png')

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2-150, Height // 3 + 135)
    size = (300, 50)  # width, height

    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Tutorial", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3+160))
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Draw the icon next to the text with the specified size
    tutorial_icon_resized = pygame.transform.scale(tutorial_icon, icon_size)
    tutorial_icon_rect = tutorial_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + 135 + (button_height - icon_size[1]) // 2))

    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_3 = pygame.Rect(position, size)
    if button_rect_3.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_3)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_3) # stay original color if cursor not hovering over

    screen.blit(tutorial_icon_resized, tutorial_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    return button_rect, button_rect_2, button_rect_3

def tutorial(): # tutorial prompt (subject to change text)
    # load image used in tutorial
    checkers_icon = pygame.image.load('pics/checkersguy_icon.png')
    tutorial_screen = pygame.display.set_mode([Width, Height])
    tutorial_screen.fill((128, 128, 128))

    # First message
    tutorial_font = pygame.font.Font(None, 64)
    tutorial_text = tutorial_font.render("Welcome to Checkers+!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 50))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Second message
    tutorial_font = pygame.font.Font(None, 32)
    tutorial_text = tutorial_font.render("This tutorial should provide you with instructions on how to play and use Checkers+.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 105))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # First paragraph
    tutorial_font = pygame.font.Font(None, 25)
    tutorial_text = tutorial_font.render("There are many features accessible from the Checkers+ main menu. You can start a PvP (player versus player) game,", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 145))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("a PvC (player versus computer) game, and access other features like the settings, leaderboard, and this tutorial!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 170))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("The settings will allow you to turn music on or off, and customize the checkers board to your liking.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 195))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("The leaderboard will show recent match results, displaying who won and loss. These will reset when you quit the app.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 220))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Create icon
    icon_size = (100, 100)
    button_height = 50
    spacing = 10
    checkers_icon_resized = pygame.transform.scale(checkers_icon, icon_size)
    checkers_icon_rect = checkers_icon_resized.get_rect(topleft=(Width // 2 - 150 + 95, Height // 3 + 30 + (button_height - icon_size[1]) // 2))
    screen.blit(checkers_icon_resized, checkers_icon_rect.topleft) 

    # Second paragraph
    tutorial_text = tutorial_font.render("To play Checkers+, standard checkers rules are applied...with a twist!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 365))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("In standard checkers, players can only move a piece diagonally until that piece has reached the last row", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 390))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("of the opposing side. In our game, you will be allowed to move a piece backwards every 45 seconds, even", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 415))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("if that piece has not yet reached the last row. You also only have 15 seconds to make a move, so think fast!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 440))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("Your 45 second timer will not reset until you make a backward move. Don't let them go to waste!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 465))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("When the game starts, you will be asked to enter the names of the players (or player, if playing against the computer).", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 490))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("Doing this will allow your name(s) and outcome to be shown on the leaderboard.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 515))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("By now, you should have a basic understanding of what Checkers+ has to offer. Go give it a try!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 540))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("If you ever need to view this tutorial again, you can access it from the main menu. Have fun!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 565))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Exit button to return back to menu
    exit_button_font = pygame.font.Font(None, 32)
    exit_button_text = exit_button_font.render("Exit Tutorial", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 50))
    pygame.draw.rect(tutorial_screen, (64, 64, 64), exit_button_rect.inflate(20, 10))
    tutorial_screen.blit(exit_button_text, exit_button_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit tutorial button is clicked
                    return  # exit tutorial and return to menu
                