"""Sample Main Project File.

This file is executed when the entire guessinggame
directory is run using Pytho and serves as the
main entry point for the application.

Usage:
    python3 -m guessinggame - execute this program
    (when run from project root).

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

import sys
from guessinggame.guess.Main import Main
Main.main(sys.argv)
