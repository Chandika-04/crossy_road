import pygame as pg

import board
import sprites as spr

# pygame setup
WIDTH = 1280
HEIGHT = 720
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Crossy Road Creeper ver.")
clock = pg.time.Clock()
running = True


# running code
creeper = spr.Creeper()
creeper_group = pg.sprite.Group()
creeper_group.add(creeper)

rail_group = pg.sprite.Group()

board = board.Background("grass.png", screen)

# game loop
while running:
    clock.tick(60)  # Set the frame rate to 60 FPS

    for event in pg.event.get():
        if (
            event.type == pg.QUIT
        ):  # check for quit event and exit game loop to close window
            running = False

    board.draw()  # Draw the background
    board.update(screen)  # Update the background

    creeper_group.draw(screen)
    creeper_group.update(HEIGHT, WIDTH)  # Update the sprite group

    WIDTH = screen.get_width()  # Get the width of the screen
    HEIGHT = screen.get_height()  # Get the height of the screen

    pg.display.flip()  # Update the display
pg.quit()
