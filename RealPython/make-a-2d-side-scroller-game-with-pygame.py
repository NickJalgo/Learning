# Draw items on your screen
# Play sound effects and music
# Handle user input
# Implement event loops
# Explore how game programming differs from standard procedural Python programming

 # PyGame is a wrapper for the SDL library
 # SDL -> Simple DirectMedia Layer
 # Provides cross-platform multimedia hardware support
 
 # AP -> python -m pygame.examples.aliens

from time import sleep

# Import and initialize the pygame library 
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    )

pygame.init() 

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

sleep(5)