# Copyright 2021-2023 Facundo Batista
# Licensed under the GPL v3 License
# For further info, check https://github.com/facundobatista/pyempaq

import math

import arcade

from arcade_helpers.key_manager import KeyManager
from arcade_helpers.particles_collision import collide

ANGLE_PUSH = 0.1
BACK_PUSH = 0.1
THRUST_COLOR = arcade.csscolor.LIGHT_GREEN
THRUST_ARC = 0.3  # in radians to each side
THRUST_LENGTH = 20  # in pixels


class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(800, 600, "Bumper ships")
        arcade.set_background_color(arcade.csscolor.WHITE)

        self.keys = KeyManager(self)
        self.keys.on_release(arcade.key.ESCAPE, arcade.exit)

    def setup(self):
        """Set up the game here; call this function to restart the game."""
        self.ship_sprite_1 = arcade.Sprite(
            ":resources:/images/space_shooter/playerShip1_blue.png", angle=90)
        self.ship_sprite_1.center_x = 200
        self.ship_sprite_1.center_y = 300
        self.ship_sprite_2 = arcade.Sprite(
            ":resources:/images/space_shooter/playerShip1_orange.png", angle=-90)
        self.ship_sprite_2.center_x = 600
        self.ship_sprite_2.center_y = 300
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.ship_sprite_1)
        self.sprite_list.append(self.ship_sprite_2)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.sprite_list.draw()

        data = [
            (self.ship_sprite_1, 6, arcade.csscolor.BLUE),
            (self.ship_sprite_2, 650, arcade.csscolor.ORANGE),
        ]
        for ship, pos_x, color in data:
            measurements = [
                ("Pos X", ship.center_x),
                ("Pos Y", ship.center_y),
                ("Vel X", ship.change_x),
                ("Vel Y", ship.change_y),
                ("Angle", ship.angle % 360),
            ]
            self._report(pos_x, color, measurements)

        if self.keys.is_pressed(arcade.key.W):
            self._thrust_back(self.ship_sprite_1)
        if self.keys.is_pressed(arcade.key.D):
            self._thrust_side(self.ship_sprite_1, clockwise=True)
        if self.keys.is_pressed(arcade.key.A):
            self._thrust_side(self.ship_sprite_1, clockwise=False)

        if self.keys.is_pressed(arcade.key.UP):
            self._thrust_back(self.ship_sprite_2)
        if self.keys.is_pressed(arcade.key.RIGHT):
            self._thrust_side(self.ship_sprite_2, clockwise=True)
        if self.keys.is_pressed(arcade.key.LEFT):
            self._thrust_side(self.ship_sprite_2, clockwise=False)

    def _thrust_back(self, ship):
        """Draw thrust from the back."""
        # ship is vertical, 0° is right wing, rear thrusther is 90° clockwise
        shipnose_angle = math.radians(ship.angle * (-1) + 90)  # because texture's nose is "up"

        # thrust from the back
        src_x = ship.center_x - ship.height / 2 * math.cos(shipnose_angle)
        src_y = ship.center_y - ship.height / 2 * math.sin(shipnose_angle)

        longit_1_angle = shipnose_angle + THRUST_ARC
        longit_2_angle = shipnose_angle - THRUST_ARC

        p1_x = src_x - THRUST_LENGTH * math.cos(longit_1_angle)
        p1_y = src_y - THRUST_LENGTH * math.sin(longit_1_angle)

        p2_x = src_x - THRUST_LENGTH * math.cos(longit_2_angle)
        p2_y = src_y - THRUST_LENGTH * math.sin(longit_2_angle)

        arcade.draw_triangle_filled(src_x, src_y, p1_x, p1_y, p2_x, p2_y, THRUST_COLOR)

    def _thrust_side(self, ship, clockwise):
        """Draw side thrusts."""
        direction = 1 if clockwise else -1

        shipnose_angle = math.radians(ship.angle * (-1) + 90)  # because texture's nose is "up"
        traversal_angle = shipnose_angle + direction * math.pi / 2

        # thrust in one side
        src_x = ship.center_x - ship.width / 2 * math.cos(traversal_angle)
        src_y = ship.center_y - ship.width / 2 * math.sin(traversal_angle)

        side_1_angle = shipnose_angle + THRUST_ARC * direction
        side_2_angle = shipnose_angle - THRUST_ARC * direction

        p1_x = src_x + THRUST_LENGTH * math.cos(side_1_angle)
        p1_y = src_y + THRUST_LENGTH * math.sin(side_1_angle)

        p2_x = src_x + THRUST_LENGTH * math.cos(side_2_angle)
        p2_y = src_y + THRUST_LENGTH * math.sin(side_2_angle)

        arcade.draw_triangle_filled(src_x, src_y, p1_x, p1_y, p2_x, p2_y, THRUST_COLOR)

        # thrust in the other side
        src_x = ship.center_x + ship.width / 2 * math.cos(traversal_angle)
        src_y = ship.center_y + ship.width / 2 * math.sin(traversal_angle)

        side_1_angle = shipnose_angle - THRUST_ARC * direction
        side_2_angle = shipnose_angle + THRUST_ARC * direction

        p1_x = src_x - THRUST_LENGTH * math.cos(side_1_angle)
        p1_y = src_y - THRUST_LENGTH * math.sin(side_1_angle)

        p2_x = src_x - THRUST_LENGTH * math.cos(side_2_angle)
        p2_y = src_y - THRUST_LENGTH * math.sin(side_2_angle)

        arcade.draw_triangle_filled(src_x, src_y, p1_x, p1_y, p2_x, p2_y, THRUST_COLOR)

    def _report(self, pos_x, color, texts):
        """Report info on screen."""
        pos_y = 10
        for title, value in reversed(texts):
            text = f"{title}: {value:7.2f}"
            arcade.Text(text, pos_x, pos_y, color, 12, font_name="Courier").draw()
            pos_y += 25

    def on_update(self, delta_time):
        """Movement and game logic"""
        ship1 = self.ship_sprite_1
        ship2 = self.ship_sprite_2

        if arcade.check_for_collision(ship1, ship2):
            collide(ship1, ship2)

        if self.keys.is_pressed(arcade.key.A):
            ship1.change_angle -= ANGLE_PUSH
        if self.keys.is_pressed(arcade.key.D):
            ship1.change_angle += ANGLE_PUSH
        if self.keys.is_pressed(arcade.key.W):
            angle_rad = math.radians(ship1.angle)
            ship1.change_x += math.sin(angle_rad) * BACK_PUSH
            ship1.change_y += math.cos(angle_rad) * BACK_PUSH

        if self.keys.is_pressed(arcade.key.LEFT):
            ship2.change_angle -= ANGLE_PUSH
        if self.keys.is_pressed(arcade.key.RIGHT):
            ship2.change_angle += ANGLE_PUSH
        if self.keys.is_pressed(arcade.key.UP):
            angle_rad = math.radians(ship2.angle)
            ship2.change_x += math.sin(angle_rad) * BACK_PUSH
            ship2.change_y += math.cos(angle_rad) * BACK_PUSH

        ship1.update(delta_time)
        ship2.update(delta_time)


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
