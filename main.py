#main file for the project
#main will contain the main game logic
#main will call the other files and classes to run the game

import pygame
# import menu # import menu.py file, currently disabled

# create pygame window  and set title
pygame.init()

# set up the drawing window
Width, Height = 1000, 700 # updated size
screen = pygame.display.set_mode([Width, Height])

#title of the gaame for screen 
pygame.display.set_caption("Checkers+")  


'''
# Load background music (replace with the actual music file path)
pygame.mixer.music.load("music_file.mp3")

# Play the music indefinitely
pygame.mixer.music.play(-1)

'''

# title for display 
game_title = "Checkers+"
message = "Checkers with a twist! For all ages and skill levels!"

background_image = pygame.image.load("checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))  


title_font = pygame.font.Font(None, 64)
message_font = pygame.font.Font(None, 32)

title_text = title_font.render(game_title, True, (255, 255, 255))
title_rect = title_text.get_rect(center=(Width // 2, 50))

#quick message !!!
message_text = message_font.render(message, True, (255, 255, 255))
message_rect = message_text.get_rect(center=(Width // 2, 120))

# run until the user asks to quit
def main():
    running = True
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN: # potential/future code for button interaction
                # If mouse clicked on PvP button
                #if pvp_button().collidepoint(event.pos):
                   # start game

        #image of the background
        screen.blit(background_image, (0, 0))

        #tile the background
        screen.blit(title_text, title_rect)
        screen.blit(message_text, message_rect)
        
        # call PvP button function from menu.py
        menu_buttons()

        # flip the display
        pygame.display.flip()

    # done! time to quit
    pygame.quit()

# function to create menu buttons
# currently supports PvP and settings buttons
def menu_buttons():
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

    return button_rect, button_rect_2


main()