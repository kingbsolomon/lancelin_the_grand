from art import *
import climage
from time import sleep
import sys
import os


name = "Lancelin the Grand"
inventory = ["Great Sword", "Map"]





clear = "\n" * 100
flying_monster = climage.convert('./images/ursula-tabaka-cu2.jpg', is_unicode=True, is_256color=True, width=100)
fight_flee = climage.convert('./images/knight_forest.jpg', is_unicode=True, is_256color=True, width=75)
fire = climage.convert('./images/fire.jpg', is_unicode=True, is_256color=True, width=75)
mage = climage.convert('./images/mage.jpg', is_unicode=True, is_256color=True, width=75)


def welcome_art():
    global name
    name_spit = name.split(" ")
    print("\033[1;32m")
    for split in name_spit:
        tprint(split, font="block")
        sleep(1)
    input("Press Enter to Continue...")

def story_intro():
    print(clear)
    print(flying_monster)
    print("\033[1;35m")
    print("""
    Lancelin had fought monsters before. Compared to the giant beast before him, the rest were harmless flies.
    “I guess this is how I’ll die,” the knight said to himself. He inhaled deeply.
    Blood rained from the red sky. The breeze from the monster’s mighty wings flapping chilled his bones.\n
    "Yeah. I'm fucked..." Lancelin said to himself.
    """)
    sleep(7)
    input("Press Enter to Continue...")
    print(clear)
    print(fight_flee)
    print("\033[1;35m")
    print("""
       The stench from the foul beast overwhelmed Lancelin's senses. Part of him wanted to flee, understandably.
       "Why should this burden be yours alone?" The voice in his head has raised a valid point. Lancelin had already risked so much.
       At what point should he care about only himself? He quickly glanced at the forest behind him and wondered if he could 
       escape the monster in the trees and the cover of darkness.\n
       
       Lancelin glanced at the sword in his hand. The scattering reflections from the ember glow of the flames from the destroyed village
       made his sword appear to shine of gold. He remembered his oath.
       
       It was time to make a decision... 
        """)
    sleep(7)
    intro_choice = input("Fight or Flee... ")
    if intro_choice == 'Flee':
        flee()
    else:
        fight()


def flee():
    print(clear)
    print(fire)
    print("\033[1;35m")
    print("""
         Lancelin dropped his sword and shield, and began to flee. Heart racing, he bounded through the impenetrable thicket.
         The screams of the beast seemed to echo from all directions. The darkness and heavy fog disoriented Lancelin, but he continued, 
         wanting to get far away from this beast. 
         
         Lancelin's death was instant. Drawing in a single breath, the beast released a hell fire that engulfed the entire forest.
         
         The End.
          """)

def fight():
    print(clear)
    print(mage)
    print("\033[1;35m")
    print("""
             Hardened with resolve, Lancelin clutches his sword and shield. He begins to move toward the beast with reckless abandon,
             when he notices a blue orb cross his path. A mysterious cloaked figure appears and hides in the shadows. A soft voice spoke directly 
             to his subconscious. 
              """)
    sleep(3)
    input("Press Enter to Continue...")



def main():
    welcome_art()
    story_intro()


if __name__ == '__main__':
    main()
