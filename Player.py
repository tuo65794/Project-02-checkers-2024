import pygame
Width, Height = 1000, 700
background_image = pygame.image.load("checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))
screen = pygame.display.set_mode([Width, Height])

# Global map for user scores
user_scores = {}

class Player:
    
    def __init__(self, username):
        self.username = username
        self.win = 0
        
    # Function to draw the text input box on the screen
    def draw_text_input(self, player_name, error_msg="name error"):
        font = pygame.font.Font(None, 32)

        # Render the background box
        pygame.draw.rect(screen, (128, 128, 128), (Width // 2 - 225, Height // 2 - 25, 450, 50))  # Adjust size and position as needed

        # Render the text on the background box
        input_text = font.render("Enter Your Name: " + player_name, True, (255, 255, 255))
        input_rect = input_text.get_rect(center=(Width // 2, Height // 2))
        screen.blit(input_text, input_rect)

        # Render the error message below the input box
        if error_msg:
            error_font = pygame.font.Font(None, 24)
            error_text = error_font.render(error_msg, True, (255, 0, 0))  # Red color for error message
            error_rect = error_text.get_rect(center=(Width // 2, Height // 2 + 30))  # Adjust position as needed
            screen.blit(error_text, error_rect)


    # Function to ask player's name
    def get_player_name(self):
        input_active = True
        player_name = ""
        error_msg = ""

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #if player_name.isalnum() and len(player_name) <= 20:
                        if (event.unicode.isalnum() or event.unicode.isspace()) and len(player_name) < 20:

                            input_active = False  # Stop taking input when Enter is pressed and the name is valid
                        else:
                            error_msg = "Invalid name. Please use English letters or numbers, and keep it under 20 characters."
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]  # Remove the last character when Backspace is pressed
                    else:
                        # Check if the typed character is an English letter, a number, or a space
                        if (event.unicode.isalnum() or event.unicode.isspace()) and len(player_name) < 20:
                            player_name += event.unicode  # Append the typed character to the player_name



            screen.blit(background_image, (0, 0))
            self.draw_text_input(player_name, error_msg)
            pygame.display.flip()
            
        self.username = player_name

        return player_name

    def add_user(self, username):
            global user_scores  # Use the global keyword to indicate that you're modifying the global variable
            # Check if the username already exists in the hashmap
            if username not in user_scores:
                # If not, add the username with a default score of 0
                user_scores[username] = 0
                print(f"User {username} added with a default score of 0.")
            else:
                print(f"User {username} already exists.")

    # Function to update scores
    def update_scores(player):
        if player.username in user_scores:
            if(player.win == 1):
                user_scores[player.username] += 50
            elif(player.win == 0):   
                user_scores[player.username] -= 50
        
    def update_win(player):
        player.win = 1

    def update_loss(player):
        player.win = 0