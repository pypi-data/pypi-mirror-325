# Copyright 2021-2023 Facundo Batista
# Licensed under the GPL v3 License
# For further info, check https://github.com/facundobatista/pyempaq

import math

import arcade


class RotatingSprite(arcade.Sprite):
    """A sprite that can rotate around a de-centered point.

    It can be stantiated with regular Sprite positional and keyword arguments, but
    also these new two arguments are available: 'decenter_rotation_x' and 'decenter_rotation_y',
    to specify the de-centered rotation point (in x and y deltas to the sprite's center); both
    are optional with default to 0.

    This class hooks correctly on Sprite internals, so it will rotate around the de-centered
    point when setting the Sprite's `angle` attribute or calling its `turn_left` or `turn_right`
    methods.

    Also, a new `rotcenter_pos` attribute is provided, which holds the current position of the
    de-centered rotation point. Setting this attribute will move the sprite in a way that the
    de-centered rotation point will be in the indicated position.
    """

    def __init__(self, *args, **kwargs):
        _decenter_x = kwargs.pop("decenter_rotation_x", 0)
        _decenter_y = kwargs.pop("decenter_rotation_y", 0)
        super().__init__(*args, **kwargs)
        self.decenter_anglerad = math.atan2(_decenter_y, _decenter_x)
        self.decenter_hyp = (_decenter_x ** 2 + _decenter_y ** 2) ** .5

    def _get_decenter_extras(self):
        """Get x and y distances from sprite center to the rotation center.

        This is based on current sprite angle and original decenter angle and hypotenuse.
        """
        composed_angle = self.decenter_anglerad - math.radians(self.angle)
        extra_x = self.decenter_hyp * math.cos(composed_angle)
        extra_y = self.decenter_hyp * math.sin(composed_angle)

        return extra_x, extra_y

    def _get_rotcenter_coords(self):
        if not self.decenter_anglerad:
            return self.center_x, self.center_y

        extra_x, extra_y = self._get_decenter_extras()
        return self.center_x + extra_x, self.center_y + extra_y

    def _get_angle(self):
        return arcade.Sprite.angle.fget(self)

    def _set_angle(self, value):
        delta = value - self._angle
        if delta == 0:
            return

        # Move the sprite along a circle centered on the point by degrees
        rot_x, rot_y = self._get_rotcenter_coords()
        self.position = arcade.math.rotate_point(self.center_x, self.center_y, rot_x, rot_y, delta)

        return arcade.Sprite.angle.fset(self, value)

    angle = property(_get_angle, _set_angle)

    def _set_rotcenter_coords(self, x_y):
        if self.decenter_anglerad:
            x, y = x_y
            extra_x, extra_y = self._get_decenter_extras()
            new_center_position = x - extra_x, y - extra_y
        else:
            new_center_position = x, y
        self.position = new_center_position

    rotcenter_pos = property(_get_rotcenter_coords, _set_rotcenter_coords)
