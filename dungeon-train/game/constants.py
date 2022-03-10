# Write your constant variables here
import os

# store absolute path to game folder
PATH = os.path.dirname(os.path.abspath(__file__))

# screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# window name
SCREEN_TITLE = "Dungeon Train"

# tilemap
MAP = os.path.join(PATH, "..", "..", "assets", "map", "dungeon_map.tmx")

# scaling
TILE_SCALING = 1.5

