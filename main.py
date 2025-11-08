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
current_buttons = []
change_flag = True
current_section = 0


def main():
    global game_frame
    global objects
    global current_buttons
    global change_flag
    global current_section
    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    pygFont = pygame.font.Font(FONT, 25)

    # Setting up clock and delta
    clock = pygame.time.Clock()
    dt = 0

    # NOTE Line length greater than 70 should newline

    # newFancyText = FancyText(FONT, screen, test_section, objects)

    story_sections = story_parser(STORY)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw a black background
        screen.fill("black")
        if change_flag:
            newFancyText = FancyText(
                FONT, screen, story_sections[current_section].text_block, objects
            )
            generate_buttons(
                story_sections[current_section].choices,
                current_buttons,
                objects,
                pygFont,
                screen,
                newFancyText,
            )
            change_flag = False
        for object in objects:
            object.process()

        # Update the window
        pygame.display.flip()
        game_frame += 1

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


def progess_story(current_choice, current_text):
    print(f"Choice clicked: ", current_choice)
    objects.remove(current_text)


def generate_buttons(choices, current_buttons, objects, pygFont, screen, newFancyText):
    if current_buttons != None:
        for button in current_buttons:
            objects.remove(button)
    offset = -300
    for choice in choices:
        newButton = Button(
            SCREEN_WIDTH / len(choices) + offset,
            SCREEN_HEIGHT - 110,
            300,
            100,
            pygFont,
            screen,
            objects,
            newFancyText,
            False,
            choice[0],
            progess_story,
            choice[1],
        )
        offset += 350


if __name__ == "__main__":
    main()
