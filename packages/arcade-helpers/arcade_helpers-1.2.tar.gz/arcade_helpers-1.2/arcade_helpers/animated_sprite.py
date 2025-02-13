# Copyright 2023-2025 Facundo Batista
# Licensed under the Apache v2 License
# For further info, check https://github.com/facundobatista/arcade-helpers

import arcade


class AnimatedSprite(arcade.Sprite):
    """Implement a sprite with textures that change in time to show animation.

    The `update` method should be called passing `delta_time`, and if the Sprite is animating
    (previously started with `play()`) it will rotate from different textures until finishes
    the sequence.

    Keep calling the `play()` method while animation should be active. When animation should
    finish stop calling `play()` and will finish after completing the sequence, or call `stop()`
    to force it to immediately stop (will go to first texture, NOT left in the middle).

    Mandatory named parameters:
    - textures: a list of at least 2 textures (otherwise an animation is not possible)
    - duration: the length in seconds of the duration for the whole animation

    The rest of keyword arguments are passed to Sprite (except 'path_or_texture', it's forbidden
    as the textures are managed by the AnimatedSprite). No positional arguments are allowed.
    """

    def __init__(self, **kwargs):
        # handle parameters
        textures = kwargs.get("textures", [])
        if len(textures) < 2:
            raise ValueError(
                "Missing a 'textures' argument holding at least 2 items "
                "(otherwise an animation is not possible)"
            )
        self._duration = kwargs.pop("duration", None)
        if self._duration is None or not isinstance(self._duration, (int, float)):
            raise ValueError(
                "Missing a 'duration' int or float argument (in seconds)"
            )
        if "path_or_texture" in kwargs:
            raise ValueError(
                "The 'path_or_texture' argument is forbidden; use 'textures'"
            )

        super().__init__(textures[0], **kwargs)
        # fix instance textures as __init__ only uses first one
        self.textures = textures

        self._animating = False
        self._time_base = None

    def update(self, delta_time):
        """Update the sprite."""
        super().update(delta_time)

        if self._animating:
            self._time_base += delta_time
            if self._time_base > self._duration:
                self._animating = False
                self._time_base = None
                return

            idx = int(len(self.textures) * self._time_base / self._duration)

            # increase by one and wrap to 0; this way the animation goes from second frame and
            # always ends in the first one (the "quiet frame")
            idx += 1
            if idx == len(self.textures):
                idx = 0

            frame = self.textures[idx]
            self.texture = frame

    def play(self):
        """Start animating."""
        if not self._animating:
            self._animating = True
            self._time_base = 0

    def stop(self):
        """Stop animating."""
        self._animating = False
        self._time_base = None
        self.texture = self.textures[0]
