#!/usr/bin/env python3
"""
ASCII Adventure Game
A choose your own adventure game that displays amazing ASCII art based on user choices.
"""

import os
import sys
import time
import random

# Import ASCII art from our organized modules
from ascii_art import (
    DRAGON,
    CASTLE,
    TREASURE,
    WIZARD,
    FOREST,
    UNICORN,
    DEATH
)
    
class Game:
    """Main game class for the ASCII Adventure."""
    
    def __init__(self):
        self.player_name = ""
        self.health = 100
        self.items = []
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def slow_print(self, text, delay=0.03):
        """Print text with a typewriter effect."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def display_art(self, art):
        """Display ASCII art with a dramatic pause."""
        print("\n" + "="*60)
        print(art)
        print("="*60 + "\n")
        time.sleep(2)
        
    def start_game(self):
        """Start the adventure game."""
        self.clear_screen()
        
        # Game title
        title = r"""
                 _    ____   ____ ___ ___      _    ______     _______ _   _ _____ _   _ ____  _____ 
                / \  / ___| / ___|_ _|_ _|    / \  |  _ \ \   / / ____| \ | |_   _| | | |  _ \| ____|
               / _ \ \___ \| |    | | | |    / _ \ | | | \ \ / /|  _| |  \| | | | | | | | |_) |  _|  
              / ___ \ ___) | |___ | | | |   / ___ \| |_| |\ V / | |___| |\  | | | | |_| |  _ <| |___ 
             /_/   \_\____/ \____|___|___| /_/   \_\____/  \_/  |_____|_| \_| |_|  \___/|_| \_\_____|
                                                                                        
        """
        
        print(title)
        self.slow_print("\n🗡️  Welcome to ASCII Adventure! 🗡️\n", 0.05)
        
        # Get player name
        self.player_name = input("What is your name, brave adventurer? ").strip()
        if not self.player_name:
            self.player_name = "Anonymous Hero"
            
        self.slow_print(f"\nWelcome, {self.player_name}! Your adventure begins now...\n")
        
        # Start the adventure
        self.intro_scene()
        
    def intro_scene(self):
        """Opening scene of the adventure."""
        self.clear_screen()
        
        self.slow_print(f"{self.player_name}, you find yourself at the entrance of a mysterious realm.")
        self.slow_print("Three paths stretch before you, each leading to unknown dangers and treasures.")
        self.slow_print("The wind whispers ancient secrets, and you must choose your destiny...\n")
        
        print("Where do you wish to go?")
        print("1. 🏰 The Enchanted Castle")
        print("2. 🌲 The Dark Forest")
        print("3. 🏔️  The Dragon's Mountain")
        print("4. 🔮 The Wizard's Tower")
        
        choice = input("\nEnter your choice (1-4) or type a keyword: ").strip().lower()
        
        # Handle both numbered choices and keywords
        if choice in ['1', 'castle', 'enchanted']:
            self.castle_path()
        elif choice in ['2', 'forest', 'dark', 'trees']:
            self.forest_path()
        elif choice in ['3', 'dragon', 'mountain', 'fire']:
            self.dragon_path()
        elif choice in ['4', 'wizard', 'tower', 'magic']:
            self.wizard_path()
        elif choice in ['treasure', 'gold', 'riches']:
            self.treasure_ending()
        elif choice in ['unicorn', 'magical', 'rainbow']:
            self.unicorn_ending()
        elif choice in ['death', 'die', 'skull']:
            self.death_ending()
        else:
            self.slow_print("You hesitate, and the paths begin to shift mysteriously...")
            time.sleep(1)
            self.intro_scene()
            
    def castle_path(self):
        """The castle adventure path."""
        self.clear_screen()
        self.display_art(CASTLE)
        
        self.slow_print("You approach the majestic castle, its towers reaching toward the clouds.")
        self.slow_print("The massive gates are guarded by stone gargoyles that seem to watch your every move.")
        self.slow_print("As you step closer, you notice a riddle carved into the gate:\n")
        
        self.slow_print("'I have cities, but no houses dwell. I have mountains, but no trees as well.")
        self.slow_print("I have water, but no fish swim free. What am I for all to see?'\n")
        
        answer = input("What is your answer? ").strip().lower()
        
        if answer in ['map', 'a map']:
            self.slow_print("\nThe gates creak open with ancient wisdom!")
            self.slow_print("Inside, you discover a vault filled with golden treasures!")
            self.treasure_ending()
        else:
            self.slow_print("\nThe gargoyles come to life with glowing red eyes!")
            self.slow_print("They speak in unison: 'Wrong answer, mortal!'")
            self.death_ending()
            
    def forest_path(self):
        """The forest adventure path."""
        self.clear_screen()
        self.display_art(FOREST)
        
        self.slow_print("You enter the dark forest where twisted trees form a canopy overhead.")
        self.slow_print("Mysterious sounds echo through the woods - whispers, rustling leaves, distant howls.")
        self.slow_print("Deep in the forest, you encounter a fork in the path.\n")
        
        print("Which way do you go?")
        print("1. Follow the glowing mushrooms")
        print("2. Take the path marked with ancient runes")
        print("3. Follow the sound of running water")
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice in ['1', 'mushrooms', 'glow']:
            self.slow_print("\nThe glowing mushrooms lead you to a magical clearing...")
            self.unicorn_ending()
        elif choice in ['2', 'runes', 'ancient']:
            self.slow_print("\nThe ancient runes guide you to a wise wizard's sanctuary...")
            self.wizard_path()
        elif choice in ['3', 'water', 'stream']:
            self.slow_print("\nYou follow the stream and discover a hidden cave filled with treasure!")
            self.treasure_ending()
        else:
            self.slow_print("\nYou wander aimlessly and get lost in the eternal darkness...")
            self.death_ending()
            
    def dragon_path(self):
        """The dragon adventure path."""
        self.clear_screen()
        self.display_art(DRAGON)
        
        self.slow_print("You climb the treacherous mountain path to the dragon's lair.")
        self.slow_print("The ancient beast awakens, its eyes glowing like molten gold.")
        self.slow_print("'Who dares disturb my slumber?' the dragon roars, breathing smoke.\n")
        
        print("How do you respond?")
        print("1. 'I seek wisdom, great dragon!'")
        print("2. 'I challenge you to combat!'")
        print("3. 'I come bearing gifts!'")
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice in ['1', 'wisdom', 'seek']:
            self.slow_print("\nThe dragon nods approvingly: 'Wisdom is the greatest treasure.'")
            self.slow_print("The dragon shares ancient knowledge and grants you magical powers!")
            self.wizard_ending()
        elif choice in ['2', 'combat', 'challenge', 'fight']:
            self.slow_print("\nThe dragon laughs: 'Brave but foolish, little one!'")
            self.slow_print("You engage in epic battle but are no match for the ancient beast...")
            self.death_ending()
        elif choice in ['3', 'gifts', 'bearing']:
            self.slow_print("\nThe dragon is pleased: 'A wise offering deserves reward!'")
            self.slow_print("The dragon shares its vast treasure hoard with you!")
            self.treasure_ending()
        else:
            self.slow_print("\nThe dragon grows impatient with your silence...")
            self.death_ending()
            
    def wizard_path(self):
        """The wizard adventure path."""
        self.clear_screen()
        self.display_art(WIZARD)
        
        self.slow_print("You ascend the spiral staircase of the mysterious tower.")
        self.slow_print("At the top, you find a wise wizard surrounded by floating books and glowing orbs.")
        self.slow_print("'Ah, a seeker of knowledge!' the wizard exclaims with twinkling eyes.\n")
        
        self.slow_print("The wizard offers you three magical potions:")
        print("1. 🔴 Red potion - Grants immense strength")
        print("2. 🔵 Blue potion - Grants magical wisdom")
        print("3. 🟢 Green potion - Grants eternal life")
        
        choice = input("\nWhich potion do you choose? ").strip().lower()
        
        if choice in ['1', 'red', 'strength']:
            self.slow_print("\nYou drink the red potion and feel incredible power coursing through you!")
            self.slow_print("You become a legendary warrior and live a life of great adventures!")
            self.wizard_ending()
        elif choice in ['2', 'blue', 'wisdom']:
            self.slow_print("\nYou drink the blue potion and your mind expands with cosmic knowledge!")
            self.slow_print("You become a master wizard yourself!")
            self.wizard_ending()
        elif choice in ['3', 'green', 'life', 'eternal']:
            self.slow_print("\nYou drink the green potion... but eternal life is a curse without purpose!")
            self.slow_print("You wander the earth forever, watching all you love fade away...")
            self.death_ending()
        else:
            self.slow_print("\nThe wizard frowns at your indecision and vanishes in a puff of smoke...")
            self.death_ending()
            
    def treasure_ending(self):
        """Happy ending with treasure."""
        self.clear_screen()
        self.display_art(TREASURE)
        
        self.slow_print(f"🎉 Congratulations, {self.player_name}! 🎉")
        self.slow_print("You have discovered unimaginable riches!")
        self.slow_print("Chests overflow with gold coins, precious gems, and ancient artifacts.")
        self.slow_print("Your name will be remembered as a legendary treasure hunter!")
        self.end_game()
        
    def unicorn_ending(self):
        """Magical unicorn ending."""
        self.clear_screen()
        self.display_art(UNICORN)
        
        self.slow_print(f"✨ Magical success, {self.player_name}! ✨")
        self.slow_print("You encounter a majestic unicorn in a field of rainbow flowers!")
        self.slow_print("The unicorn grants you a wish, and you choose to bring peace to all lands.")
        self.slow_print("You become a legendary peacekeeper, beloved by all creatures!")
        self.end_game()
        
    def wizard_ending(self):
        """Magical wizard ending."""
        self.clear_screen()
        self.display_art(WIZARD)
        
        self.slow_print(f"🔮 Mystical triumph, {self.player_name}! 🔮")
        self.slow_print("You have gained powerful magical abilities!")
        self.slow_print("With your new wisdom and power, you help those in need.")
        self.slow_print("You become a legendary wizard, protector of the realm!")
        self.end_game()
        
    def death_ending(self):
        """Game over ending."""
        self.clear_screen()
        self.display_art(DEATH)
        
        self.slow_print(f"💀 Game Over, {self.player_name}... 💀")
        self.slow_print("Your adventure has come to an unfortunate end.")
        self.slow_print("But fear not! Every great hero has faced defeat before achieving glory.")
        self.slow_print("Your story ends here, but legends never truly die...")
        self.end_game()
        
    def end_game(self):
        """End the game and offer to play again."""
        self.slow_print("\n" + "="*60)
        self.slow_print("Thank you for playing ASCII Adventure!")
        
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again in ['y', 'yes']:
            self.__init__()  # Reset game state
            self.start_game()
        else:
            self.slow_print("Farewell, brave adventurer! May your real-life quests be legendary!")
            sys.exit(0)

def main():
    """Main function to run the game."""
    try:
        game = Game()
        game.start_game()
    except KeyboardInterrupt:
        print("\n\nThanks for playing! Adventure awaits another day...")
        sys.exit(0)

if __name__ == "__main__":
    main()
