# This is where the variables are

default persistent.progress = {
    "complete_ch_1": False,
    "complete_ch_2": False,
    "complete_ch_3": False,
    "complete_ch_4": False,
    "complete_ch_5": False,
    "complete_ch_6": False,
    "complete_ch_7": False,
    "complete_ch_8": False,
    "complete_ch_9": False,
    "complete_ch_10": False,
    "complete_ch_11": False,
    "complete_ch_12": False,
    "complete_ch_13": False,
    "complete_ch_14": False,
    "complete_ch_15": False,
}

# Default progress for launching a new game.
default episodes = [
    ["Prologue", True, "images/bg lab.jpg"],
    ["Chapter 1", True, "images/bg van.jpg"],
    ["Chapter 2", persistent.progress["complete_ch_1"], "images/bg road night.jpg"],
    ["Chapter 3", persistent.progress["complete_ch_2"], "images/bg spaceship.jpg"],
    ["Chapter 4", persistent.progress["complete_ch_3"], "images/bg villa.png"],
    ["Coming Soon", persistent.progress["complete_ch_4"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_5"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_6"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_7"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_8"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_9"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_10"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_11"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_12"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_13"], "images/bg black.jpg"],
    ["Coming Soon", persistent.progress["complete_ch_14"], "images/bg black.jpg"],
]

default persistent.pronouns = {
    "subject": {"Male": "he", "Female": "she"},
    "object": {"Male": "him", "Female": "her"},
    "possessive": {"Male": "his", "Female": "hers"},
    "determiner": {"Male": "his", "Female": "her"},
    "reflexive": {"Male": "himself", "Female": "herself"},
    "child": {"Male": "boy", "Female": "girl"},
    "adult": {"Male": "man", "Female": "woman"},
    "adults": {"Male": "men", "Female": "women"},
    "sibling": {"Male": "brother", "Female": "sister"},
    "offspring": {"Male": "son", "Female": "daughter"},
}

default persistent.tough_decisions_1 = {
    "TD1": None, # brother or supplies
    "TD2": None, # antidote or pull
    "TD3": None, # kill or spare
    "TD4": None, # tell or silent
    "TD5": None  # kill or capture
}

default persistent.romance_points = {
    "Terrence": 0,
    "Exaqlyon": 0,
    "Serpent": 0,
    "Br33t4ny": 0
}

default persistent.weapons = {
    "Bow and Arrows": True,
    "Fire Axe": False,
    "Light Sabre": False,
    "Qruy's Blaster": False
}

default persistent.side_quests_1 = {
    "An Abandoned Villa": False,
    "A Zombie Like Me": False,
    "An Alien Princess": False,
    "Into the Enemy's Lair": False,
    "Partner": None,
    "A Serpent's Past": False,
    "The Peculiar Cyborg": False,
}

default persistent.partner_pronouns = {
    "subject": {"Female": "he", "Male": "she"},
    "object": {"Female": "him", "Male": "her"},
    "possessive": {"Female": "his", "Male": "hers"},
    "determiner": {"Female": "his", "Male": "her"},
    "reflexive": {"Female": "himself", "Male": "herself"},
    "child": {"Female": "boy", "Male": "girl"},
    "adult": {"Female": "man", "Male": "woman"},
    "adults": {"Female": "men", "Male": "women"},
    "sibling": {"Female": "brother", "Male": "sister"},
    "offspring": {"Female": "son", "Male": "daughter"},
    "target": {"Female": "Terrence", "Male": "Exaqlyon"},
    "other": {"Female": "Exaqlyon", "Male": "Terrence"},
}

default persistent.healing_items = []
# This is the contents of healing_items:
# Medkit
# Obsidian Theta Lava

default persistent.outfits = ['Casual']
default persistent.outfit = persistent.outfits[0]

default persistent.met_uzi = False
default persistent.injured = False