# Copyright 2021-2023 Facundo Batista
# Licensed under the GPL v3 License
# For further info, check https://github.com/facundobatista/pyempaq

import pathlib

import arcade

from arcade_helpers import animated_sprite, key_manager

BASEDIR = pathlib.Path(__file__).parent
MOVE_STEP = 5


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(800, 600, "Animation example")
        arcade.set_background_color(arcade.csscolor.WHITE)

        self.keys = key_manager.KeyManager(self)
        self.keys.on_release(arcade.key.ESCAPE, arcade.exit)
        self.sprite = None

    def setup(self):
        """Set up the game here; call this function to restart the game."""
        # load a sprite sheet to easily retrieve several textures from one PNG; this file has
        # 10 25x28 frames in 10 columns
        ssheet = arcade.texture.spritesheet.SpriteSheet(BASEDIR / "animation_spritesheet.png")
        textures = ssheet.get_texture_grid((25, 28), 10, 10)
        self.sprite = animated_sprite.AnimatedSprite(textures=textures, duration=1, scale=3)

        self.sprite.center_x = 400
        self.sprite.center_y = 300
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.sprite)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.sprite_list.draw()

    def on_update(self, delta_time):
        """Movement and game logic"""
        moving = False
        if self.keys.is_pressed(arcade.key.LEFT):
            self.sprite.center_x -= MOVE_STEP
            moving = True
        if self.keys.is_pressed(arcade.key.RIGHT):
            self.sprite.center_x += MOVE_STEP
            moving = True
        if self.keys.is_pressed(arcade.key.UP):
            self.sprite.center_y += MOVE_STEP
            moving = True
        if self.keys.is_pressed(arcade.key.DOWN):
            self.sprite.center_y -= MOVE_STEP
            moving = True

        if moving:
            self.sprite.play()
        else:
            self.sprite.stop()
        self.sprite.update(delta_time)


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
