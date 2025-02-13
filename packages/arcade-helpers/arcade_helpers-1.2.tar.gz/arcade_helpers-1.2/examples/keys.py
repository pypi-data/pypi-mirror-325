# Copyright 2023-2025 Facundo Batista
# Licensed under the Apache v2 License
# For further info, check https://github.com/facundobatista/arcade-helpers

import arcade

from arcade_helpers import key_manager

MOVE_STEP = 5

BLUE_GEM = arcade.load_texture(":resources:/images/items/gemBlue.png")
RED_GEM = arcade.load_texture(":resources:/images/items/gemRed.png")

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Key Manager example")
        arcade.set_background_color(arcade.csscolor.WHITE)
        self.camera = arcade.camera.Camera2D(
            position=(0, 0),
            projection=arcade.types.LRBT(left=0, right=WINDOW_WIDTH, bottom=0, top=WINDOW_HEIGHT),
            viewport=self.rect
        )

        self.sprite = None

        self.keys = key_manager.KeyManager(self)
        self.keys.on_release(arcade.key.ESCAPE, arcade.exit)
        self.keys.on_release(arcade.key.F, self.toggle_fullscreen)
        self.keys.on_release(arcade.key.B, self.set_gem, BLUE_GEM)
        self.keys.on_release(arcade.key.R, self.set_gem, RED_GEM)

    def setup(self):
        """Set up the game here; call this function to restart the game."""
        self.sprite = arcade.Sprite(BLUE_GEM, 1)
        self.sprite.center_x = WINDOW_WIDTH // 2
        self.sprite.center_y = WINDOW_HEIGHT // 2
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.sprite)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        with self.camera.activate():
            self.sprite_list.draw()

    def toggle_fullscreen(self):
        self.set_fullscreen(not self.fullscreen)
        self.camera.viewport = self.rect

    def set_gem(self, texture):
        self.sprite.texture = texture

    def on_update(self, delta_time):
        """Movement and game logic"""
        x, y = self.sprite.position

        if self.keys.is_pressed(arcade.key.LEFT):
            x -= MOVE_STEP
        if self.keys.is_pressed(arcade.key.RIGHT):
            x += MOVE_STEP
        if self.keys.is_pressed(arcade.key.UP):
            y += MOVE_STEP
        if self.keys.is_pressed(arcade.key.DOWN):
            y -= MOVE_STEP

        self.sprite.position = (x, y)


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
