import pygame
import random
from pygame import mixer

pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Creating Boolean variable to keep the game running
isRunning = True

# To add title and icon to our game window we will write the following code before the game loop.

# Title
pygame.display.set_caption('Protect the CEO')

# Icon
icon = pygame.image.load('man.png')  # Here we are loading the man image from our resource.
pygame.display.set_icon(icon)  # Setting the icon on the game window.

# Creating CEO
ceo = pygame.image.load('man.png')

# Loading the block image
block = pygame.image.load("block.png")
# Variable containing the X and Y value of the block
blockX = 300  # After adjusting the image accordingly in the center
blockY = 375  # Above the CEO's image
# Variable containing the change of the value that happend in blockX
changeX = 0

# Loading the image of the girl.
girlOne = pygame.image.load('girl (1).png')
# For Random start position.
girlOneX = random.randint(0, 10)
girlOneY = 100
Xchange = 0.5
Ychange = 0.5

# Adding Score
score = 0  # Variable that contains score
# Creating the font
font = pygame.font.Font('freesansbold.ttf', 24)


def displayScore(score):
    # Creating score image by rendering the font
    scoreImage = font.render(str(score), True, (255, 255, 255))
    # Displaying it on the top left corner of our game window
    screen.blit(scoreImage, (10, 10))


def game_over():
    gfont = pygame.font.Font('freesansbold.ttf', 45)
    game = gfont.render("Game Over!", True, (255, 255, 255))
    screen.blit(game, (275, 275))


# We will create a game over variable
isGameOver = False

# Background Sound
# Loading the background music.
background = mixer.music.load('background.wav')  # The name of my music file is background.wav
mixer.music.play(-1)  # We use -1 to tell the mixer to play this music on repeat. It's like a code for it.

# Creating the game loop
while (isRunning):
    # For colour, we will write
    screen.fill((69, 68, 65))  # It's a grayish colour
    # Checking all the events that are happening on our screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        # Inside the for-loop, that loops over all the events
        if event.type == pygame.KEYDOWN:  # This runs, when a key is pressed
            if event.key == pygame.K_LEFT:  # This checks if the keypress was of the left arrow key
                changeX -= 3  # To change the positon in left direction
            if event.key == pygame.K_RIGHT:  # This checks if the keypress was of the right arrow key
                changeX += 3  # To change the positon in left direction

        if event.type == pygame.KEYUP:  # This runs when a key is released after press
            changeX = 0

    # This will run after the for-loop
    # The following statement is to check if the block is touching the boundaries, if yes then stop immediately because we don't want our block to move outside the game screen.
    if blockX + changeX >= 546 or blockX + changeX < 0:
        # If it touches the boundaries then change the changeX to 0. This will stop the change to happen to the block.
        changeX = 0
    else:
        blockX += changeX

    # All of this code is written inside the game loop after the for-loop of events

    # This will change the position of the girl, everytime the loop executes
    girlOneX += Xchange
    girlOneY += Ychange
    # This will check if the girl is touching any boundaries except the bottom one.
    if (girlOneX < 0):
        Xchange = 1
    elif girlOneX > 750:  # After adjusting the maximum X value of girl in horizontal direction
        Xchange = -1  # This changes the movement of girl in opposite direction
    elif girlOneY < 0:
        Ychange *= -1  # This changes the movement of girl in opposite direction

    if girlOneY >= 480:  # This checks if the girl has reached around the CEO
        # Right now, for reference. We will print the Game Over
        # print("Game Over")
        isGameOver = True
    elif girlOneX > (blockX + changeX) and girlOneX < (
            blockX + changeX + 254) and girlOneY >= 425:  # To check if the girl has touched the block
        Ychange *= -1
        # Increasing the score
        score += 1
        # Let's play the laser sound effect
        sound = mixer.Sound('laser.wav')
        sound.play()

    displayScore(score)
    if (isGameOver):
        game_over()
    else:
        # Now let's do, screen.blit()
        screen.blit(girlOne, (girlOneX, girlOneY))
        screen.blit(block, (blockX, blockY))
        # We use screen.blit() to place our image inside our game window
        screen.blit(ceo,
                    (375, 540))  # After adjusting, I found this coordinate to set our CEO in the very Bottom-Center.

    # And to Update, we will write the following code in the very end of the game loop.
    pygame.display.update()
