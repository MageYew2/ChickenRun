import pygame
import sys
from circleshape import CircleShape
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Initialize player at center
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.on_collision(player):
                print("Game Over!")
                sys.exit()
        player.move(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Delta time in seconds.


if __name__ == "__main__":
    main()
	

