import pygame as pg

import sprites as spr


class Background:
    def __init__(self, image_path, screen):
        super().__init__()
        self.screen = screen
        blit_image = pg.image.load(image_path).convert()
        self.image = pg.transform.scale(
            blit_image, (screen.get_width(), screen.get_height())
        )
        self.rect = self.image.get_rect(topleft=(0, 0))

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, screen):
        self.rect.topleft = (0, 0)
        self.image = pg.transform.scale(
            self.image, (screen.get_width(), screen.get_height())
        )
        self.screen.blit(self.image, self.rect)

    def generate_obstacle(self):
        # This method can be implemented to generate obstacles on the board
        pass
