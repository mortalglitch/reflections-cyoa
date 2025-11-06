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
    t = pmtext.para.Typewriter(p)

    t.color(255, 255, 255)
    t.string("Hello ")
    t.newline()
    t.wait(10)
    t.color(255, 0, 0)
    t.string("world")
    t.color(255, 255, 255)
    t.string(".")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw a white background
        screen.fill("black")

        # Draw Typewriter
        t.pulse()
        t.draw(screen, 10, 10)

        # Update the window
        pygame.display.flip()

        # print("Hello from reflections-cyoa!")
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
