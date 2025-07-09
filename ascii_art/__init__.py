"""
ASCII Art Package

This package contains all the ASCII art used in the adventure game.
Each art piece is in its own module for better organization.

Usage:
    from ascii_art import dragon, castle, treasure
    
    # Use the art
    print(dragon.DRAGON)
    print(castle.CASTLE)
"""

# Import all ASCII art for easy access
from .dragon import DRAGON
from .castle import CASTLE
from .treasure import TREASURE
from .wizard import WIZARD
from .forest import FOREST
from .unicorn import UNICORN
from .death import DEATH

# Make all art available from the package root
__all__ = [
    'DRAGON',
    'CASTLE', 
    'TREASURE',
    'WIZARD',
    'FOREST',
    'UNICORN',
    'DEATH'
]
