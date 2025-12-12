label chapter2:
    
    if persistent.gender == 'Female':
        $ terrence_points = 0
        $ persistent.romance_points['Terrence'] = 0
        $ renpy.save_persistent()

    "Chapter 2: A 'Normal' Zombie"

    "You're awake with a start."

    mc "Ugh... what?"

    "You open your eyes, you're lying on a... bed?"
    
    "You look around and realize you're no longer in the street, you're in a cabin-like building."
    
    "A candle illuminates the room from beside you."

    mc "Where the hell am I?"

    "The memory of that... man from earlier still haunts your mind."
    
    "Suddenly, the door knob turns, and the door slowly opens."

    mc "..."

    "The creature walks in, a teapot in his left hand, while in his tentacles are a cup, a bag of sugar and a teaspoon."

    placeholder "So you're awake."

    "He sits beside you and you recoil instantly, keeping a far enough distance."
    
    "He pays you no mind, he pours a liquid from the teapot into the cup, followed by some sugar, and then stirring it before handing it to you."

    placeholder "Here."

    menu:

        "A cup of liquid."

        "Ummm... thanks?":
            pass
    
    menu:
        
        mc "Uhh... Is this..."

        "Tea?":

            placeholder "My god, again with the questions!"

            placeholder "Drink your damn tea, or throw it to the floor if you don't want it!"

            mc "Okay okay! Point taken, sheesh."

        "Poison?":

            placeholder "My god, again with the questions!"

            placeholder "If I wanted you dead I'd have left you on the street! So what's that liquid to you?"

            mc "You don't have to be mad about it..."
        
    "You sip your tea as you both sit in an uncomfortable silence."

    placeholder "...Sorry If I'm being rude and secretive. This body isn't really fit for greeting guests."

    mc "I also apologize if I pushed you too far. I was taught that I shouldn't trust strangers during the zombie apocalypse."
    
    mc "But thank you, by the way, for saving my life."

    placeholder "Don't mention it. I'm Terrence."

    mc "[persistent.name]."

    "You move closer to him, mind filled with millions of questions but you're unsure of asking them."

    terrence "So uhh... You must have a {i}lot{/i} of questions right?"

    mc "Uh-huh."

    terrence "{i}Sigh{/i}... Okay, I'll answer one question of yours."
    
    terrence "But only one. Okay?"

    if persistent.gender == "Female":
        
        tutorial "You just meet your potential {b}Love Interest{/b} for the story, which means you flirt with him."
        
        tutorial "Every love interests in this game are Non-Humans."

        tutorial "Alternatively, you can choose not to if you don't like it. Every romance options are marked with the 💗 symbol."
    
    menu:

        mc "In that case..."

        "What are you?":

            terrence "I'm a zombie."

            terrence "And no, I'm not who you think I am. I'm not like other zombies, and they're nothing like me."

            terrence "The truth is... I don't even know {i}why{/i} I'm different."

        "Is this your house?":

            "Terrence snorts."

            terrence "Heh, I wish. I've stayed in this house ever since I'm a zombie."

            terrence "I don't know what happened to the owner. It's not much, but just {i}enough{/i} for a zombie like myself."

        "💗 Are you single?" if persistent.gender == "Female":
            
            $ terrence_points += 1

            terrence "Ex-{i}cough{/i} Excuse me?"

            "Terrence looks back at you, his cheeks turn slightly red."

            mc "Sorry, didn't mean to make you nervous."

            terrence "Of all the questions you could've asked... you chose {i}that{/i}?"

            "Terrence shakes his head while you chuckle. After a while, he continues speaking."

            terrence "Well... I suppose I {i}am{/i} single, it's a little too late for me now though, and I can't date a human too, you know?"

            mc "Why?"

            terrence "Because I'm a {i}zombie{/i}."

    "Terrence stands up."

    terrence "Well, that's all you're getting out of me."

    mc "But--"

    terrence "Ah ah ah, one question, remember?"

    terrence "Now let me take you back."

    "He offers you his hand."

    menu:

        mc "(I should...)"

        "💗 Take his hand." if persistent.gender == "Female":

            $ terrence_points += 1

            "You take his hand, slipping your fingers between his."
            
            "His hand feels cold, and a little sharp because of his bones."

        "Take his hand." if persistent.gender == "Male":

            "You take his hand, it feels cold, and a little sharp because of his bones."

        "Stand up without assistance.":

            "You stand up without assistance."

            "With a shrug, he leads you to his door."
    
    terrence "Let's go."

    if persistent.side_quests_1["An Abandoned Villa"]:

        terrence "Oh, and don't forget this."

        "Terrence hands you a med kit. It was the med kit you found with Azure in the Abandoned villa."

        mc "Oh... thanks."

        "You take the medkit, and then follow him out."

    "You both step outside his house, past some alleys where you last see him."

    mc "It looks like dawn is already rising."

    terrence "Okay, you {i}should{/i} be knowing your way now. Just go down this path, and--"

    mc "Wait, you're not coming?"

    terrence "Hell no, taking you to my house already exposed a lot of me."
    
    terrence "You will return to your peaceful village and I'll continue being myself, we'll never speak about this {i}ever again{/i}."

    mc "(Hmm... Terrence seems to hide a lot of himself, I bet I could persuade him to open up.)"
    
    mc "(And having a zombie with human consciousness is {i}definitely{/i} useful for an ally.)"

    tutorial "Who is this mysterious zombie? Can you convince him into becoming your ally?"

    tutorial "Convince Terrence to join you to not only get him to open up, but a chance to learn some survival skills."

    menu:

        "Side Quest: Zombie Like Me."

        "Take Terrence with you.":
            
            mc "You should come with me, Terrence."

            terrence "I told you I--"

            mc "I'm not sure about these streets, and if you {i}really{/i} want to save me, you'll make sure I arrive safely."

            terrence "You're really pushing the boundaries of my generosity here!"

            mc "I won't be a burden, I promise."

            "Terrence goes silent, eventually he steps forward."

            terrence "Fine. Let's get this over with."

            "As you walk down the road. You notice Terrence is gazing into the distance."

            mc "So, you mind if I ask questions? Or do you prefer to walk in silence?"

            terrence "...Fine, but only because this night air brings me in a good mood."

            $ opt1 = False
            $ opt2 = False
            $ opt3 = False

            call loop2

            "After a while, you both come to a bridge on top of a river."

            terrence "Ahh... this is my favourite spot every time I need to clear my head. The sound of water here always puts my mind at ease."

            "You stand beside him on the bridge, you can see his face shining in the moonlight."

            if persistent.gender == "Male":

                mc "So... do you come here often?"

                terrence "Every time it's possible, though I'm mostly alone."

                mc "Well, now you have a friend with you."

                terrence "Friend? Me? Come on now."

                "He chuckles, the terrifying zombie does have a sense of humor."

            else:

                menu:

                    mc "Terrence..."

                    "💗 You look cute.":
                        
                        $ terrence_points += 1

                        "Terrence raises an eyebrow, he looks at you strangely."

                        terrence "Are you saying that because you don't know what else to say?"

                        mc "I'm serious, you look dashing... for a zombie."

                        "Terrence smiles, sliding a little closer to you."

                    "Do you come here often?":
                        
                        terrence "Every time it's possible, though I'm mostly alone."

                        mc "Well, now you have a friend with you."

                        terrence "Friend? Me? Come on now."

                        "He chuckles, the terrifying zombie does have a sense of humor."
            
            terrence "You know, [persistent.name]. I don't usually feel this way around people."

            mc "What about zombies?"

            terrence "Not so much, but maybe because I spent a lot of time on the--"

            terrence "MOVE!"

            "All of the sudden, he pulls you aside!"

            mc "What's--"

            terrence "Hrah!"

            zombie "Grrgghhh..."

            "The zombie goes down, you see two more coming after you both."

            terrence "[persistent.name], you know how to fight right?"

            mc "Kind of? I mean, yeah… a little. I'm trained with bow and arrows."

            terrence "Good, make sure to aim at the {color=#FF0000}{b}vulnerable organs that visibly appear{/b}{/color}."

            mc "You mean the brain?"

            terrence "That sometimes won't work, some zombies have sturdy skeletons."

            "You observe one of the zombies that comes, you see blonde hair from its {color=#FF0000}{b}head{/b}{/color}, some moss from its {color=#FF0000}{b}left wrist{/b}{/color}, and its {color=#FF0000}{b}stomach{/b}{/color}."

            $ fight = 0

            menu:

                mc "(I should aim my arrow...)"

                "At the head.":
                    
                    "Your arrow hits its target, but the zombie keeps marching forward."

                    zombie "Gragghh..."

                    mc "Oh no."

                    terrence "[persistent.name]!"

                    "Terrence delivers a jab to the zombie's stomach, it crumples down and stays still."

                    zombie "Arghhh..."

                    mc "Thanks for that."

                "At the wrist.":
                    
                    "Your arrow hits its target, but the zombie keeps marching forward."

                    zombie "Gragghh..."

                    mc "Oh no."

                    terrence "[persistent.name]!"

                    "Terrence delivers a jab to the zombie's stomach, it crumples down and stays still."

                    zombie "Arghhh..."

                    mc "Thanks for that."

                "At the stomach.":
                    
                    $ fight += 1

                    "Your arrow hits the zombie's stomach and it crumples down in pain."

                    zombie "Hsss..."

                    mc "And stay down!"
            
            "The other zombie gets away from Terrence, running slightly faster to you."

            menu:

                mc "..."

                "Dodge and observe!":

                    $ fight += 1

                    "You dive out of the way, and spots the {color=#FF0000}{b}kidneys{/b}{/color} from its back!"

                    mc "(There!)"

                    "You grab your arrow and stab it into its kidney."

                    zombie "Grggkk..."

                    terrence "Nice move."

                "Shoot its skull!":

                    "Forgetting Terrence's advice, you shoot an arrow into its skull, but it only gets even angrier."

                    zombie "Hrrggghhh..."

                    mc "Oh no!"

                    terrence "Get off [persistent.pronouns['object']]!"

                    "Terrence finishes the zombie, and it stays still."
            
            "After the crisis has been dealt, Terrence looks at you."

            if fight == 2:

                terrence "You're doing good out there, I'm impressed."

            elif fight == 1:

                terrence "Not bad, a little more practice and you should be fine."

            else:
                
                terrence "Well {i}that{/i} was a disaster."
            
            terrence "Come on, let's continue our journey."

            "You continue your walk with Terrence..."

            "After a while, the front gate of your colony begins to appear."

            terrence "Alright, I'm serious now, this is the furthest I can take you."

            if persistent.gender == "Male":

                mc "Thanks for walking me back home, Terrence. The world needs more zombies like you."

                terrence "Yeah well, whatever. Just doing what I always do."
            
            else:

                menu:

                    mc "..."

                    "Thank him.":

                        mc "Thanks for walking me back home, Terrence. The world needs more zombies like you."

                        terrence "Yeah well, whatever. Just doing what I always do."
                    
                    "💗 Hug him.":

                        $ terrence_points += 1

                        'You hug Terrence close, feeling the surface of his chest as he\'s taken by surprise.'

                        terrence "[persistent.name]!"

                        "At first, he tenses, but later returns the hug."

                        terrence "Pleasure's all mine [persistent.name]."
            
            terrence "Now please leave me alone."

            mc "Alright, bye Terrence."

            $ notify("A Zombie Ally", "You get to know Terrence better.")

            $ persistent.side_quests_1["A Zombie Like Me"] = True

        "Part ways":
            
            mc "This is goodbye then."

            terrence "Yeah, goodbye."

            $ notify("Solo Mission", "You part ways with Terrence.")
        
    "You start to go when..."

    terrence "Oh, and [persistent.name]?"

    mc "Yeah?"

    terrence "Please don't tell anyone about this, if anyone knows I have a human consciousness they'll lock me in a cell and start doing experiments."
    
    terrence "I know something like this is unique, but curiosities are what caused this disaster in the first place."
    
    terrence "The more curiosities appear, the more dangerous the world will be."

    mc "...You got it Terrence."

    "You continue walking to your colony. Many pairs of eyes spot you as you walk down the streets... Into Azure!"

    azure "[persistent.name]!"

    if persistent.tough_decisions_1["TD1"] == 'supplies':

        "...and your parents."
    
    else:

        "...along with Lee and your parents."
    
    dad "[persistent.name]! There you are."

    mom "We were so worried."

    if persistent.tough_decisions_1["TD1"] == "supplies":

        mom "We just lost your brother, the idea of losing you too... I just..."

        mc "I'm here mom, I'm not going anywhere."

        azure "Where were you anyway?"
    
    else:

        lee "Hehe, you handled yourself well, kid."

        mc "Thanks?"

        lee "Are you gonna tell us where you've been?"
    
    mc "I... got surrounded by zombies, so I camped out till daylight."
    
    mc "Speaking of daylight, I think I'll pass out now, I didn't sleep last night."

    mom "Of course, let's get you to bed."

    "Your mother takes you for a check up. Making sure you haven't been bitten by zombies."

    "After the check has been completed, she takes you inside your house."

    "Upon arriving, you put your weapons on the floor and lay down on the bed, mind racing after everything that has happened."

    mom "...Here."

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        "Your mother gives you a glass of water, which you drink instantly."

        "You didn't realize just how thirsty you've been. You realize her expression."
    
    else:

        "Your mother gives you a new bag, along with a glass of water."

        "You drink the water she gave you, and put your stuff in the bag."

        "You finally realize her expression."
    
    mc "Mom..."

    "Without a word, she hugs you close."

    mom "I thought I lost you... Ever since you're gone, I can't stop thinking about whether or not..."

    mc "Whether or not what?"

    mom "...Whether or not letting you hunt was a good idea."

    "Her words left an unbearable silence in the air."

    mom "I'm sorry, I shouldn't--"

    mc "Mom, do you think I'm not ready?"

    mom "I didn't say that... I..."

    mom "You know what? That doesn't matter right now, you need to rest."

    "You want to argue back, but you don't have the energy to."

    "You lay your head on the bed as your mom straddles your hair, you glance out the window... and you see an old, abandoned house in the distance."

    mc "Mom... who lives in that house?"

    "Your mother follows your gaze, and her expression suddenly turns sour."

    mom "...I always knew they were trouble."

    menu:

        mc "..."

        "They?":

            pass

        "What happened?":

            pass
    
    mom "When I was pregnant with you, a couple of people came into our village. They wore white robes, claiming to be scientists."

    mom "They said they've been researching the cause of this apocalypse, and thought they knew the cure."

    mom "They brought with themselves a special seed, saying that the ground here is perfect to grow a plant to cure the infected. So we let them stay."

    mom "After all, they promised that we would be the first one to obtain this 'medicine'."

    mc "And then what happened?"

    mom "At first it was fine, everyone was just minding their business..."

    mom "But as the days go on, they became more... demanding."

    mom "They were asking resources, always with the same excuse, saying it was for their research purposes."

    "You notice her voice starting to get angry."

    mom "Who did they think they are? We were already struggling to fit our daily needs, and they just took like they own everything."

    mom "...At least their son is not so bad."

    mc "They had a son?"

    mom "Yes, his name is {color=#FFFF00}{b}Spencer{/b}{/color}. He likes to help out the villagers, though I can't say we are close."

    mom "He has this pet snake named {color=#00FF00}{b}Jason{/b}{/color} and it always cling to his neck, so we always keep our distance."

    mc "How old was he?"

    mom "Around your age."

    mc "So 20 years old?"

    mom "Back {i}then{/i}, yes. But I don't even know if he's alive today."

    mc "What happened?"

    mom "One day my water broke, so I have to give birth to you."

    mom "During that time we heard a huge explosion from the house, it didn't take long until the S.W.A.T team started locking in the place."

    menu:

        mc "So..."

        "Did the boy survive?":

            mom "Nobody knows for sure. No one ever saw him."

            mc "So he could still be alive right? 20 years isn't a lifetime."

        "The experiment failed?":

            mom "It was a total disaster! All those days in this village and what did they give us?"

            mom "Nothing! At least karma finally got to them."

            mom "Serves them right if you ask me."

    mc "Mom... What happened to them?"

    mom "They're dead [persistent.name], their bodies look like they had been attacked by a savage beast."

    mom "...Except for the son, who had never been seen again."
    
    mom "Anyway, since then, the house has been labeled {i}{b}The Failed Experiment.{/b}{/i}"
        
    "You take a look at the house again. Mind filled with curiosities."

    mom "Now I know that look, and no! You are not allowed to be near that place!"

    mc "But mom--"

    mom "No buts [persistent.name]! I know you want to see the world."

    mom "But this world is cruel. And we're lucky to have made it this far."

    mom "Keep pushing luck, and one day luck will push you back!"

    "And with that, your mom leaves you alone in the room."

    "Exhausted, you close your eyes..."

    # Change backdrop here

    "{i}Now playing as Lee.\n10 years ago...{/i}"

    mc "Are we there yet? Can I open my eyes now?"

    "You close your little [persistent.pronouns['sibling']]'s eyes as you walk inside your house."

    "It was your [persistent.pronouns['sibling']]'s 10th birthday, and you've planned a surprise party for [persistent.pronouns['object']]."

    lee "Almost there kiddo."

    "As you walk inside the room, you saw everyone had taken their position."

    lee "Alright, now open your eyes."

    "[persistent.name] opened [persistent.pronouns['determiner']] eyes and..."

    everyone "SURPRISE!!! HAPPY BIRTHDAY [persistent.name]!"

    mc "Oh wow! Thank you, thank you."

    "Your parents came over to give your [persistent.pronouns['sibling']] a hug."

    dad "Happy birthday my [persistent.pronouns['offspring']]."

    mom "You are now 10 years old."

    "As your [persistent.pronouns['sibling']] starts blowing [persistent.pronouns['object']] candle and ate [persistent.pronouns['object']] birthday cake, it was time to open the presents."

    mc "Oohh... this one is from Lee."

    "[persistent.pronouns['subject'].title()] opened [persistent.pronouns['determiner']] present... Turns out it was a mini bow."

    mc "Wow... An actual bow for shooting!"

    "The crowds suddenly went quiet. Your saw your parents looking at you."

    "Despite that, you walk to your [persistent.pronouns['sibling']] with a smile."

    lee "That's right, kiddo. One day, I will take you to hunt and you will become a fighter just like your big bro."

    mc "Realy? Oh thank you, thank you!"

    "[persistent.pronouns['subject'].title()] hugged you tightly."

    mc "I love you, Lee. You're the best brother ever!"

    "[persistent.pronouns['subject'].title()] left the room happily as your parents approached you."

    dad "Son... Are you sure [persistent.pronouns['subject']]'s ready?"

    lee "Relax dad, [persistent.name] still has a long way to go."

    lee "Besides, it took me 5 and a half years to finish my training."

    mom "But you started at 12 years old. Your [persistent.pronouns['sibling']] is still too young."

    lee "Don't worry mom, I'll make sure [persistent.name] is ready. I swear on my life."

    lee "And when [persistent.pronouns['subject']]'s ready, I'll trust [persistent.pronouns['object']] with the {color=#00FF00}{b}key{/b}{/color} to our secret {color=#00FF00}{b}supplies.{/b}{/color}"

    "But even as you said that, you can't stop but feeling worried..."

    "..."

    "...Worried that something could happen to your [persistent.pronouns['sibling']]..."

    # Change backdrop here

    "{i}Now Playing as [persistent.name].\nPresent time.{/i}"

    "You're awake with a start."

    mc "...Huh?"

    "KRIIING... An loud sound echoes through the room, it's an {b}alarm!{/b}"

    mc "We're under attack!"

    "You quickly takes your stuff and run outside."

    "As you run outside your house, you spot Azure rushing toward the Town's Hall."

    mc "Azure, wait!"

    azure "[persistent.name]? What are you doing? Aren't you supposed to be resting?"

    menu:

        mc "Yeah well..."

        "It's time to do something stupid.":
            
            mc "I've just had a very bad luck yesterday. I guess it's time to even the odds."

        "I can't just stand here while people are risking their lives!":
            
            mc "Do you think I can just let you have all the fun killing dead bodies?"

            mc "Not a chance."
    
    "Azure grins at you."

    azure "Well come on then, let's do this together."

    "Azure leads you toward the main hall. Dozens of people gather already, weapons ready for battle."

    "In the center of the crowd, Fabien stands on a wooden crate, giving a motivational rally."

    fabien "Remember folks, just like every other battle, what you're about to do today will be remembered as something heroic."

    fabien "You're putting your lives on the line to keep us going."

    fabien "I assure you, whatever happens out there, one thing is for sure. Victory will be on our side!"

    "The crowd cheer."

    everyone "Hear Hear!"

    fabien "Now prepare yourself at the front gate. And remember, look out for each other."

    fabien "I don't want to have to use this."

    "Fabien reveals a {color=#FF0000}{b}glock{/b}{/color} beneath his jacket."

    mc "(Gulp...)"

    "As the front gate to your village opens, several villagers let out a battle cry."

    villager "YEAHH!!!"

    villager "RAGHHH!"

    azure "For the village!"

    "You're about to let out a battle cry... When you hear your mother's voice!"

    mom "[persistent.name]? [persistent.name.upper()]! Did anyone see my [persistent.pronouns['offspring']]?"

    "You look back and see your mother looking around in a panic."

    mc "(Sorry mom... But I have to do this.)"

    "You go the other way to battle."

    "The battlefield is a chaos, dozens of zombies rush toward your village."

    "You look around... looking if you can help anyone."

    tutorial "From now on, if you get too many wrong choices in combat, you will get {color=#FF0000}{b}injured{/b}{/color}!"

    tutorial "If you get injured, the future fights will be harder."

    tutorial "Injuries can only be healed if you have {color=#00FF00}{b}healing items{/b}{/color} with you."

    "Up ahead... You see Azure slashing a huge zombie with [persistent.pronouns['determiner']] daggers."

    default combat_points = 0

    "On your left, you see a group of guys setting something on the sand..."

    if persistent.tough_decisions_1['TD1'] == "brother":

        "On your right, you see Lee looking into the distance."
    
    menu:

        mc "(Who should I help?)"

        "Azure":
            jump chapter2_azure

        "The three guys":
            jump chapter2_uzi

        "Lee" if persistent.tough_decisions_1['TD1'] == 'brother':
            jump chapter2_lee

    jump chapter2_resolution

label loop2:

    menu:

        mc "I want to ask..."

        "How come you're different from other zombies?" if not opt1:
            
            $ opt1 = True
            
            terrence "I don't exactly know how I got to this point, honestly."
            
            terrence "But I guess it has something to do with when I was buried."

            mc "You mean... You died when the 'incident' happened?"

            terrence "You could say that, I drowned in the ocean because an octopus pulled me under."

            terrence "Guess that explains these tentacles."

            mc "And... the human consciousness?"

            terrence "Beats me, I'm still looking for an answer."

        "Do you know how to stop this apocalypse?" if not opt2:
            
            $ opt2 = True

            terrence "For that, you gotta fix the {i}source{/i} of the problem to stop it from spreading."

            mc "So to stop this madness, we have to find the source."

            terrence "That's what I thought, but honestly, that might be impossible."

            mc "How so?"

            terrence "Because that would mean we need to kill the {color=#FF0000}{b}queen.{/b}{/color}"

            mc "The... the queen?"

            "Terrence doesn't answer, you realize his pained expression."

            terrence "Yeah, let's not talk about that."

        "Why are you fighting your own kin?" if not opt3:
            
            $ opt3 = True

            terrence "What's {i}that{/i} supposed to mean?"

            mc "You're a zombie too, why didn't you... I don't know, just stay out of sight maybe?"

            "Terrence lets out a bitter laugh."

            terrence "Say, if you see a human doing violence to... an animal for example."
            
            terrence "Would you just stay out of their sight and pretend nothing's happening?"

            mc "Of course not, how could you ask such a thing?"

            terrence "You're both humans, aren't you?"

            mc "...Noted."

            terrence "I might be a zombie, but I still have my humanity."

    if opt1 and opt2 and opt3:
        return

    else:
        jump loop2

label chapter2_azure:
    
    "You run to Azure, [persistent.pronouns['subject']] is slashing the giant zombie in a single sweep with [persistent.pronouns['determiner']] daggers."

    azure "Hyah!"

    zombie "Grr..."

    mc "Azure!"

    "[persistent.pronouns['subject'].title()] doesn't hear you, instead [persistent.pronouns['subject']] leaps back as the zombie rushed toward you!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter2_timer_out1'
    show screen countdown 

    menu:

        mc "Uh oh..."

        "Hesitate!":

            hide screen countdown
            jump chapter2_timer_out_1

        "Dive out of the way!":

            hide screen countdown
            
            $ combat_points += 1

            "You dived out of the way as the zombie runs past you."

            mc "Phew."

            azure "Nice save [persistent.name]!"

            "The zombie trips and falls face-first to the ground."

            zombie "Urkk..."

            "However, the zombie seems more enraged than ever."

            jump chapter2_azure_1
        
        "Stare!":

            hide screen countdown
            jump chapter2_timer_out_1

label chapter2_timer_out1:

    "You didn't move..."

    azure "[persistent.name]!"

    "The zombie rams into you, causing you to fly backwards."

    mc "Agh!"

    "You collided with the rocky ground, you feel pain in your back."

    mc "Aww..."

    azure "You okay?"

    "[persistent.pronouns['subject']] gives you a hand and you take it as you stand up."

    "Meanwhile, the zombie looks more enraged than ever."

    jump chapter2_azure_1

label chapter2_azure_1:
    
    zombie "Hrr..."

    mc "What {i}is{/i} that thing, Azure?"

    azure "It seems like that zombie is {color=#0000FF}{b}mutated{/b}{/color}."

    mc "Any ideas on how to defeat it?"

    azure "Its skin is so thick, my blades can't cut through."

    azure "However it {i}seems{/i} like it likes charging at other people."

    zombie "Blarghhh!"

    "The zombie readies itself again, charging toward you both."

    azure "Here it is again, any ideas?"

    "You look around, you spot an old {b}Metal Car{/b}, a {b}Wind Turbine{/n}, and a big {b}cactus{/b}."

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter2_timer_out2'
    show screen countdown

    menu:

        mc "Azure, let's lure that thing into the..."

        "Metal Car!":
            
            hide screen countdown

            azure "Are you sure it's a good idea?"

            mc "Trust me."

            "You both run toward the rusty metal car. The huge zombie follows close."

            "As the zombie gets close, you two jump out of the way..."

            "BRAK! The zombie collides with the metal car, sending debris everywhere."

            zombie "Grkk..."

            "...But a few pieces of shrapnels fly over at your direction! Some cuts your cheek!"

            mc "Aghh!"

            azure "Ouch!"

            "You fell your wound, you see blood all over your palm."

            mc "That is gonna leave a mark."

            "Meanwhile, the zombie comes out of the wreckage, still as enraged as ever..."

            zombie "Grr..."

            azure "We need to kill this bastard!"

            jump chapter2_azure_2

        "Wind Turbine!":
            
            hide screen countdown
            $ combat_points += 1

            "You both run toward the wind turbine. The blade is spinning rapidly."

            azure "Are you sure this will work?"

            mc "Honestly? Not so much, let's just hope this zombie is strong enough to knock the turbine."

            "As the zombie gets closer, you both jump out of the way."

            zombie "Grk!"

            "The zombie collides with the sturcture with great force! The wind turbine goes down with its turbine still spinning!"

            zombie "Aghh-gahg-argh!!!"

            "The turbine slices the zombie, blood spraying everywhere."

            azure "Yes!"

            mc "Phew..."

            "However, the zombie still manages to stand up..."

            zombie "Grahhh!"

            azure "What the hell? It's still alive?"

            jump chapter2_azure_2

        "Cactus!":

            hide screen countdown
            $ combat_points += 1

            azure "I don't know... that cactus looks fragile."

            mc "It's more sturdy than you think, come on."

            "The two of you run to the cactus, its spikes stick out sharply."

            zombie "Grahh!"

            "As the zombie gets close, you two jump out of the way."

            zombie "Grkk!"

            "The zombie collides with the cactus, the cactus' spikes piercing its skin."

            azure "Whoo hoo! Have that."

            mc "Don't get too excited yet, look!"

            "The zombie pushes itself from the cactus."

            "Although the spikes stick out from its body, it's still moving as if nothing's happening."

            azure "Seriously? How is it still moving? It's a cactus!"
            
            jump chapter2_azure_2

label chapter2_timer_out2:
    
    "You can't come up with a plan..."

    azure "To where, [persistent.name]?"

    mc "Umm... Uhh..."

    "The zombie gets closer to you both."

    azure "Ah screw it!"

    "Azure pulls you aside to the metal car."

    "As the zombie gets close, you two jump out of the way..."

    "BRAK! The zombie collides with the metal car, sending debris everywhere."

    zombie "Grkk..."

    "...But a few pieces of shrapnels fly over at your direction! Some cuts your cheek!"

    mc "Aghh!"

    azure "Ouch!"

    "You fell your wound, you see blood all over your palm."

    mc "That is gonna leave a mark."

    "Meanwhile, the zombie comes out of the wreckage, still as enraged as ever..."

    zombie "Grr..."

    azure "We need to kill this bastard!"

    jump chapter2_azure_2

label chapter2_azure_2:
    
    if persistent.side_quests_1['A Zombie Like Me']:

        "You remember your encounter with Terrence earlier..."

        "...How he said to {b}{i}observe{/i}{/b} for any vulnerable organs."

        mc "Wait, I know how to kill this zombie!"

    else:

        mc "Hitting it blindly won't do anything, Azure."

        mc "We need to find its {b}weakness{/b}!"
    
    "You suddenly rush forward to meet the zombie head on."

    azure "[persistent.name], wait!"

    if persistent.side_quests_1['A Zombie Like Me']:

        "The zombie swings its arm at you, but you evade it easily, since your intention isn't to grapple with it."

        "You notice its exposed kidneys on its lower back!"

        mc "There!"

        "The zombie takes a giant swing! Before you somersault back out of the way."

        zombie "Hrr?"

        "It loses balance and fell with its back on top."

        menu:

            "You take aim with your bow... and..."

            "Shoot!":

                $ combat_points += 1

        "{i}SHKK!{/i} The arrow sticks into the kidneys, causing blood to erupt from it."

        zombie "AUGHHHHH!"

        "The zombie stays completely still... dead."

        azure "That was amazing, [persistent.name]!"

        "Azure punches you in the back, hard!"

        mc "Aw! What was {i}that{/i} for?"

        azure "For not telling me your idea!"

        jump chapter2_resolution
    
    else:

        "As you approach the zombie, it swings its arm at you."

        mc "Whoa..."

        "You evade it barely, looking for a weakness."

        "You spot its {color=#FF0000}{b}skull{/b}{/color} visible from its scorched head, a {color=#FF0000}{b}muscle tendon{/b}{/color} on its arm, and its {color=#FF0000}{b}kidneys{/b}{/color} visible from its back."

        "Grabbing your bow and arrow, you take aim..."

        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'chapter2_timer_out3'
        show screen countdown

        menu:

            mc "I should shoot my arrow on its..."

            "Skull!":

                hide screen countdown

                "Your arrow hits the skull, but gives no effect."

                jump chapter2_timer_out3_1

            "Tendons!":

                hide screen countdown

                "Your arrow hits the muscle, but gives no effect."

                jump chapter2_timer_out3_1

            "Kidneys!":

                hide screen countdown
                $ combat_points += 1

                "Your arrow hits the kidney! Blood spraying all over the place."

                zombie "AUGHHHH!"

                "It falls to the ground, dead."

                azure "That was amazing, [persistent.name]!"

                "Azure punches you in the back, hard!"

                mc "Aw! What was {i}that{/i} for?"

                azure "For not telling me your idea!"

                jump chapter2_resolution

label chapter2_timer_out3:
    
    "You can't tell where to aim the arrow..."

    jump chapter2_timer_out3_1

label chapter2_timer_out3_1:

    mc "Uh oh..."

    "Enraged, the zombie caught you off guard, and pins you to the ground."

    zombie "GRAGHHH!!!"

    "It grabs your neck, cutting the airflow."

    mc "Hff... Hff..."

    "As you almost run out of oxygen, the zombie suddenly writhes in pain."

    zombie "AUGHHH!"

    "It fell to the ground, dead."

    azure "Are you okay?"

    mc "Hff... {i}yeah... I'm good.{/i}"

    "[persistent.pronouns['subject'].title()] helps you up."

    jump chapter2_resolution

label chapter2_uzi:

    $ persistent.met_uzi = True
    
    "You go toward the three guys, they are setting something on the sand."

    mc "What are you guys doing?"

    placeholder "We're setting a trap."

    placeholder "An {color=#FF0000}{b}explosive{/b}{/color} trap."

    "A smaller guy with a ponytail on his head speaks up."

    placeholder "That's a bit of a stretch, but yeah, we're planning to detonate these bastard."

    "The two men cheered."

    placeholder "You're the man, Uzi."

    placeholder "This plan is your best one yet."

    uzi "Focus, idiots! Now's not the time for praisin'."

    uzi "Anyway, what do you say your name was, kid?"

    mc "I didn't, it's [persistent.name]."

    uzi "Alright [persistent.name], here's the plan..."

    uzi "We have a bunch of {color=#FF0000}{b}bombs{/b}{/color} buried in the sand here."

    placeholder "Don't ask where we got those."

    uzi "These bombs will surely cause a huge explosion, but we need the zombies to be in its blast radius."

    uzi "At the same time, we have to {b}get out of the scene{/b} ourselves otherwise we'll be {color=#FF0000}{b}injured{/b}{/color}."

    uzi "We need someone to {color=#00FF00}{b}distract{/b}{/color} the zombies, but both Ryan and Jack here will be too busy setting up the bombs."

    mc "Then why don't {i}you{/i} go and lure them?"

    ryan "Hey, watch your mouth little [persistent.pronouns['child']]!"

    jack "Yeah, that's our boss you're talking to!"

    uzi "You heard them, if I'm gone, then these idiots would perish as well."

    uzi "But maybe YOU can."

    menu:

        mc "..."

        "Okay, bring it on.":
            
            uzi "Really? You'd do it?"

            mc "If you're really as capable as your men say, then you'll keep me safe."

            mc "So yeah."

            "Uzi looks offended, but shrugs it off."

        "Hell no.":
            
            uzi "You'll be fine. As long as I'm in charge, nobody gets left behind."

            mc "But--"

        "Why me?":
            
            uzi "Because I say so, that's why."
    
    uzi "Now come on! Clock's ticking."

    "Uzi brings you forward, you see several villagers fighting the zombies."

    uzi "Grab their attention and bring those zombies toward that spot over there."

    "You look at the direction he's pointing. The spot is surrounded by 4 stones, forming a square."

    uzi "When you're done, make sure to {b}cover yourself!{/n}."

    "And just like that, uzi runs back to their men."

    mc "Ho boy, what did I just get myself into."

    "You tried your best to get the zombies' attention!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter2_timer_out4'
    show screen countdown

    menu:

        mc "(I should shout...)"

        "Over here, corpse face!":
            hide screen countdown
            $ combat_points += 1

        "Free Robux!":
            hide screen countdown
            $ combat_points += 1

        "ROAR!!!!!":
            hide screen countdown
            $ combat_points += 1
    
    "Some zombies are enraged by your shout, so they chase you instead."

    jump chapter2_uzi_1
    
label chapter2_timer_out4:
    
    "You didn't say anything..."

    "At the same time, a wild arrow fly toward you! The arrow cuts your shoulder."

    mc "Ack!"

    "Your shout managed to grab the zombies' attention, making them chasing you instead."

    jump chapter2_uzi_1

label chapter2_uzi_1:

    mc "That's it, come to me."

    "You bring the zombies toward the spot Uzi told you."

    mc "(Okay, that should do the trick.)"

    mc "(Now where should I hide?)"

    "You look around, and see a peculiar {b}sand dune{/b} in the distance, along with a {b}big cactus{/b} and a {b}sewage well{/b}."

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter2_timer_out5'
    show screen countdown

    menu:
    
        mc "(I should go for the...)"

        "Sand dune!":
            
            hide screen countdown
            "You make your way toward the sand dune..."

            jump chapter2_timer_out5_1

        "Cactus!":
            
            hide screen countdown
            "You make your way toward the cactus..."

            jump chapter2_timer_out5_1

        "Well!":
            
            hide screen countdown
            $ combat_points += 2

            "You go down the sewage well and quickly seal the lid."

            "Stretching your leg, you balance yourself between the walls of the well."

            "KA-BOOM! The explosion wipes out the zombies from underneath them!"

            zombie "Arggh!"

            zombie "Grkk!"

            zombie "Blaghh!"

            "The explosion finally reach you, but you're safe because you sealed yourself beneath the well."

            mc "Phew."

            "As the explosion recedes, you go out the well... And see Uzi and his men cheering."

            uzi "Hahaha! Take that, undead scums!"

            ryan "Our boss strikes again!"

            jack "You rule, boss!"

            "They finally spot you!"

            jack "Hey, the kid survived!"

            ryan "Mad respect!"

            uzi "I know you could do it, kid. You should join me instead."

            mc "Not in a million years."

            jump chapter2_resolution

label chapter2_timer_out5:
    
    mc "Umm... Ah screw this!"

    "As you panic, you start running far away, just as..."

    jump chapter2_timer_out5_1

label chapter2_timer_out5_1:

    "KA-BOOM! The explosion wipes out the zombies from underneath them!"

    zombie "Arggh!"

    zombie "Grkk!"

    zombie "Blaghh!"

    "The explosion finally reach you, the impact sends you flying, you feel your skin starts to burn..."

    mc "Aghh!"

    "You fall on the sand, bruises and burns on your skin."

    mc "Aww..."

    "As the explosion recedes, Uzi and his men are cheering."

    uzi "Hahaha! Take that, undead scums!"

    ryan "Our boss strikes again!"

    jack "You rule, boss!"

    "They finally spot you!"

    uzi "You okay, kid?"

    mc "Okay?? I'm almost dead! You didn't tell me the bomb was beneath them!"

    uzi "Well I told ya to hide didn't I? Now who's the idiot!"

    mc "Ughh!"

    "You storm away from them."

    jump chapter2_resolution

label chapter2_lee:
    
    "You make your way to your brother, he is seeing something in using his binoculars."

    mc "Are you going to fight or not?"

    "Startled, he drops his binoculars."

    lee "Gah! You scared me, kid! Thought you're a zombie sneaking up on me."

    mc "What are you looking for anyway? Shouldn't we be killing these things?"

    lee "Still reckless, I see. That, [persistent.name], is how you'll kill yourself."

    mc "I saved your ass with that strategy, you know?"

    lee "Maybe that one time, but now there's more of them. We need a plan."

    "He points at a nearby zombie... This zombie is huge, unlike any other type of zombie."

    lee "You see that zombie? Normal attacks won't work against it, we need to find its {color=#FF0000}{b}weakness{/b}{/color}."

    if persistent.side_quests_1['A Zombie Like Me']:

        $ plan = "Terrence"
        
        "You remember your encounter with Terrence earlier..."

        "...How he said to {b}{i}observe{/i}{/b} for any vulnerable organs."

        mc "We need to attack its organs, Lee. It's the only way."

        lee "Gross, who told you that?"

        mc "A friend told me, you have any objections?"

        lee "As disgusting as it sounds, you have a point. Let's do it!"
    
    else:

        mc "What's your plan?"

        lee "I say we trip it first, and then cuts his neck when he's vulnerable."

        mc "That's too risky, this thing's huge!"

        lee "You have a better idea?"

        menu:
            
            mc "Well..."

            "Let's observe it for weaknesses.":
                
                $ plan = "MC"

                lee "And then? What if it doesn't have one?"

                mc "{i}Everybody{/i} has weaknesses, including zombies."

                lee "Alright, smartypants. Lead on."

            "Actually, let's go with your plan":
                
                $ plan = "Lee"

                lee "I thought so, let's go!"
    
    "Both of you run to face the zombie head on, the moment it sees you..."

    zombie "HRAGHH!"

    if plan == "Terrence" or plan == "MC":

        mc "Scramble!"

        "You and your brother go opposite ways, the zombie strikes the ground beneath you."

        lee "Hey ugly, come get some!"

        if plan == "MC":

            "As your brother distracts the zombie, you take aim with your arrow and..."

            $ time = 5
            $ timer_range = 5
            $ timer_jump = 'chapter2_timer_out6'
            show screen countdown

            menu:

                mc "(I should...)"

                "Wait!":
                    hide screen countdown
                    jump chapter2_timer_out6                    

                "Shoot!":
                    hide screen countdown

                    "You let your arrow fly... and it lands on the zombie's back!"

                    zombie "Grr..."

                    "The zombie doesn't get affected by the arrow, instead it flips its direction at you!"

                    mc "Uh oh..."

                    "The zombie then charges at you with inhuman speed!"

                    lee "[persistent.name]!"

                    "Unable to react quickly... you collide with the zombie with extreme force!"

                    mc "Oof!"

                    "As you tried to get up... You notice something on the zombie..."

                    jump chapter2_lee_2
                
                "Attack!":
                    hide screen countdown

                    "You let your arrow fly... and it lands on the zombie's back!"

                    zombie "Grr..."

                    "The zombie doesn't get affected by the arrow, instead it flips its direction at you!"

                    mc "Uh oh..."

                    "The zombie then charges at you with inhuman speed!"

                    lee "[persistent.name]!"

                    "Unable to react quickly... you collide with the zombie with extreme force!"

                    mc "Oof!"

                    "As you tried to get up... You notice something on the zombie..."

                    jump chapter2_lee_2        
        else:

            "As your brother distracts the zombie, you look for any weaknesses."
            jump chapter2_lee_2
    
    else:
        
        lee "Scramble!"

        "You and your brother jump in different directions as the zombie's punch shakes the earth."

        mc "Alright, lee. What's your plan?"

        lee "Find a way to make it lose balance!"

        zombie "Gragh!!!"

        "The zombie goes after your brother, he swiftly dodges its punches."

        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'chapter2_timer_out8'
        show screen countdown

        menu:

            mc "(I should...)"

            "Throw a rock!":
                
                hide screen countdown

                "You grab a rock nearby and throw it as hard as you can!"

                mc "Hrah!"

                "The rock hits the zombie's back, but not enough to damage it."

                zombie "Hrr..."

                mc "Uh-oh..."

                "It claws at your face, blood spraying from your cheek!"

                mc "Aghh!"

                lee "Oh hell no!"

                "Lee uses the momentary distraction and kicks the zombie's ankle."

                zombie "AUGHH!!!"

                "It writhes in pain as it tumbles down!"

                jump chapter2_lee_3

            "Shoot its leg!":
                
                hide screen countdown
                $ combat_points += 2

                "You grab your arrow and point at its leg!"

                zombie "AUGHHH!"

                "It writhes in pain as it tumbles down!"

                lee "Nice work, [persistent.name]!"

                jump chapter2_lee_3

label chapter2_timer_out6:

    $ combat_points += 1

    mc "Not yet..."

    "You observe the zombie as it swings its arm at your brother..."

    lee "Hrah!"

    "He evades it with ease as you continue to observe..."

    jump chapter2_lee_2

label chapter2_lee_2:
    
    "You spot its {color=#FF0000}{b}skull{/b}{/color} visible from its scorched head, a {color=#FF0000}{b}muscle tendon{/b}{/color} on its arm, and its {color=#FF0000}{b}kidneys{/b}{/color} visible from its back."

    "Grabbing your bow and arrow, you take aim..."

    if persistent.side_quests_1["A Zombie Like Me"]:

        $ combat_points += 2

        "...And hit the kidneys!"

        zombie "AUGHHH!"

        "The zombie writhes in pain... and collapse to ground, dead."

        lee "Wow, just wow."

        mc "Come on, let's finish the rest of them."

        jump chapter2_resolution
    
    else:

        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'chapter2_timer_out7'
        show screen countdown

        menu:

            mc "I should shoot my arrow on its..."

            "Skull!":

                hide screen countdown

                "Your arrow hits the skull, but gives no effect."

                jump chapter2_timer_out7_1

            "Tendons!":

                hide screen countdown

                "Your arrow hits the muscle, but gives no effect."

                jump chapter2_timer_out7_1

            "Kidneys!":

                hide screen countdown
                $ combat_points += 2

                "Your arrow hits the kidney! Blood spraying all over the place."

                zombie "AUGHHHH!"

                "It falls to the ground, dead."

                lee "Okay, wow. Just wow."

                mc "Come on, let's finish the rest of them."

                jump chapter2_resolution

label chapter2_timer_out7:
    
    "You didn't do anything..."

    lee "Do something dammit!"

    "The zombie finally flips its head at you."

    jump chapter2_timer_out7_1

label chapter2_timer_out7_1:
    
    zombie "Grr..."

    "It suddenly charges at you with inhuman speed!"

    mc "Uh oh..."

    "The zombie swings its arm, and claws your face!"

    mc "Aghh!"

    lee "Oh hell no!"

    "Lee charges forward, a blade in hand, he stab the zombie's kidneys!"

    zombie "AUGHHH!"

    "The zombie drops to the ground, dead."

    mc "Wow, just wow."

    lee "That was a terrible plan, [persistent.name]!"

    mc "Sorry."

    lee "Just, head back to the village before you kill yourself!"

    jump chapter2_resolution

label chapter2_timer_out8:
    
    "You didn't do anything..."

    lee "What are you doing, [persistent.name]? Do something!"

    "The zombie swings its head at you! Finally running toward you with inhuman speed!"

    mc "Uh-oh..."

    "It claws at your face, blood spraying from your cheek!"

    mc "Aghh!"

    lee "Oh hell no!"

    "Lee uses the momentary distraction and kicks the zombie's ankle."

    zombie "AUGHH!!!"

    "It writhes in pain as it tumbles down."

    jump chapter2_lee_3

label chapter2_lee_3:
    
    mc "Be careful, it's still moving!"

    lee "Not for long!"

    "Lee takes a blade from his pocket and stabs the zombie into its chest!"

    zombie "GRAGHHHH!!!"

    "It flails wildly before finally stops moving."

    lee "See? I told you it would work."

    if combat_points < 2:

        "Lee examines the scar on your face."

        "You better get that checked out."

        mc "Yeah, sure."
    
    else:
        
        mc "There's still more of them, I'll head back to the village."
    
    "You split paths with Lee and head for the village."

    jump chapter2_resolution

label chapter2_resolution:

    "You return to the main gate of your village... The sun is almost setting..."

    "The amount of zombies is also starting to recede..."

    if combat_points >= 2:

        $ notify("Reckless Warrior", "You hold your own against zombie attacks!")

        mc "Looks like we did it!"
    
    else:

        "You feel pain from your injuries."

        $ notify("Injury taken", "You got injured during the battle, the fights ahead will be harder.", color_title="#FF0000")

        $ persistent.injured = True

        mc "Hff..."

        if len(persistent.healing_items) > 0:
            
            $ persistent.healing_items.pop(0)

            "You quickly take out the medkit from your bag and apply it to your bruises."

            "Soon, the pain starts to recede..."

            $ notify("Injury healed!", "You use the medkit to heal your injuries.")

            $ persistent.injured = False

            mc "That's better."
    
    "As the sun starting to set and the amount of zombies starting to disappear... You gather with the others in the town center."

    "As you make your way to town, you notice people gathering in a big circle, murmuring something."

    "You take a look, and notice 2 villagers being tied together, bite marks visible on their bodies."

    mc "Oh no..."

    villager "Please... I assure you, this is not a bite mark!"

    "The other female villager also pleads to the crowd, tears falling from her eyes."

    villager "Don't do this, what about my family?"

    "As the crowd began to panic, Fabien quickly addresses the crowd."

    fabien "Silence! It appears tragedy has once again struck this village."

    "He takes out the {color=#FF0000}{b}glock{/b}{/color} from his pocket and aim it at the male villager's forehead."

    villager "No please! SOMEBODY HELP ME!"

    mc "STOP!"

    "You rushed forward and grab Fabien's hand."

    fabien "What the--"

    mc "Leave him alone!"

    "The crowd begin to gasp, looking at you with concern."

    fabien "What do you think you're doing?"

    mc "These two have fight for us and you're just going to kill them?!"

    fabien "They have been {color=#FF0000}{b}bitten{/b}{/color} by a zombie! Soon the infection will spread and they'll {i}become{/i} a zombie."

    fabien "You want them to bite you next?"

    menu:

        mc "(...)"

        "There has to be a cure!":
            
            fabien "If there is, then this whole apocalypse wouldn't have happen in the first place!"

            mc "But--"

        "You can't just kill them.":
            pass
    
    fabien "This isn't a fairytale [persistent.name]! Sometimes we need to make some {color=#FF0000}{b}Tough Decisions{/b}{/color} in our lives!"

    fabien "What I'm doing is putting them out of their misery."

    "Several people from the crowd began to murmur..."

    villager "That [persistent.pronouns['child']] is crazy!"

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        villager "Isn't [persistent.pronouns['subject']] the one who let [persistent.pronouns['determiner']] brother die yesterday?"

    if persistent.met_uzi:

        uzi "I thought {i}I{/i} am the crazy one here."
    
    villager "Where are [persistent.pronouns['determiner']] parents?"

    "Soon, you feel a hand pulling you aside."

    mc "What the--"

    "You look around and see your dad pulling you away from the crowd."

    mc "Dad! Let go of me!"

    dad "No!"

    mc "But Fabien's gonna--"

    "BAM! BAM! You hear two gunshots behind you."

    mc "No!"

    "You start running back, but can't because your father holds you back."

    dad "ENOUGH!"

    mom "[persistent.name.title()], you're supposed to be resting, but instead you're off doing something stupid!"

    dad "And as if that wasn't enough, you proceed to humiliate us in front of the whole village!"

    if combat_points < 2:

        dad "I mean look at you! Covered in bruises!"

        if persistent.tough_decisions_1['TD1'] == 'supplies':

            mom "We just lost your brother, and now you're trying to get yourself killed too!"

    dad "From now on, you are grounded!"

    "Tears fill your eyes as your parents drag you to your house..."

    "Until..."

    # Change backdrop here

    "A flash of light appear from the sky, it's so bright that you have to cover your eyes."

    mc "Aghh..."

    dad "Argh!"

    mom "Agh!"

    "Startled, your Father releases your hand."

    "When the light disappears, you look at the sky... And see countless ships, heading for your village."

    mc "Wow..."

    mom "[persistent.name], get behind me!"

    "Several villagers start coming at you, shocked by the scenery above them."

    villager "Now I know I've seen everything."

    villager "Wha... what {i}is{/i} that?"

    "The ships make their landing, releasing huge steam... You cover your eyes as the door opens..."

    "A figure steps out, an alien. Her skin is green, her eyes black and wide, she wears a purple jumpsuit and points a blaster toward the crowd!"

    fabien "It's... it's an alien!"

    "The crowd start to panic, but several other aliens suddenly appear, it's as if they're teleporting, the aliens surround the crowd, each holding a blaster in hand."

    "The female alien speaks, but you don't know what she says."

    placeholder "☊⟟⏁⟟⋉⟒⋏⌇ ⍜⎎ ⏁⊑⟒ ⟒⏃⍀⏁⊑, ⏁⏃☍⟒ ⋔⟒ ⏁⍜ ⊬⍜⎍⍀ ⌰⟒⏃⎅⟒⍀!"

    "None of the villagers dare to speak."

    placeholder "⎅⍜ ⊬⍜⎍ ⋏⍜⏁ ⊑⟒⏃⍀ ⋔⟒? ⟟ ⌇⏃⟟⎅ ⏁⏃☍⟒ ⋔⟒ ⏁⍜ ⊬⍜⎍⍀ ⌰⟒⏃⎅⟒⍀!"

    "You muster the courage to speak."

    mc "What... what do you want with us?!"

    dad "[persistent.name.title()]!"

    "But it's too late, the alien spots you!"

    placeholder "..."

    "As if by magic, you feel yourself levitating. Only to realize you're not feeling it. You're {i}actually{/i} floating in mid air."

    mc "Whoaa..."

    mom "[persistent.name.title()]!"

    "You float forward, and land in front of the alien!"

    placeholder "..."

    "You try to speak... but can't. You feel like there's a barrier in your throat that prevents any word to come out."

    "Meanwhile, the alien reaches out her hand, and touches your forehead."

    "You feel a tingly sensation as the alien muster a sentence to you."

    placeholder "⏁⏃⌰☍ ⏁⍜ ⋔⟒..."

    placeholder "Ta⌰☍ to ⋔e..."

    placeholder "Talk to me..."

    mc "Talk... to you?"

    placeholder "Human of Earth. I am Princess Exaqlyon of Planet Aurellion, your planet is now mine."

    exaqlyon "Surrender and be my slave, or face extinction this very second!"

    mc "Hold on, you can't just take this planet, you just got here!"

    azure "I'm sorry, Am I missing something, you understand this freak now?"

    fabien "[persistent.name.title()], what did she say?"

    "You turn around and face the crowd."

    mc "She... she wants us to be her slave, and if we deny, she'll kill us!"

    "The townsfolk start to gasp."

    villager "What are we gonna do?"

    if persistent.tough_decisions_1['TD1'] == 'brother':

        lee "Like hell..."
    
    if persistent.met_uzi:

        uzi "She ain't gonna be the boss of me, she's a woman!"

        jack "You tell her, boss!"

        ryan "Yeah, we ain't no simp!"

    "Exaqlyon takes your focus back to her, not caring about the crowd behind you."

    exaqlyon "I'm afraid you have no choice in the matter, surrender or be annihilated!"

    fabien "[persistent.name], this is huge, think of your next response very carefully!"

    menu:

        mc "Well then..."

        "Over my dead body!":
            pass

        "Take your unwanted request and shove it!":
            pass

        "For a karen, you got a lot of nerve talking to me like that!":
            pass
    
    "The townsfolk gasp, you see Exaqlyon's eyes widen, completely stunned by your response, before turning into anger!"

    exaqlyon "You... you..."

    exaqlyon "HRAH!"

    mc "Aghh!"

    "You suddenly feel extreme pain in your head, like your brain is being squished by a truck!"

    "You double over, as the aliens surrounding your people raise their weapons, lasers visible at the tip of their blasters."

    villager "Holy..."

    fabien "David! Your [persistent.pronouns['offspring']] is going to get us all killed!"

    "With anger, you hear Exaqlyon's voice in your head."

    exaqlyon "Foolish [persistent.pronouns['adult']], don't you realize just how powerful I am?! I can obliterate you this very instant!"

    exaqlyon "You think this is a joke? Well say goodbye to your--"

    mc "W-wa..."

    mc "WAIT!"

    "You fight against the restraint, your shout caught Exaqlyon by surprise!"

    mc "Wait, please, I'm sorry. Listen to me!"

    "Still in pain, you raise your hand to her, after a while, she orders her men to stand down."

    "The aliens lower their weapons, and your head starting to feel better."

    exaqlyon "Last chance, human! Or do you want me to prolong your suffering?"

    mc "T-take... Take me instead!"

    exaqlyon "What?"

    mc "You said you want to see the leader, right? Well {i}I'm{/i} that person."

    mc "Take me first, let's talk about this, and then I'll show you everything this planet has to offer."

    exaqlyon "This isn't a diplomatic visit, human. You are my prisoner, not a guest of honor."

    mc "Judging by your outfit, you aren't exactly a warrior either, you're a royalty. Now tell me, does every alien royal solve their problems by war and conquest?"

    "She weighs your words, thinking deeply. Meanwhile the villagers start to murmur again."

    if persistent.tough_decisions_1['TD1'] == 'brother':
        
        lee "Are you following this, Azure? 'Cause I'm lost."

        azure "No clue, but I trust [persistent.name] to solve this."

        fabien "Solve how, pray tell? Solve by almost shooting us to ashes?"
    
    elif persistent.met_uzi:

        jack "I think it's working."

        ryan "It looks like that [persistent.pronouns['child']] manages to do it, boss."

        uzi "Yeah, manage to send us to afterlife, you mean."

    else:

        azure "Uhh... Anybody has any idea what they're talking about?"

        fabien "[persistent.name.title()] is screwing this up! We can't trust [persistent.pronouns['determiner']] with this!"

        dad "Watch your mouth, Fabien! That's my [persistent.pronouns['offspring']] you're talking about!"
    
    "Exaqlyon finally offers an answer."

    exaqlyon "Very well, come with me. We'll discuss this in my planet."

    exaqlyon "But I'm warning you! Try anything stupid and you're stardust!"

    mc "{i}Gulp{/i}."

    "She gestures you to her ship, which you reluctantly follow through."

    mc "(At least I manage to buy some time. Hopefully it's enough to persuade her.)"

    "As the door to her ship closes... you see the rest of the aliens teleport back to their ship, finally leaving your people alone."

    "Finally the ship take off... Flying upwards..."

    scene bg black
    with fade

    $ renpy.pause(1.0)

    "Into the unknown..."

    show bg black
    with fade

    $ notify("Chapter 2 Complete", "You've finished Chapter 2. Don't forget to save!")

    $ persistent.progress['complete_ch_2'] = True
    $ persistent.romance_points['Terrence'] += terrence_points
    $ renpy.save_persistent()
    $ renpy.pause(1.0)

    menu:

        "Continue?"

        "Yes":

            "Don't forget to save your game."
            
            jump chapter3

        "No":
            
            call screen episodes
            return