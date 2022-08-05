# https://www.youtube.com/watch?v=nGufy7weyGY&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=4
# https://www.youtube.com/watch?v=-5GNbL33hz0&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=5
# https://www.youtube.com/watch?v=33g62PpFwsE&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=6
# https://www.youtube.com/watch?v=mOckdKp3V38&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=7
# https://www.youtube.com/watch?v=_y5U8tB36Vk&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=8

# Shmup game
import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image = meteor_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)  # we compute the radius for the cicrle collision
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill it if moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# Load all game graphics
background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
player_img_rect = player_img.get_rect()
meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
meteor_img_rect = meteor_img.get_rect()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
bullet_img_rect = bullet_img.get_rect()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # Check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)  # True, True as we want mobs and bullets to be deleted
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if the player hit a mob
    # We want to check the player against the mobs group, so it tells us if any of the mobs hits the player.
    # hits is a list of the mobs that hit the player.
    hits = pygame.sprite.spritecollide(player, mobs,
                                       False, pygame.sprite.collide_circle)
    # False tell us if any mobs that get hit should be deleted or not and pygame.sprite.collide_circle is to tell
    # that we don't use a rectangle but a circle to detect collisions

    # if the list hits is empty you don't change running otherwise running is set to False
    if hits:
        running = False

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display (double buffering)
    pygame.display.flip()

pygame.quit()
