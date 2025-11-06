import pygame
import pmtext.para
import pmtext.util_pygame

from config.default_config import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()

    # Setting up clock and delta
    clock = pygame.time.Clock()
    dt = 0

    # pmtext init
    font = pmtext.util_pygame.TTF(
        "./fonts/BigBlueTerminal/BigBlueTermPlusNerdFontMono-Regular.ttf", 12
    )
    p = pmtext.para.Graph(font)

    p.color(0, 0, 0)
    p.string("Hello ")
    p.color(255, 0, 0)
    p.string("world")
    p.color(0, 0, 0)
    p.string(".")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw a white background
        screen.fill("white")

        # Draw a paragraph
        p.draw(screen, 10, 10)

        # Update the window
        pygame.display.flip()

        # Wait a bit
        # pygame.time.wait(2000)

        print("Hello from reflections-cyoa!")
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
