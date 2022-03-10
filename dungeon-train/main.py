import arcade

from game import constants
from game.dungeon_train import Dungeon

def main():
    window = Dungeon()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()