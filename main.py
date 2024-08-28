import pygame 
from player import Player
from constants import *


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    body_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatable_group:
            updatable.update(dt)
        for drawable in drawable_group:
            drawable.draw(screen)
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()