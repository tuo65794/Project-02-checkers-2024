import pygame

Width, Height = 1000, 700 


class SecondMenu:
    def start_game_menu():
        start_game_screen = pygame.display.set_mode([Width, Height])
        pygame.display.set_caption("Start Game Menu")

        start_game_font = pygame.font.Font(None, 36)
        start_game_text = start_game_font.render("Choose Game Mode", True, (0, 0, 0))  # Black font color
        start_game_rect = start_game_text.get_rect(center=(Width // 2, 50))

        # Set background color
        background_color = (169, 169, 169)  # Light Gray
        start_game_screen.fill(background_color)

        start_game_screen.blit(start_game_text, start_game_rect)

        # Create buttons for different game modes
        pvp_button_rect = pygame.Rect(Width // 2 - 150, Height // 3, 300, 50)
        pvc_button_rect = pygame.Rect(Width // 2 - 150, Height // 3 + 60, 300, 50)
        exit_start_button_rect = pygame.Rect(Width // 2 - 150, Height // 3 + 120, 300, 50)

        button_color = (128, 128, 128)  # Dark Gray
        cursor_color = (100, 100, 100)  # Darker Gray

        pygame.draw.rect(start_game_screen, button_color, pvp_button_rect)
        pygame.draw.rect(start_game_screen, button_color, pvc_button_rect)
        pygame.draw.rect(start_game_screen, button_color, exit_start_button_rect)

        pvp_button_text = start_game_font.render("Player vs Player", True, (0, 0, 0), button_color)  # Black font color, transparent background
        pvc_button_text = start_game_font.render("Player vs Computer", True, (0, 0, 0), button_color)  # Black font color, transparent background
        exit_start_button_text = start_game_font.render("Back", True, (0, 0, 0), button_color)  # Black font color, transparent background

        pvp_button_text_rect = pvp_button_text.get_rect(center=(Width // 2, Height // 3 + 25))
        pvc_button_text_rect = pvc_button_text.get_rect(center=(Width // 2, Height // 3 + 85))
        exit_start_button_text_rect = exit_start_button_text.get_rect(center=(Width // 2, Height // 3 + 145))

        start_game_screen.blit(pvp_button_text, pvp_button_text_rect)
        start_game_screen.blit(pvc_button_text, pvc_button_text_rect)
        start_game_screen.blit(exit_start_button_text, exit_start_button_text_rect)

        mouse = pygame.mouse.get_pos()

        if pvp_button_rect.collidepoint(mouse):
            pygame.draw.rect(start_game_screen, cursor_color, pvp_button_rect)
            if pygame.mouse.get_pressed()[0]:
                # Start Player vs Player game
                print("Starting Player vs Player game...")
        else:
            pygame.draw.rect(start_game_screen, button_color, pvp_button_rect)

        if pvc_button_rect.collidepoint(mouse):
            pygame.draw.rect(start_game_screen, cursor_color, pvc_button_rect)
            if pygame.mouse.get_pressed()[0]:
                # Start Player vs Computer game
                print("Starting Player vs Computer game...")
        else:
            pygame.draw.rect(start_game_screen, button_color, pvc_button_rect)

        if exit_start_button_rect.collidepoint(mouse):
            pygame.draw.rect(start_game_screen, cursor_color, exit_start_button_rect)
            if pygame.mouse.get_pressed()[0]:
                return  # Exit the start game menu
        else:
            pygame.draw.rect(start_game_screen, button_color, exit_start_button_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_start_button_rect.collidepoint(event.pos):  # if exit button is clicked
                        return  # exit start game  and return to menu