import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt




class Player(CircleShape):
    
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initial rotation angle
        self.shoot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_LEFT]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.move(dt, keys)

    def move(self, dt, keys):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)    
        if keys[pygame.K_UP]:
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_DOWN]:
            self.position -= forward * PLAYER_SPEED * dt

    def shoot(self):
        
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_INTERVAL
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

