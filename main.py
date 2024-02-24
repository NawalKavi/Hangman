# Importing libraries.
import pygame
import sys

# Initialising and setting up.
pygame.init()
screen = pygame.display.set_mode((1200, 800))  # Creates a window with the dimensions specified.
pygame.display.set_caption("Land of Sus")
clock = pygame.time.Clock()
menuFont = pygame.font.Font("Assets/Fonts/minecraft.ttf", 60)
frameCounter = 0  # Counter for each individual AU frame that will loop through them.
menuActive = True
gameActive = False

# Surfaces.
menuBackground = pygame.Surface((1200, 800))
menuBackground.fill("Dark Gray")
menuText_P = menuFont.render("PLAY", False, "Yellow")  # When the button is being hovered over.
menuText_NP = menuFont.render("PLAY", False, "White")  # When the button is not being hovered over.

# Dictionaries.
auDictionary = {  # Dictionary storing all the frames of each individual Among Us colour.
    "purple": {
        1: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 1.png"), (60, 70)).convert_alpha(),
        2: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 2.png"), (60, 70)).convert_alpha(),
        3: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 3.png"), (60, 70)).convert_alpha(),
        4: pygame.transform.scale(pygame.image.load("Assets/Sprites/Purple/Frame 4.png"), (60, 70)).convert_alpha(),
        "currentFrame": 1  # Starts at the first frame before being cycled through each frame inside the game loop.
    },
    "red": {
        1: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 1.png"), (60, 70)).convert_alpha(),
        2: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 2.png"), (60, 70)).convert_alpha(),
        3: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 3.png"), (60, 70)).convert_alpha(),
        4: pygame.transform.scale(pygame.image.load("Assets/Sprites/Red/Frame 4.png"), (60, 70)).convert_alpha(),
        "currentFrame": 1
    },
    "blue": {
        1: pygame.transform.scale(pygame.image.load("Assets/Sprites/Blue/Frame 1.png"), (60, 70)).convert_alpha(),
        2: pygame.transform.scale(pygame.image.load("Assets/Sprites/Blue/Frame 2.png"), (60, 70)).convert_alpha(),
        3: pygame.transform.scale(pygame.image.load("Assets/Sprites/Blue/Frame 3.png"), (60, 70)).convert_alpha(),
        4: pygame.transform.scale(pygame.image.load("Assets/Sprites/Blue/Frame 4.png"), (60, 70)).convert_alpha(),
        "currentFrame": 1
    },
    "orange": {
        1: pygame.transform.scale(pygame.image.load("Assets/Sprites/Orange/Frame 1.png"), (60, 70)).convert_alpha(),
        2: pygame.transform.scale(pygame.image.load("Assets/Sprites/Orange/Frame 2.png"), (60, 70)).convert_alpha(),
        3: pygame.transform.scale(pygame.image.load("Assets/Sprites/Orange/Frame 3.png"), (60, 70)).convert_alpha(),
        4: pygame.transform.scale(pygame.image.load("Assets/Sprites/Orange/Frame 4.png"), (60, 70)).convert_alpha(),
        "currentFrame": 1
    }
}

imageDictionary = {
	"ground": pygame.transform.scale(pygame.image.load("Assets/Images/Ground.png"), (2400, 1600)).convert_alpha()
}


# Positions.
menuText_xPos = 600
menuText_yPos = 200
settingsCog_xPos = 1150
settingsCog_yPos = 100
ground_xPos = 600
ground_yPos = 400

# AU Positions.
purpleAU_xPos = -70
purpleAU_yPos = 700
redAU_xPos = -310
redAU_yPos = 700
blueAU_xPos = -190
blueAU_yPos = 705
orangeAU_xPos = 600
orangeAU_yPos = 400

# AU rectangles.
purpleAU_rect = auDictionary["purple"][1].get_rect(midbottom=(purpleAU_xPos, purpleAU_yPos))
redAU_rect = auDictionary["red"][1].get_rect(midbottom=(redAU_xPos, redAU_yPos))
blueAU_rect = auDictionary["blue"][1].get_rect(midbottom=(blueAU_xPos, blueAU_yPos))
orangeAU_rect = auDictionary["orange"][1].get_rect(midbottom=(orangeAU_xPos, orangeAU_yPos))

# Other rectangles.
ground_rect = imageDictionary["ground"].get_rect(center = (ground_xPos, ground_yPos))
menuText_rect = menuText_NP.get_rect(center=(menuText_xPos, menuText_yPos))  # Having the menu text as a rectangle to make interactions with it and drawing it easier.

# Game loop.
while True:

    for event in pygame.event.get():  # Retrieves all events running.
        if event.type == pygame.QUIT:  # Checks if the current event is the same as the quit button of a window.
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and menuText_rect.collidepoint(mousePos):  # Checks if the user has pressed play in the menu.
            menuActive = False
            gameActive = True

    # Menu screen.
    if menuActive:

        screen.blit(menuBackground, (0, 0))  # Menu text blitting.
        pygame.draw.rect(screen, "Dark Gray", menuText_rect)
        screen.blit(menuText_NP, menuText_rect)
        mousePos = pygame.mouse.get_pos()  # Gets the current position of the mouse pointer inside the screen.
        if menuText_rect.collidepoint(
                mousePos):  # Returns either True or False depending on whether the mouse pointer is colliding with the menu text.
            pygame.draw.rect(screen, "Dark Gray", menuText_rect)
            screen.blit(menuText_P, menuText_rect)

        purpleAU_rect.left += 2  # Purple blitting.
        if purpleAU_rect.left > 1200:
            purpleAU_rect.left = -70
        screen.blit(auDictionary["purple"][auDictionary["purple"]["currentFrame"]], purpleAU_rect)

        redAU_rect.left += 2  # Red blitting.
        if redAU_rect.left > 1200:
            redAU_rect.left = -70
        screen.blit(auDictionary["red"][auDictionary["red"]["currentFrame"]], redAU_rect)

        blueAU_rect.left += 2  # Blue blitting.
        if blueAU_rect.left > 1200:
            blueAU_rect.left = -70
        screen.blit(auDictionary["blue"][auDictionary["blue"]["currentFrame"]], blueAU_rect)

    # Game screen.
    if gameActive:
        screen.fill("Blue")
        screen.blit(imageDictionary["ground"], ground_rect)
        screen.blit(auDictionary["orange"][auDictionary["orange"]["currentFrame"]], orangeAU_rect)

        for event in pygame.event.get():  # Retrieves all events running.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if frameCounter < 10:  # Changes AU frame every 10 frames.
                        frameCounter += 1
                    else:
                        frameCounter = 0
                        if menuActive:
                            for imageName in auDictionary:  # Loops through each colour in the dictionary.
                                image = auDictionary[imageName]
                                if image["currentFrame"] < len(
                                        image) - 1:  # Length of each colour dictionary is 5, which is why it is len(image) - 1.
                                    image["currentFrame"] += 1
                                else:
                                    image[
                                        "currentFrame"] = 1  # If the current index is not less than 4 (the last frame), then it is sent back to 1 (the first frame).


    # Framerate synchronisation.
    if frameCounter < 10:  # Changes AU frame every 10 frames.
        frameCounter += 1
    else:
        frameCounter = 0
        if menuActive:
            for imageName in auDictionary:  # Loops through each colour in the dictionary.
                image = auDictionary[imageName]
                if image["currentFrame"] < len(image) - 1:  # Length of each colour dictionary is 5, which is why it is len(image) - 1.
                    image["currentFrame"] += 1
                else:
                    image[
                        "currentFrame"] = 1  # If the current index is not less than 4 (the last frame), then it is sent back to 1 (the first frame).

    pygame.display.flip()  # Updates the display.
    clock.tick(60)  # Sets the framerate; here, 60fps has been set as the target.