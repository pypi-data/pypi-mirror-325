# arcade-helpers

Some helpers to work better/easier with the Arcade gaming library.

Mainly a collection of stuff I've been writing to help me or my son when writing games.

To run examples, just clone this repo, create a virtual environment and try them. E.g.:
```
python3 -m venv env
source env/bin/activate
pip install -e .
python examples/keys.py
```

## Key Manager

**Class**: `arcade_helpers.key_manager.KeyManager`

This class is a manager to simplify the handling of keys. Must be instantiated with the main window.

Provides the following methods:
- `is_pressed(key)`: to find out if the indicated key is currently pressed
- `on_release(key, function, *args, **kwargs)`: will call the indicated function when that key is released, passing any indicated positional and/or keyword arguments.


### Example:

**See:** `examples/keys.py`

The example presents a simple gem in blue in the center of the screen which we'll control in several ways using the keyboard.

The Key Manager is instantiated in `__init__`, and there some keys are hooked, to show the versatility of this functionality:
- **`ESCAPE`**: will call `arcade.exit`, a function from the Arcade library itself, to finish the game
- **`F`**: will call a method in our own class, which will toggle the full-screen mode
- **`B`** and **`R`**: will call another method in our own class, both the same method, but an extra argument is indicated which will be used by that method to set the gem in Blue or Red

Also, in the `on_update` method the "arrow keys" are checked if they are pressed; if yes the sprite position will be adjusted accordingly and the final effect is that we can move the gem around the window. This structure is simple and yet very powerful, check it to see how smooth the movement is, even when pressing more than one of these keys simultaneously.


## Animated Sprite

**Class**: `arcade_helpers.animated_sprite.AnimatedSprite`

Implements a sprite with textures that change in time to show animation.

The `update` method should be called passing `delta_time`, and if the Sprite is animating (previously started with `play()`) it will rotate from different textures until finishes the sequence.

Keep calling the `play()` method while animation should be active. When animation should finish stop calling `play()` and will finish after completing the sequence, or call `stop()` to force it to immediately stop (will go to first texture, NOT left in the middle).

Mandatory named parameters:
- textures: a list of at least 2 textures (otherwise an animation is not possible)
- duration: the length in seconds of the duration for the whole animation

The rest of keyword arguments are passed to Sprite (except 'path_or_texture', it's forbidden as the textures are managed by the AnimatedSprite). No positional arguments are allowed.

### Example:

**See:** `examples/animated.py`

The example presents a little fire that is animated when moving through the screen.

On `setup` the spritesheet is loaded from the PNG file, and then textures are *cut* from it according to designed sizes (this should vary for your spritesheet). Then `AnimatedSprite` is instantiated passing those textures, the duration in seconds of the whole sequence, and other parameters for the `Sprite` (e.g. the scale).

In the `on_update` method the sprite is refreshed passing the delta time. In this example code a `moving` variable is used to play or stop the animation. Alternatively, the animation can be left to finish naturally instead of interrupting it (comment out the `stop()` call and try it).


## Rotating Sprite

**Class**: `arcade_helpers.rotating_sprite.RotatingSprite`

This is a sprite that can rotate around a de-centered point.

It can be stantiated with regular Sprite positional and keyword arguments, but also these new two arguments are available: 'decenter_rotation_x' and 'decenter_rotation_y', to specify the de-centered rotation point (in x and y deltas to the sprite's center); both
are optional with default to 0.

This class hooks correctly on Sprite internals, so it will rotate around the de-centered point when setting the Sprite's `angle` attribute or calling its `turn_left` or `turn_right` methods.

Also, a new `rotcenter_pos` attribute is provided, which holds the current position of the de-centered rotation point. Setting this attribute will move the sprite in a way that the de-centered rotation point will be in the indicated position.

### Example:

**See:** `examples/rotate.py`

The example presents a single sprite in the screen (a space ship) with a de-centered rotation point. A line is drawn from the center of the sprite to the de-centered rotation point, so it's easier to see how the sprite rotates.

Some keys are hook in the example: the `left` and `right` arrows will rotate the ship gradually (the `up` arrow gives velocity, if you want to fly the ship), while the `r` and `l` keys will rotate it in 90° steps.

Also, the mouse is hooked. Clicking anywhere in the screen will move the ship in a way that the rotation point is in the clicked position.


## Collision Dynamics Between Sprites

**Function**: `arcade_helpers.particles_collision.collide`

**Dependency**: `numpy`

Collide two sprites using collision dynamics.

Linear and angular velocities will be adjusted for both sprites.

This function implements the equation 3.16 from book "Computational Granular Dynamics" by Thorsten Pöschel and Thomas Schwager (Springer, 2004) with the following simplifications: R=1, J̃=1.

### Example:

**See:** `examples/collision_ships.py`

The example presents a two space ships facing each other. These ships are controlled using `a/d/w` keys (left one) and the `left/right/up` arrow keys (right one).

Just go a smash both ships together and see how the behave after colliding.

Most of the example is about drawing space ships thrusts and handling keys. The relevant for the functionality is in the `on_update` method where collision is checked, and it that case the `collide` function is called.
