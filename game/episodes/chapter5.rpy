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

    terrence "Seems like it. Welp, I\'m going to enjoy the view while we wait."

    "As everyone disperse, you make your way to a familiar path."

    exaqlyon "Going somewhere, [persistent.name]?"

    mc "Yeah... I\'d like to see {b}{color=#ff0000}him.{/cplor}{/b}"

    exaqlyon "Larx, go with [persistent.pronouns['object'][persistent.gender]], if anything goes wrong, report immediately."

    larx "Understood."

    "The tall alien guide you through the hallway, down to the bottom chamber..."

    "As you descend downward, you heard a soft giggle."

    serpent "{i}Hehehe...{/i}"

    "You see serpent play around with Jason, not realizing you both."

    mc "Enjoying ourselves, are we?"

    "Upon hearing your voice, he immediately looks your direction, eyes wary."

    "Jason immediately wraps himself on Serpent\'s neck."

    serpent "..."

    menu:

        mc "Why go quiet all of a sudden?"

        "Don\'t mind me, just passing by.":
            
            larx "What a filthy being, still able to stifle a laugh even in this moment."

            mc "I don\'t blame him, though. It could get pretty lonely in that cage."

        "You\'d think you can plot something without anyone noticing?":
            
            larx "I assure you, this cage will be the last thing he sees if he plots something."

    serpent "What do you want?"

    mc "Oh, so you {i}can{/i} speak after all."

    serpent "If you come here to kill me, just do it already."

    serpent "Otherwise you\'re just wasting time. Aren\'t you afraid I\'ll bust down this cage and kill you all?"

    mc "You won\'t."

    serpent "And why not?"

    mc "Because {i}{b}Spencer{/b}{/i} isn\'t a killer."

    "Serpent\'s eyes go wild, exactly like what you see in the lab."

    serpent "...Leave me alone."

    mc "No, I am {i}not{/i} leaving until..."

    menu:

        mc "Until..."

        "You apologize for everything!":
            pass

        "I hear what you have to say.":
            pass
    
    "Serpent goes quiet."

    serpent "You... you\'re their [persistent.pronouns['offspring'][persistent.gender]] aren\'t you?"

    mc "Who?"

    serpent "David and Betsheba... they\'re the only ones whom had actually asked my name..."

    mc "David\'s my father\'s name, Betsheba\'s my mom\'s."

    "Serpent looks at the ground, you can tell he\'s ashamed."

    mc "(Hmm... He seems rather conflicted.)"

    mc "(I bet if I pry more, I can listen his side of the story.)"

    mc "(How he got himself like this in the first place...)"

    tutorial "Spend some alone time with Spencer to get to know him, learn about his past, and earn his trust..."

    tutorial "What secrets could this monstrous mutant has in his past?"

    tutorial "And what can you do if he\'s on {b}YOUR{/b} side?"

    menu:

        "Side Quest: A Serpent\'s Past"

        "Ask Serpent about his past.":
            pass

        "Forget it.":
            pass

label premium5:
    
    call screen episodes
    return