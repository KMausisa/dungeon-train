import arcade

from game import constants

class Dungeon(arcade.Window):
    """
    Main application class.
    """
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            constants.SCREEN_TITLE
        )

        # temporary background color
        arcade.set_background_color(arcade.color.BLACK)

        # scene object
        self.scene = None

        # tilemap object
        self.tile_map = None

    def setup(self):
        """
        Setup Game Here. 
        Call this function to restart the game.
        """
        # name of the tilemap to load
        map_name = constants.MAP

        # Layer specific options are defined based on 
        # Layer names in a dictionary. Doing this will 
        # make the SpriteList for the platforms layer
        # use spatial hashing for detection.
        layer_options = {
            "Base Layer": {
                "use_spatial_hash": True,
            },
            "Layer 1": {
                "use_spatial_hash": True,
            },
            "Layer 2": {
                "use_spatial_hash": True,
            },
        }

        # read the tiled map
        self.tile_map = arcade.load_tilemap(map_name, constants.TILE_SCALING, layer_options)

        # initialize scene with our tile map
        self.scene = arcade.Scene.from_tilemap(self.tile_map)


    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        # draw our scene
        self.scene.draw()