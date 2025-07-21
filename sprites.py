# sprite object classes
import pygame as pg


class Railroad(pg.sprite.Sprite):
    screenheight = 720  # Set a default height for the railroad

    def __init__(self, height=screenheight):
        super().__init__()
        self.screenheight = height
        self.x = -50
        self.y = int(self.screenheight / 2)
        self.speed = 10
        self.width = 120
        self.height = self.screenheight

        self.image = pg.image.load("rail.PNG")
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def movement(self):
        self.x -= self.speed

    def update(self, height=screenheight):
        self.screenheight = height
        self.movement()
        self.rect.center = (self.x, self.y)
        if self.x + self.width < 0:
            self.kill()

    def getpos(self):
        return self.x, self.y


class Creeper(pg.sprite.Sprite):
    screenheight = 720
    screenwidth = 1280

    def __init__(self, height=screenheight, width=screenwidth):
        super().__init__()
        self.screenheight = height
        self.screenwidth = width
        self.x = 50
        self.y = int(self.screenheight / 2)
        self.speed = 30
        self.width = 80
        self.height = 125

        self.creeperR = pg.image.load("creeperRight.PNG")
        self.creeperR = pg.transform.scale(self.creeperR, (self.width, self.height))
        self.creeperL = pg.image.load("creeperLeft.PNG")
        self.creeperL = pg.transform.scale(self.creeperL, (self.width, self.height))

        self.image = self.creeperR
        self.rect = self.image.get_rect()

    def update(self, height=screenheight, width=screenwidth):
        self.screenheight = height
        self.screenwidth = width
        self.movement()
        self.boundary()
        self.rect.center = (self.x, self.y)

    def boundary(self):
        if self.x - (self.width / 2) < 0:
            self.x = int(self.width / 2)
        elif self.x + (self.width / 2) > self.screenwidth:
            self.x = int(self.screenwidth - (self.width / 2))
        if self.y - (self.height / 2) < 0:
            self.y = int(self.height / 2)
        elif self.y + (self.height / 2) > self.screenheight:
            self.y = int(self.screenheight - (self.height / 2))

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
