import pygame, player
from constants import *


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    body_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        body_player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()