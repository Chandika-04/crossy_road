import pygame as pg

# pygame setup
WIDTH = 1280
HEIGHT = 720
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Crossy Road Creeper ver.")
clock = pg.time.Clock()
running = True


class Creeper(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = int(HEIGHT / 2)
        self.speed = 30
        self.width = 100
        self.height = 125

        self.creeperR = pg.image.load("creeperRight.PNG")
        self.creeperR = pg.transform.scale(self.creeperR, (self.width, self.height))
        self.creeperL = pg.image.load("creeperLeft.PNG")
        self.creeperL = pg.transform.scale(self.creeperL, (self.width, self.height))

        self.image = self.creeperR
        self.rect = self.image.get_rect()

    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.image = self.creeperL
            self.x -= self.speed

        elif keys[pg.K_RIGHT]:
            self.image = self.creeperR
            self.x += self.speed

        if keys[pg.K_UP]:
            self.y -= self.speed

        elif keys[pg.K_DOWN]:
            self.y += self.speed


creeper = Creeper()
creeper_group = pg.sprite.Group()
creeper_group.add(creeper)

while running:
    clock.tick(60)  # Set the frame rate to 60 FPS
    # pg.QUIT means user pressed X to close window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black

    creeper_group.draw(screen)
    creeper_group.update()  # Update the sprite group

    pg.display.flip()  # Update the display
pg.quit()
