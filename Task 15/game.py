# Taks 15 game.py


import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1440
screen_height = 1050
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates a backround image

back_image = pygame.image.load("pTns7.png")

# This creates the player and gives it the image found in this folder (similarly with the enemy, enemy2 & enemy3 image). 

player = pygame.image.load("6_enemies_1_attack_000.png")

enemy = pygame.image.load("2_enemies_1_attack_002.png")

enemy2 = pygame.image.load("5_enemies_1_attack_001.png")

enemy3 = pygame.image.load("10_enemies_1_attack_001.png")

gem = pygame.image.load("13.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
back_image_Height = back_image.get_height()

image_height = 269
image_width = 150

enemy_height = 250
enemy_width = 200

enemy2_height = 250
enemy2_width = 200

enemy3_height = 250 
enemy3_width = 200

gem_height  = 250
gem_width = 200

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

print("This is the height of the enemy 1: ") +str(enemy_height)
print("This is the Width of the enemy 1: ") +str(enemy_width)

print("This is the height of the enemy 2: ") +str(enemy2_height)
print("This is the widht of the enemy 2: ") +str(enemy2_width)

print("This is the height of the enemy 2: ") +str(enemy2_height)
print("This is the widht of the enemy 3: ") +str(enemy3_width)

# Stores background image position

back_imageXPosition = 0
back_imageYPosition = 0

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make enemy, enemy2 and enemy3 start off screen and at a random y position.

enemyXPosition =  1300
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy2XPosition =  1900
enemy2YPosition =  random.randint(0, screen_height - enemy_height)

enemy3XPosition = 2500
enemy3YPosition =  random.randint(0, screen_height - enemy_height)

gemXPosition = 2900
gemYPosition = random.randint(0, screen_height - gem_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyLeft = False
KeyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 2: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.

    # Background Image added each time to fill screen

    screen.blit(back_image,(back_imageXPosition, back_imageYPosition)) #
    screen.blit(back_image,(0, 500))
    screen.blit(back_image,(500, 0))
    screen.blit(back_image,(500, 500))
    screen.blit(back_image,(1000, 500))
    screen.blit(back_image,(1000, 0))

    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    
    screen.blit(enemy2,(enemy2XPosition, enemy2YPosition))
    
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    
    screen.blit(gem,(gemXPosition, gemYPosition))

    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                KeyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                KeyRight = False
            
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 7
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 7
    if keyLeft == True: # This makes the user not move off the screen on the left
        if playerXPosition > 0:
            playerXPosition -= 7
    if KeyRight == True < screen_width - image_width: # this makes sure the user does not move of the screen on the right
        playerXPosition += 7
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect()) or pygame.Rect(enemy2.get_rect()) or pygame.Rect(enemy3.get_rect())
    enemyBox.top = enemyYPosition or enemy2YPosition or enemy3YPosition
    enemyBox.left = enemyXPosition or enemy2XPosition or enemy3XPosition
    

    # Prize Gem Box

    gemBox = pygame.Rect(gem.get_rect())
    gemBox.top = gemYPosition 
    gemBox.left = gemXPosition

    # Test player against Gem Colision of Box

    if playerBox.colliderect(gemBox):
        print("You got a Prize Gem!")

        pygame.quit()

        exit(0)

    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0) 
    
    # Make enemy approach the player.
    
    enemyXPosition -= 10
    enemy2XPosition -= 10
    enemy3XPosition -= 10
    gemXPosition -= 10
    
    # ================The game loop logic ends here. =============
  
