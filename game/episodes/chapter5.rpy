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

    serpent "David and Betsheba... they\'re the only ones whom had actually asked for my name..."

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
            jump premium5

        "Forget it.":
            pass

label premium5:

    "You turned to Larx."

    mc "Can you excuse us? There\'s something I want to ask him."

    larx "Are you certain? This beast could--"

    mc "Just keep watch outside, I won\'t release him."

    larx "But--"

    mc "If something happened, I\'ll bang on the door and you\'ll know."

    larx "...Understood."

    "Larx bowed and leaves you two alone."

    "As the door closes, you sit down in front of Serpent\'s cage."

    mc "Well... Start talking."

    serpent "...What?"

    mc "Tell me your story, you owe me that much."

    "Conflicted, Serpent sighs."

    serpent "Fine, how old are you?"

    mc "This year I\'ll turn 20, but I\'m technically still 19 years old."

    serpent "Right, it all happened 20 years ago."

    scene bg village day
    with fade

    "{i}Now playing as Spencer.\n20 years ago...{/i}"

    "You stepped out from the van, holding Jason, your pet snake close to you. In front of you were your parents."

    dad "So this is it? The {b}{color="#0000ff"}Messenborough{/color}{/b} Village."

    mom "Not bad, for a village I\'d expect it to be filthier."

    dad "Watch your mouth, darling. We\'re here on a mission, remember?"

    "Your parents continued to chat, but you don\'t care. You kept your attention to your pet."

    spencer "I wonder what we can find in this village? Maybe a rat? A baby hamster? Or better... A dead zombie."

    jason "Hss..."

    "Jason wrapped himself around your left arm."

    "As the three of you went on to the front gate, a crowd emerged."

    fabien "Halt, outsiders. My name is Fabien, state your business before we could let you in."

    dad "We are the Edisons."

    "At that name, several villagers began to murmur."

    villager "It\'s {i}them.{/i}"

    villager "They\'re the scientists promised by the governments!"

    mom "We were told the land in your village is suitable to grow what we believed to be cure plant for this zombie apocalypse."

    dad "If you let us in, we promised not only would you be the first into taking this medicine, but the president will also favor you in the long run."

    fabien "And what about {i}him?{/i}"

    "At the sound of that, you lifted your head, noticing they were pointing at your direction."

    villager "Is that a snake?"

    villager "That boy is playing with a snake!"

    villager "Not just any kind, venomous ones! The kind that stops blood from clotting."

    villager "The {b}{color=#ff0000}Boomslang!{/color}{/b}"

    "The villager gasps."

    mom "I umm... I assure you this {i}child{/i} of mine possesses no harm whatsoever."

    dad "That\'s right! The snake has no venom anyway."

    "You felt offended, why would your father lied?"

    menu:

        spencer "Umm..."

        "But this {i}still{/i} has venom.":

            spencer "But this {i}still{/i} has--"
            
        "Since when do we took it out?":
            
            spencer "Since when do we took--"
    
    spencer "Mmff!!!"

    "Your mother immediately shut your mouth."

    mom "Isn\'t that right, {i}dear?!{/i}"

    "You saw your mother giving you the side eye. Leaving you no choice but to nod."

    fabien "Hmm... Well, do keep that snake in check, alright?"

    "The villagers finally let you in."

    "As you walk in, you notice a pair of husband and wife. The wife had a big belly, indicating she was pregnant."

    david "Hello there, umm... Lovely snake you have."

    spencer "Umm... Thanks."

    betsheba "What\'s your name?"

    spencer "His name is Jason."

    betsheba "Ah I mean {i}your{/i} name."

    spencer "Oh... It\'s Spencer."

    scene bg spaceship
    with fade

    "{i}Now playing as [persistent.name].\nPresent day...{/i}"

    serpent "At first it wasn\'t a huge deal, but overtime your parents started getting close to my family."

    serpent "Even {i}too{/i} close."

    mc "What happened?"

    scene bg village night
    with fade
    
    "{i}Now playing as Spencer.\n20 years ago...{/i}"

    call screen episodes
    return