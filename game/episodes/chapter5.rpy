label chapter5:
    
    if persistent.gender == 'Female':
        $ terrence_points = persistent.romance_points['Terrence']
        $ serpent_points = persistent.romance_points['Serpent']
    else:
        $ exaqlyon_points = persistent.romance_points['Exaqlyon']

    $ renpy.save_persistent()

    "Chapter 5: The Forgotten Soldier"

    scene bg spaceship
    with fade

    "The ship soars to the sky, you try your best to hold on and not blown away from the high current."

    mc "Hngghh..."

    "Your back against the door, you can only hope Exaqlyon knows you\'re outside."

    "BZT! The door swings open, pulling you inside."

    mc "Woah!"

    "You fall to the floor as the door closes again. When you lift your head, you see Exaqlyon and Terrence looking at you."

    terrence "Well well well... Look who decided to steal a ride."

    exaqlyon "{i}What{/i} were you thinking, [persistent.name]?!"

    menu:

        mc "I..."

        "I was worried about you all.":
            
            terrence "Barf."

        "Are you seriously abandoning me?":
            
            exaqlyon "You {i}do{/i} know my planet is not {i}your{/i} home planet, right?"

            terrence "[persistent.pronouns['subject'][persistent.gender].title()] knows, [persistent.pronouns['subject'][persistent.gender].title()]\'s just messing with us."

        "Sorry, I thought this was my bedroom.":
            
            terrence "Very funny."
    
    exaqlyon "Seriously, though. Are you out of your mind?"

    mc "Look, I know it was very selfish of me..."

    if persistent.tough_decisions_1["TD2"] == "antidote":

        mc "Not to mention my leg is due to my recklessness."
    
    else:

        mc "I also planned very poorly..."

        "You looked at Terrence\'s left arm."
    
    mc "But all my life I\'ve been living inside a wall, and people expect me to be able to defend myself..."

    mc "Well, how am I going to do that if I simply don\'t have enough experience?"

    terrence "By going up against a literal alien?"

    mc "Worst case scenario, I\'ll die. But I feel the danger everyday."

    mc "So I\'m not taking a rest simply because it has nothing to do with me, not anymore."

    exaqlyon "Suit yourselves, fair warning though, this is going to be rough."

    exaqlyon "Even more brutal than before."

    "Exaqlyon looks at Terrence."

    terrence "What?"

    exaqlyon "You\'re coming, aren\'t you? I can sense it in your mind."

    terrence "Is there anything good for me here? No, right? Might as well kick some Alien butts."

    exaqlyon "Alright, so we\'re doing this together again."



    call screen episodes
    return