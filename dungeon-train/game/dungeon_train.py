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

        arcade.set_background_color(arcade.color.BLACK)
    
    def setup(self):
        """
        Setup Game Here. 
        Call this function to restart the game.
        """
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()