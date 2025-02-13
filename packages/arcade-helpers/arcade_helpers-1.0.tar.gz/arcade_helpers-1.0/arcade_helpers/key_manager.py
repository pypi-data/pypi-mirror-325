# Copyright 2023-2025 Facundo Batista
# Licensed under the Apache v2 License
# For further info, check https://github.com/facundobatista/arcade-helpers

class KeyManager:
    """Manager to simplify the handling of keys.

    Must be instantiated with the main window.

    Provides the following methods:
    - `is_pressed(key)`: to find out if the indicated key is currently pressed
    - `on_release(key, function, *args, **kwargs)`: will call the indicated function
      when that key is released, pasing any indicated positional and/or keyword arguments.
    """

    def __init__(self, window):
        # hook callbacks
        window.on_key_press = self._on_key_press
        window.on_key_release = self._on_key_release

        # holder of keys and callbacks
        self._keys = set()
        self._callbacks = {}

    def is_pressed(self, key):
        """Return True if the specified key is currently pressed."""
        return key in self._keys

    def on_release(self, key, function, *args, **kwargs):
        """Set up to call a function when the specified key is released."""
        self._callbacks[key] = (function, args, kwargs)

    def _on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        self._keys.add(key)

    def _on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        self._keys.discard(key)
        if key in self._callbacks:
            (func, args, kwargs) = self._callbacks[key]
            func(*args, **kwargs)
