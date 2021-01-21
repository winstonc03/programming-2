# sprite_example.py
# Introduction to the Sprite class

# Goals:
#   * introduce the Sprite class
#   * subclass the Sprite class (inheritance)

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1920
HEIGHT = 1080
TITLE = "Sprite Example"
NUM_JEWELS = 75
NUM_ENEMY = 4


class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        # call the superclass constructor
        super().__init__()

        # Image is a Surface
        self.image = pygame.Surface((35, 20))
        self.image.fill(SKY_BLUE)

        # Rect is Rectangle (x, y, width, height)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/tyler1lol.png")
        self.image = pygame.transform.scale(self.image, (110, 87))

        self.rect = self.image.get_rect()

    def update(self):
        """Changes the position of the player
        based on the mouse position"""
        self.rect.center = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/diamond.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        self.x, self.y = (
            random.randrange(1, WIDTH),
            random.randrange(1, HEIGHT)
        )

        self.vel_x = 3
        self.vel_y = 3

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vel_x *= -1
        if self.rect.y + 250 > HEIGHT or self.rect.y + 75 < 0:
            self.vel_y *= -1


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    score = 0

    # Sprite group and sprite creation
    sprite_group = pygame.sprite.Group()
    jewels_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    # Jewel creation
    for i in range(NUM_JEWELS):
        jewel = Jewel()
        # Spawn inside the visible screen
        jewel.rect.x = random.randrange(WIDTH - jewel.rect.width)
        jewel.rect.y = random.randrange(HEIGHT - jewel.rect.height)
        sprite_group.add(jewel)
        jewels_group.add(jewel)

    player = Player()
    sprite_group.add(player)

    for x in range(NUM_ENEMY):
        enemy = Enemy()
        enemy.rect.x = random.randrange(WIDTH - enemy.rect.width)
        enemy.rect.y = random.randrange(HEIGHT - enemy.rect.height)
        sprite_group.add(enemy)
        enemy_group.add(enemy)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        sprite_group.update()

        # Player collides with jewel
        jewels_collected = pygame.sprite.spritecollide(player, jewels_group, True)
        for jewel in jewels_collected:
            score += 1
            print(score)

        player_collide = pygame.sprite.spritecollide(player, enemy_group, True)

        if player_collide:
            done = True
        # ----- DRAW
        screen.fill(BLACK)
        sprite_group.draw(screen)

        # ----- UPDATE
        for enemy in enemy_group:
            enemy.update()


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()