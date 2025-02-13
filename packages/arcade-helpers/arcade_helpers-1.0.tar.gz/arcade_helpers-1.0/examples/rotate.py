# Copyright 2021-2023 Facundo Batista
# Licensed under the GPL v3 License
# For further info, check https://github.com/facundobatista/pyempaq

import math

import arcade

from arcade_helpers import key_manager, rotating_sprite

ANGLE_STEP = 2
SPEED_STEP = .1


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "Rotation example")
        arcade.set_background_color(arcade.csscolor.WHITE)

        self.keys = key_manager.KeyManager(self)
        self.keys.on_release(arcade.key.ESCAPE, arcade.exit)
        self.keys.on_release(arcade.key.L, self.rotate, -90)
        self.keys.on_release(arcade.key.R, self.rotate, 90)
        self.sprite = None

    def setup(self):
        """Set up the game here; call this function to restart the game."""
        self.sprite = rotating_sprite.RotatingSprite(
            ":resources:/images/space_shooter/playerShip1_blue.png",
            scale=.5,
            decenter_rotation_x=40,
            decenter_rotation_y=-10,
        )

        self.sprite.center_x = 400
        self.sprite.center_y = 300
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.sprite)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.sprite_list.draw()

        ship = self.sprite
        self.report([
            ("Pos X", ship.center_x),
            ("Pos Y", ship.center_y),
            ("Vel X", ship.change_x),
            ("Vel Y", ship.change_y),
            ("Angle", ship.angle % 360),
        ])

        from_x, from_y = ship.position
        end_x, end_y = ship.rotcenter_pos
        arcade.draw_line(from_x, from_y, end_x, end_y, arcade.csscolor.BLACK)

    def report(self, texts):
        """Report info on screen."""
        pos_y = 10
        for title, value in reversed(texts):
            text = f"{title}: {value:7.2f}"
            arcade.Text(text, 6, pos_y, arcade.csscolor.BLACK, 12, font_name="Courier").draw()
            pos_y += 25

    def on_mouse_press(self, x, y, button, modifiers):
        """Teletransport ship."""
        self.sprite.rotcenter_pos = (x, y)

    def on_update(self, delta_time):
        """Movement and game logic"""
        if self.keys.is_pressed(arcade.key.LEFT):
            self.sprite.turn_left(ANGLE_STEP)
        if self.keys.is_pressed(arcade.key.RIGHT):
            self.sprite.turn_right(ANGLE_STEP)
        if self.keys.is_pressed(arcade.key.UP):
            angle_rad = math.radians(self.sprite.angle)
            self.sprite.change_x += math.sin(angle_rad) * SPEED_STEP
            self.sprite.change_y += math.cos(angle_rad) * SPEED_STEP

        self.sprite.update(delta_time)

    def rotate(self, angles):
        """Rotate the sprite a fixed amount of angles."""
        self.sprite.angle += angles


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
