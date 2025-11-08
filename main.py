import pygame
import pmtext.para
import pmtext.util_pygame
import random
import math

from src.button import Button
from src.fancy_text import FancyText
from src.story_parser import story_parser
from config.default_config import SCREEN_HEIGHT, SCREEN_WIDTH, FONT, STORY

game_frame = 0
objects = []


def main():
    global game_frame
    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    pygFont = pygame.font.Font(FONT, 25)

    # Setting up clock and delta
    clock = pygame.time.Clock()
    dt = 0

    test_section = []
    test_section.append("You wake up in an area unknown to you.")
    test_section.append(
        "Looking around to realize it is a [#c-255,0,0#] [#shake#] dark cave [#reset#]"
    )
    test_section.append(
        "Staring down at the floor you notice what appears to [#newline#] be a torch and a flashlight."
    )

    # NOTE Line length greater than 70 should newline

    # newFancyText = FancyText(FONT, screen, test_section, objects)

    story_sections = story_parser(STORY)

    newFancyText = FancyText(FONT, screen, story_sections[0].text_block, objects)
    ## Button Testing
    customButton = Button(
        440,
        600,
        400,
        100,
        pygFont,
        screen,
        objects,
        False,
        "Button for choice 1",
        myFunction,
        "data_choice",
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw a white background
        screen.fill("black")

        for object in objects:
            object.process()

        # Update the window
        pygame.display.flip()
        game_frame += 1

        # print("Hello from reflections-cyoa!")
        dt = clock.tick(60) / 1000


def jitter(char_index):
    """Angry text motion."""
    x = random.randint(0, 1)
    y = random.randint(0, 1)
    return x, y


def singsong(char_index):
    """Happy text motion."""
    x = math.cos(float(game_frame + char_index) / 2)
    y = math.sin(float(game_frame + char_index) / 2)
    return x, y


def myFunction(current_choice):
    print(f"Choice clicked: ", current_choice)


if __name__ == "__main__":
    main()
