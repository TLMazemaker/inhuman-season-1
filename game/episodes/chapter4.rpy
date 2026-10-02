default visit_second_floor = False
default visit_basement = False
default healing_item = None

label chapter4:
    
    if persistent.gender == 'Female':
        $ terrence_points = persistent.romance_points['Terrence']
    else:
        $ exaqlyon_points = persistent.romance_points['Exaqlyon']
    
    $ combat_points = 0
    $ renpy.save_persistent()

    "Chapter 4: The Failed Experiment"

    scene bg road night
    with fade

    "You stand there, in front of Exaqlyon's ship after your space voyage."
    
    "And you both came face to face with..."

    mc "Terrence..."

    terrence "Didn't you hear what I just said, alien? Get out of my planet!"

    exaqlyon "[persistent.name], you know this freak?"

    terrence "Yeah, I couldn't care less."

    exaqlyon "I wasn't talking to you!"

    terrence "Why you--"

    menu:

        mc "Wait! Hold on..."

        "Back off, Terrence!":

            terrence "Excuse me?!"

            mc "You heard me! Exa was just dropping me off. You can't just barge in here like you know everything to the story!"

            exaqlyon "{i}Thank you.{/i} Finally someone speaks sense."

            terrence "You... You went with--"

        "Watch your mouth, Exa!":

            exaqlyon "What, you're suddenly on {i}his{/i} side?"

            mc "Did you think I forgot what kinda treatment you gave me upon landing in my colony?"
            
            mc "I've known Terrence before I know you and he has every right to guard his territory!"

            terrence "I know you'll understand, [persistent.name]."

            exaqlyon "...Fine, whatever."
    
    terrence "You know what? I don't know what kind of language you speak lady, but you need to get out of here before you cause something!"

    exaqlyon "Ugh... You are seriously hopeless."

    "Exaqlyon steps forward and touches Terrence's forehead, just like what she did to you."

    terrence "Hey! What do you think you're--"

    mc "It's okay, she did this to me earlier, you'll understand what she's saying soon."

    "Terrence's eyes widen, while Exaqlyon says a slightly familiar sentence."

    python:

        for _ in range(3):
        
            renpy.say(exaqlyon, "Talk to me...")
    
    terrence "You... how did you--"

    exaqlyon "My name is Princess Exaqlyon from the Regumen Galaxy. I was just taking [persistent.name] back from my planet."

    exaqlyon "Sorry for the ruckus that I've caused, I mean you no harm."

    "Terrence watches her slightly... then sighs."

    terrence "I'm Terrence, sorry for being a jerk."

    "He offers his hand, and both {i}beings{/i} shake hands."

    mc "See? Why don't we all be friends?"

    terrence "Hmph. I don't know about {i}that{/i}."

    terrence "What {i}were{/i} you doing with her, [persistent.name]?"

    "You quickly tell Terrence the whole story, he nods."

    if persistent.side_quests_1['An Alien Princess']:

        exaqlyon "Well, this has been good and all but I have a kingdom to look after so..."
    
    else:

        exaqlyon "Well, this has been good and all but I believe I have a vacation to attend so..."

    mc "Wait, you're leaving?"

    exaqlyon "I dropped you, right? What else do you want me to do?"

    terrence "You can't seriously force this wannabe warrior queen to stay on our planet."

    "Exaqlyon glares at Terrence, who shrugs nonchalantly."

    mc "I think we should get to know each other first."

    menu:

        mc "Because..."

        "We're a team.":

            terrence "Barf. Says who?"

            exaqlyon "You know, I don't recall teaming up with a human and a... what are you again?"

        "The universe needs us.":

            exaqlyon "From what, exactly?"

            terrence "And for the record, I ain't going inside a spaceship doing a fool's errand."
    
    mc "Guys!"

    mc "I know you two have differences, but I know deep down you're good creatures."
    
    mc "Terrence, you basically spend your whole life defending humans, from your own zombie kin."
    
    mc "Exa, if there's ever a time to impress both of your parents, it's now. And you need help."

    "They both look at each other uneasily."

    exaqlyon "Fine, as long as you stay out of my way."

    terrence "Right back at you."

    terrence "So what should we do now, O fearless leader?"

    mc "You know, there's this abandoned building which I've been {i}dying{/i} to check out."

    mc "And it's surely the best way for bonding."

    exaqlyon "And why's that?"

    mc "Because it's dangerous."

    terrence "Wait, Abandoned Building? You mean--"

    mc "Yup, {b}{color=#FF0000}The Failed Experiment.{/color}{/b}"

    "Terrence furrows his eyebrows, giving you the {i}\"Really?\"{/i} look."

    "Exaqlyon however, gets confused."

    exaqlyon "Umm... how's an abandoned building supposed to be dangerous?"

    terrence "You don't know the history behind it."

    terrence "And are you {i}sure{/i} you want to go there, [persistent.name]?"

    mc "Come on, what's the worst that could happen? Let's go."

    "You start to run, leaving them both."

    exaqlyon "Hey! Wait up!"

    "Exaqlyon presses her watch, and her ship turns invisible before finally running after you."

    terrence "Welp, that [persistent.pronouns['child'][persistent.gender]]'s going to get [persistent.pronouns['reflexive'][persistent.gender]] hurt, isn't [persistent.pronouns['subject'][persistent.gender]]?"

    "Terrence quickly follows you both."
    
    # Change backdrop here.

    "Soon, the three of you arrive in front of the house, the night sky filled the atmosphere, making you shiver."

    mc "This is it."

    exaqlyon "So... what's the deal with this house anyway?"

    terrence "Basically a couple of scientists got killed here, because of their own bloody experiment."

    mc "Not to mention their son {i}{b}and{/b}{/i} a girl went missing."

    exaqlyon "I still don't understand the danger here, how come nobody destroyed this building already?"

    terrence "Nobody would destroy a building in the middle of a zombie apocalypse. This ain't like {i}your{/i} planet, Alien!"

    exaqlyon "You mean {i}your kin{/i} is the problem? Why don't you tell your people to back off then?"

    terrence "I'm not {i}like{/i} them, doofus! Zombies can't--"

    mc "That's enough!"

    "You tell Exaqlyon about Terrence and his conditions."

    exaqlyon "{i}*Sigh*...{/i} You should've told me sooner. So a zombie apocalypse, this Terrence is a docile one, and now {i}this?{/i}"

    exaqlyon "How old was this fairytale of yours?"

    mc "Before I was born, which was {b}{color=#FF0000}20 years ago.{/color}{/b}"

    exaqlyon "Yeah, no creatures on Planet Earth would survive without food for 20 years."

    mc "Which is why I'm eager to find out."

    "You open the door and step in. Inside, the room is very messy, you see a lot of glass shards on the ground, some wooden splinters."
    
    "And some dry blood on the wall."

    terrence "This is just miserable, what are we doing here again?"

    mc "Exploring, I need to know what actually happened here, and how come there's still no trace of the son and the girl."

    "Eventually, you arrive in the living room."
    
    "An elegant staircase spiraling its way up to the second floor, while another one spiraling its way down into the basement."

    menu:

        mc "Let's check the..."

        "Second floor.":

            jump second_floor

        "Basement":

            jump basement

label second_floor:

    "The three of you went upstairs. There, you find yourself in front of a big wooden door."

    exaqlyon "Hmm... weird."

    mc "What is?"

    exaqlyon "This door is made out of a very unique wood, the kind that grows in my planet."

    terrence "Hold up, you're saying this door is {b}{color=#00FF00}alien made?{/color}{/b}"

    if visit_basement:

        exaqlyon "We might find the key to the door on the basement here."
    
    else:

        exaqlyon "We might find something valuable there."

    terrence "Yeah, and then all of a sudden something wrong happens and we're completely cornered."

    "Exaqlyon glances at Terrence."

    exaqlyon "I thought {i}you're{/i} supposed to be strong."

    mc "Can't hurt to be cautious though. One of us should stand guard."

    menu:

        "Side Quest: Into the Enemy's Lair."

        "Go with Terrence" if persistent.gender == 'Female':

            $ persistent.side_quests_1["Partner"] = "Terrence"

            exaqlyon "Good call, {i}Someone{/i} needs to keep watch here."

            "Terrence glares at Exaqlyon, but resigns a sigh as he follows up to you."

            terrence "Come on [persistent.name], before I lose the last of my mind."

            exaqlyon "You already lost it."

            terrence "Very funny."

            "Terrence follows you inside."

            jump premium4

        "Go with Exaqlyon" if persistent.gender == 'Male':

            $ persistent.side_quests_1["Partner"] = "Exaqlyon"

            terrence "Finally, I knew you'd get this pain off of my ass."

            "Exaqlyon opens her mouth to reply, thinks better of it, then follows up to you instead."

            exaqlyon "Come on [persistent.name], otherwise I might blast this creep."

            terrence "What happened to {i}\"I mean you no harm?\"{/i}"

            "Gritting her teeth, she follows you in."

            jump premium4
        
        "Let Terrence and Exaqlyon go.":

            terrence "You're... You're not serious right?"

            exaqlyon "You can't seriously let me wander inside a room with him, I can't guarantee we'll get along."

            mc "You both are the most powerful duo I've ever met, if there's a danger in there you'll be the perfect pair to respond to it."

            exaqlyon "And what about you?"

            mc "I'll be fine, I can smack this door down if anything happens."

            terrence "Alrightthen, {i}Exa{/i}. Stay out of my way, I'll stay out of yours."

            exaqlyon "The feeling's mutual."

            "They both step into the building as you stand guard on the door. Scanning every place for a possible movement, every inch."
            
            $ notify("I'm just a Side Character", "You choose to keep watch.")

            $ persistent.side_quests_1["Into the Enemy's Lair"] = False
            
            "Not long after, the door opens again and the two return, bickering."

            terrence "... {i}You{/i} just blasted the goddamn shelf! You know how the dangerous it is?"

            exaqlyon "So you just tore it open and caused noises? No wonder you're--"

            mc "Guys stop! What do you find in there?"

            "Exaqlyon opens her palm and offers you a key."

            jump chapter4_1

label premium4:

    "You both step inside, the ominous feeling fills you both as you watch the unsurprisingly tidy bedroom."

    menu:

        mc "Well this is..."

        "Eerie.":

            if persistent.side_quests_1["Partner"] == "Terrence":

                terrence "Heh, I'm used to this whole environment, though it might take a while to get used to."
            
            else:

                exaqlyon "Really? This place doesn't quite strike me as 'eerie'."

        "Surprising":

            partner "Surprising?"

            mc "Yeah, everything outside is messed up, this place should also be messy."

        "💗 Romantic":
            
            partner "Romantic?"

            mc "You know... that bed, king sized, just you and me..."
            
            "You raise your eyebrow at [persistent.partner_pronouns['object'][persistent.gender]], you notice [persistent.partner_pronouns['determiner'][persistent.gender]] cheeks flushed."
            
            if persistent.side_quests_1['Partner'] == 'Terrence':

                $ terrence_points += 1
                
                terrence "I... I mean... [persistent.name], we can't--"

                mc "A sleepover I mean, what do you think I was implying?"

                terrence "Oh... well, okay yeah."

                terrence "{i}Aaaannywaaaay...{/i}"
                
            else:

                $ exaqlyon_points += 1

                exaqlyon "You... and me? I mean [persistent.name], I'm not a--"

                mc "A sleepover."

                exaqlyon "Huh?"

                mc "I meant we could have a sleepover on that bed."

                mc "Or do you have any {i}other{/i} ideas in mind?"

                exaqlyon "R-right, I know that."

                exaqlyon "Moving on..."
    
    "[persistent.side_quests_1['Partner'].capitalize()] walks over to the bed, scanning every inch of the mattress, all the way until below the bed."

    partner "Nothing."

    mc "Look at this, though."

    "You beckon [persistent.partner_pronouns['object'][persistent.gender]] to follow you over to the bedside table, you point at the drawer and pull it."

    $ renpy.pause(1.0)

    "...But to no avail."

    mc "Damn, {i}of course{/i} it\'s locked."

    if persistent.side_quests_1['Partner'] == 'Terrence':

        terrence "Let me try."

        "Terrence uses his tentacles and pulls the drawer with all his might."
        
        "After a while, the drawer breaks free from its shelf."
    else:

        exaqlyon "Here, let me."

        "Exaqlyon pulls a blaster from her belt and starts to take aim, she shoots a projectile and the drawer breaks."
        
    "[persistent.partner_pronouns['subject'][persistent.gender].capitalize()] takes something from the shelf and gives it to you."

    partner "Look at this."

    menu:

        "Whoa."
        
        "A key":
            
            pass
    
    mc "Where do you think this key belongs to?"

    if persistent.side_quests_1['Partner'] == "Terrence":

        if not visit_basement:

            terrence "It has to be somewhere around the house, let\'s check it out."
        
        else:

            terrence "This must be the key to the basement, let\'s check it out."
    
    else:

        if not visit_basement:
    
            exaqlyon "My guess is, it\'s somewhere around the house. Let's go."
        
        else:

            exaqlyon "Could this be the key to the basement?"

            mc "It\'s worth a shot."

            exaqlyon "Let\'s go."
    
    "You put the key to your pocket."

    mc "Well, we manage to find something, and not get killed in the process."

    if persistent.side_quests_1['Partner'] == "Terrence":

        terrence "Well, I won't call it \'get killed\' per se. More like, getting into trouble."
    
    else:

        exaqlyon "If something {i}does{/i} happen, I'm sure we can handle it."
    
    mc "All we have to do is to show this to [persistent.partner_pronouns['other'][persistent.gender]]."

    if persistent.side_quests_1['Partner'] == "Terrence":

        terrence "...You're close with this alien, aren't you?"
    
    else:

        exaqlyon "...This Terrence fellow, he's a friend of yours?"
    
    mc "Pretty much, yeah. [persistent.pronouns['subject'][persistent.gender].capitalize()]\'s not a bad creature though."

    if persistent.side_quests_1['Partner'] == "Terrence":

        terrence "I'm sure you already know I'm not good at making friends."

        terrence "I might've misjudged her character, but I don't think she'll forgive me after what I did."

        mc "She's had a lot on her mind, but she's not completely heartless, really the two of you are very similar."

        terrence "You think so?"

        terrence "Well, if you're fine with her... then I guess I can deal with it."
    
    else:

        exaqlyon "I'm sure you know I can be difficult to deal with, especially with my attitude."

        exaqlyon "I caught a glimpse of his mind... and I can sense he's offering me an olive branch."

        mc "Why do I feel like there's a but coming?"

        exaqlyon "...But I don't know why my ego doesn't want to let me."

        exaqlyon "Anyways, I'll try to be nicer to him... seeing you and him are close and all."
    
    menu:

        mc "..."

        "I am not interested in [persistent.pronouns['object'][persistent.gender]].":

            if persistent.side_quests_1['Partner'] == "Terrence":

                terrence "Whoa there, that's not what I'm implying."
            
            else:

                exaqlyon "Umm... I'm not saying 'close' as in romance, you know?"
            
            mc "That's alright, I just don\'t want you to get the wrong idea."

            partner "Heh, believe me. I won't."

            "You walk toward the door."

        "Good, we need teamwork.":

            mc "We might be a ragtag team, but with a little faith, I'm sure we could pull this off."

            "You walk toward the door."
            
        "💗 I'm more interested in YOU.":
            
            if persistent.gender == "Female":

                $ terrence_points += 1
            
            else:

                $ exaqlyon_points += 1
            
            "You take a step closer towards [persistent.partner_pronouns['object'][persistent.gender]]... You put your hand on the back of [persistent.partner_pronouns['determiner'][persistent.gender]] neck and slowly caress it."
            
            partner "[persistent.name.capitalize()] I..."

            mc "Sssshhh... We'll talk later."

            "You give [persistent.partner_pronouns['target'][persistent.gender]] a wink and walk toward the door."
        
    $ notify("Partners In Crime", "You Investigate the Second Floor with [persistent.side_quests_1['Partner']]!")

    $ persistent.side_quests_1["Into the Enemy\'s Lair"] = True

    mc "Come on... let's return."

    if persistent.side_quests_1['Partner'] == "Terrence":

        "Once you both get out of the room, Exaqlyon salutes you."

        exaqlyon "Took you long enough, what do you find in there?"
    
    else:
        
        "Once you both get out of the room, Terrence salutes you."

        terrence "Welcome back, what do you find in there?"
    
    "You show [persistent.pronouns['object'][persistent.gender]] the key."

    jump chapter4_1

label chapter4_1:
    
    menu:

        "A key."

        "Where does this go?":

            pass
    
    if visit_basement:

        mc "I bet it will fit the door in the basement."

        terrence "Well, let's go then."

        "You make your way back to the basement... Once you're there, you're faced with the same door."

        jump chapter4_2
    
    else:

        mc "Any idea where this key goes?"

        exaqlyon "I bet it fits somewhere in the other parts of this house, Come on."

        $ visit_second_floor = True

        "The three of you make your way down... Once you're back, you notice there's still the basement left to explore."

        mc "Let's check the basement this time."

        jump basement

label basement:

    "You make your way down, there you find a big sturdy metal blocking your path."

    terrence "What on earth?"

    exaqlyon "Hmm... interesting."

    mc "What?"

    exaqlyon "This wall is very smooth, no keyhole, no handle."
    
    exaqlyon "It's almost like... it's machine-based."

    terrence "You mean this contraption?"

    "Terrence points toward a lever being held in place inside a transparent barrier."
    
    "The barrier itself is sealed with a lock."

    if visit_second_floor:

        $ visit_basement = True

        jump chapter4_2

    else:

        mc "Hmm... I think we're missing something here."

        mc "Let's search some other place first, if we find a key we'll return here."

        terrence "The stairs go up to the second floor, right? What about there?"

        exaqlyon "For once, I agree."

        "You make your way back up, into the second floor."

        $ visit_basement = True

        jump second_floor

label chapter4_2:

    mc "Let's see if this key fits."

    "You put the key into the hole and began turning it, you heard a soft click, and the lock opened."

    mc "It works!"

    "Once you pull the lever, the metal door lifts up."
    
    "Inside you spot a laboratory, completely tarnished."

    exaqlyon "Nice, let's see what this place is all about."

    terrence "I have a bad feeling about this, maybe we shouldn't--"

    exaqlyon "Don't tell me you're backing up now, zombie."

    terrence "You don't know what you're talking about, alien!"

    exaqlyon "You're telling me you're afraid of some myth from 20 years ago? Coward."

    terrence "You're goading me into following you, right?"

    exaqlyon "Is it working?"

    terrence "Yes, let's go already."

    "The three of you step inside the laboratory, you can't shake the feeling of being watched."

    mc "..."

    "You glance at Terrence and Exaqlyon, somehow you know they feel it too."

    "{i}Click!{/i}"

    terrence "What was that?"

    exaqlyon "Umm... probably just the wind, right?"

    mc "Wind? In the basement?"

    "The feeling comes again, stronger this time..."
    
    "You can feel movements from your {b}{color=#FF0000}left{/color}{/b} side!"

    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'chapter4_timer_out1'
    show screen countdown

    menu:

        mc "..."

        "(Turn left)":
            hide screen countdown

            "You glance at your left side... and spot a pair of eyes!"

            mc "What was that?"

            "The others look too, but it's too quick, the eyes quickly disappear."

        "(Keep going forward)":
            hide screen countdown
            jump chapter4_timer_out1
    
    jump chapter4_3

label chapter4_timer_out1:

    "Ignoring your gut, you keep moving forward, just as..."

    exaqlyon "Who's there?"

    "You see Exaqlyon looking at her left side, the same side you felt."

    jump chapter4_3

label chapter4_3:

    exaqlyon "I could've sworn I saw a {color=#FF0000}{b}pair of eyes{/b}{/color} from over there!"

    terrence "Oh {i}now{/i} you're scared?"

    "{i}Crash!{/i} A loud noise can be heard from behind you!"
    
    "The three of you look back and see a disintegrated beaker glass at the floor... followed by a soft laughter."

    placeholder "Heh heh heh..."

    mc "Who's there?"

    terrence "Show yourself coward!"

    placeholder "Coward? Heh heh heh... Very well..."

    "{i}Ka-CHUNK!{/i} In an instant, the door to the entrance is closed shut, trapping you inside!"

    exaqlyon "What on earth?"

    "You heard a soft hiss... and a couple footsteps on the wall..."
    
    "Finally, you heard a loud sound, from the entrance of the lab! You look in that direction and see..."

    placeholder "Grr..."

    terrence "Oh... My..."

    exaqlyon "World..."

    "The boy from your mother's tale... looking younger than you despite being 20 years older than you, his skin is filled with scales, he has the eyes of a snake, and only his trouser remains on him."
    
    "Also, a snake is clinging around his neck..."

    mc "You! You're the boy from the myth!"

    placeholder "Heh heh heh, funny how I manage to become a myth despite me being real."

    "The figure steps closer, making your group walk further into the lab."

    placeholder "The name's Serpent, being a mutant is much more rewarding than being a human."
    
    serpent "And you lot shouldn't be wandering here if you already heard of this house!"

    exaqlyon "S-s-stay back!"

    serpent "Now who's the coward?"

    serpent "You wanna play? Let's play, I want to see who can get out of this place ALIVE!"
    
    serpent "Jason? Boost me!"

    jason "HSSSS!!!"

    "The snake that's surrounding his neck bites down! Injecting him with venom."
    
    "He kneels down, you see his eyes filled with fury!"

    serpent "Hrr... HRRAAAGHHH!!!"

    "And just like that, he lunges at you!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter4_timer_out2'
    show screen countdown

    menu:

        mc "..."

        "Stare!":
            hide screen countdown
            jump chapter4_timer_out2
        
        "Draw your weapon!":
            hide screen countdown

            "You reach for your weapon..."

            "But it's too slow! He tackles you to the floor!"

            mc "Ahh!"

            serpent "Hahahaha! Little fools!"

            jump chapter4_4
        
        "Duck!":
            hide screen countdown

            $ combat_points += 1

            "Thinking quickly! You drop to your feet, Serpent lunges above you and crashes to the floor."

            serpent "Grr..."

            mc "Ha! Not so smart now, are you boy?"

            "He stands, staring you dead in the eyes!"

            jump chapter4_4

label chapter4_timer_out2:

    "Terrence and Exaqlyon both get out of the way, but you stay still... allowing him to push you to the floor!"

    mc "Ahh!"

    serpent "Hahahaha! Little fools!"

    jump chapter4_4

label chapter4_4:

    exaqlyon "Get away from [persistent.pronouns['object'][persistent.gender]]!"

    "Exaqlyon takes out her blaster, shooting some projectiles..."
    
    "But Serpent's too fast, he slithers on the floor toward you in an inhuman speed."

    terrence "Exa, move!"

    "Terrence tackles Exaqlyon to the side while Serpent rises up and focuses his gaze on you once more!"

    serpent "Come here little mouse! The serpent just wants to play!"

    "Suddenly, He throws his snake in your direction, jaw wide open!"

    jason "HISSSSS!!!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter4_timer_out3'
    show screen countdown

    menu:

        mc "..."

        "Duck!":
            hide screen countdown

            "You duck to the ground… right at where it's landing! Landing at your face."

            mc "Gahh!"

            jason "HISSS!"

            "But before it could bite you, you smack your own face at the table!"

            mc "Oof..."

            jump chapter4_5

        "Smack it away!":
            hide screen countdown
            
            "You smack the snake with your hand... forgetting it could cling onto it!"

            jason "HISSS!!!"

            "It presses around your arm, making you can't feel anything!"

            mc "Argh!"

            "Before you run out of energy, you find some salt at the table, and immediately spread it to the snake."

            jason "SSSHHHHH!!!"

            jump chapter4_5
        
        "Block with a beaker!":
            hide screen countdown

            $ combat_points += 1

            "Thinking quickly, you take a beaker glass and shove it in the snake's mouth!"

            mc "Eat this!"

            jason "HRRKKKK!!!"

            jump chapter4_5

label chapter4_timer_out3:

    "Not knowing what to do... the snake lands at your face!"

    mc "Gahh!"

    jason "HISSS!!!"

    "But before it could bite you, you smack your own face at the table!"

    mc "Oof..."

    jump chapter4_5

label chapter4_5:

    "The snake slithers away from you, just as..."

    serpent "Jason!"

    "Serpent runs to grab Jason, but Terrence's tentacles lock him in position while Exa shoots the snake and traps it in a force field!"

    terrence "Where do you think you're going huh?"

    exaqlyon "Let's see how you fare without your pet, you ugly beast!"

    serpent "No... HRRAGGGHHH!!!"

    "With his strength, he grabs one of Terrence's tentacles and throws him at Exaqlyon!"

    terrence "Wha-- AHHH!"

    exaqlyon "Oof!"

    "They tumble to the ground as the forcefield that's holding Jason disappears."

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter4_timer_out4'
    show screen countdown

    menu:

        mc "..."

        "Throw something at Serpent!":

            hide screen countdown

            "You grab a microscope and throw it at Serpent\'s head."

            "{i}CRASH!{/i}"

            serpent "Oof!"

            "He rubs his temples... but remains undamaged."

            serpent "Big mistake!"

            "In a flash, he lunges at you and scratches your face!"

            mc "Argh!"

            "Serpent walks past you and reclaims Jason."

            jump chapter4_6

        "Tackle him!":

            hide screen countdown

            "You lunge for him, forgetting he is a mutant."
            
            "He shifts his weight against you and pins you to the ground."

            mc "Ack!"

            serpent "Fools..."

            mc "You're nothing without your Jason!"

            serpent "Oh yeah?"

            "He curls his fist and punch your jaw, {i}hard!{/i}"

            mc "Augh!"

            "Jason slithers to his leg, making its way to Serpent\'s neck once more."

            jump chapter4_6

label chapter4_timer_out4:

    $ combat_points += 1

    "You keep your distance as Serpent takes Jason and puts it back around his neck."

    mc "(There's nothing I can do for now, better preserve my energy.)"

    jump chapter4_6

label chapter4_6:

    serpent "Hngg..."

    "Serpent clutches his head, toppling backwards."

    "Nearby, Exaqlyon stretches her arm, attacking Serpent's mind."

    exaqlyon "Hngg... Stay... silent!"

    serpent "Grr..."

    "As if on cue, Jason leapt toward Exaqlyon, its jaw open, ready to bite!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter4_timer_out5'
    show screen countdown

    menu:

        mc "..."

        "Fire an arrow!":
            hide screen countdown

            "You fire an arrow, but Jason is too quick, it misses the arrow by a pinch!"

            mc "No!"

            jump chapter4_7

        "Warn Exaqlyon!":

            hide screen countdown

            mc "Exa! Watch out!"

            exaqlyon "Huh?"

            jump chapter4_7

label chapter4_timer_out5:

    "You stand there, words can't seem to escape your mouth."

    terrence "Alien! Snake!"

    exaqlyon "Huh?"

label chapter4_7:

    "Sensing danger is nearby, Exaqlyon stops her attack."

    exaqlyon "Whoa!"

    "Jason lands on the floor, hiding behind a nearby cabinet."

    if combat_points < 2:

        "You look back at Serpent, who looks back at you, smirking."

        serpent "Heh, that's all you got? Pathetic!"

        mc "Hff... hff..."

        $ notify("Injury Taken", "You did poorly against Serpent.")

        $ persistent.injured = True

        if persistent.healing_items:

            $ healing_item = persistent.healing_items.pop(0)

            if healing_item == "Medkit":

                "You quickly take the medkit from the villa and begin wrapping a part of your face with the bandages."
            
            else:

                "You take out the Obsidian Theta Lava from your journey with Exaqlyon and begin to pour the cold lava on your face."
        
            "Soon, you can feel the pain dissipates."

            mc "Hff..."

            $ notify("Injury Healed", "You used your healing item.")

            $ persistent.injured = False
        
        serpent "You thought you're so smart exploring off-limit areas..."
    
    else:

        "You look back at Serpent, who looks back at you, shocked."

        serpent "I must say, normally people wouldn't last this long."

        $ notify("Inhuman Warrior", "You hold your own against Serpent.")

        mc "Tired yet? I can do this all damn night!"

        serpent "You and your friends might still be standing..."
    
    "Behind him, Jason reappears and begins slithering up to Serpent\'s neck."

    serpent "...but this is where your journey ends!"

    terrence "Urgg... Not... not yet..."

    exaqlyon "We won\'t... lose to you..."

    "Serpent walks towards you, you notice the door you walked in from, closed. A lever stands beside it."

    mc "(Fighting him is impossible, we must escape!)"

    "You glance at Terrence, once he looks at you, you nod toward the door, hoping to give him the signal."
    
    "He nods."

    terrence "..."

    "You do the same with Exaqlyon. She also nods."

    exaqlyon "..."

    serpent "Let's see how much of you squirm once I infuse you with this venom..."

    exaqlyon "Infuse yourself with this!"

    "In a flash, Exaqlyon bolts out her blaster, shooting laser towards Serpent\'s eyes!"

    serpent "{i}HISSS!!!{/i}"

    mc "Now Terrence!"

    terrence "Hrah!"

    "Terrence darts forward, locking Jason with his tentacles and keeping Serpent in his grip!"

    serpent "{i}HISSS!!!{/i}"

    terrence "Now, both of you!"

    "You and Exaqlyon darts forward, you pull the lever down, and immediately the door opens."
    
    mc "That's it, let's..."

    exaqlyon "[persistent.name], wait!"

    "As you release the lever from your grip, walking outside, Exaqlyon suddenly stops you, just as..."

    "{i}CHUNK!{/i} The door immediately closes after you let go of the lever."

    mc "What the..."

    exaqlyon "The lever won't stay in place, I knew I sense danger."

    "Meanwhile, the two men wrestle, Serpent thrashes violently against Terrence\'s grip."

    exaqlyon "Let me try holding the door, you pull the lever on the other side!"

    "Exaqlyon stands beneath the door as you pull the lever again, you let go of the lever slowly as she holds the door beneath her."

    exaqlyon "Hngh! Hurry!"

    "You get out of the room, but notice the other lever has been snapped!"

    mc "Oh no! Exa, the lever here is broken!"

    exaqlyon "Son of a {i}gekron{/i}!"

    "Back in the lab, Terrence puts Serpent in a chokehold position, while his tentacles keeping a steady grip on Jason."

    mc "Terrence! Exa manages to hold the lever, but it won\'t stay open. You gotta {b}{color=#ff0000}let him go!{/color}{/b}"

    terrence "Are you insane? If I let go, he\'ll go after you both!"

    exaqlyon "Hngh! You gotta take the risk, otherwise you can\'t escape!"

    terrence "Just... take [persistent.name] and get out of here! I can deal with these two!"

    exaqlyon "I can't just leave you here you idiot!"

    "Exaqlyon steadies her breath, steadying her feet as the door above her getting heavier."

    exaqlyon "Because... we\'re a team, remember?"

    terrence "Exa..."

    serpent "HISSSS!"

    "Seeing an opening, Serpent bares his fangs, landing on Terrence\'s left wrist!"

    terrence "AAAAGGGHHHH!!!"

    mc "TERRENCE!"

    "You watch in horror as Terrence screams in pain, not knowing what to do."

    exaqlyon "[persistent.name.title()] look! Over there!"

    "You follow Exaqlyon\'s gaze, and see a bottle labeled \"Antidote\" across the room at the far corner."

    mc "Is that..."

    exaqlyon "I believe that potion could neutralize the venom infecting Terrence, but it\'s so far away you have to act quick!"

    "Your mind\'s racing, you look at the antidote, to Terrence, and to the door..."
    
    "You know... at that one moment..."
    
    $ renpy.pause(1.0)

    "You can\'t save both."

    menu:

        mc "(What should I do?)"

        "☠️ Pull Terrence away! ☠️":
            
            $ decision = "pull"
            jump chapter4_pull

        "☠️ Grab the antidote! ☠️":
            
            $ decision = "antidote"
            jump chapter4_antidote

    # mc "I need you to do something for me, Exa."

    # "You lift the door from Exaqlyon's hands."

    # exaqlyon "What should we do?"

    # "As she releases her grip, you immediately shoulder her out from the lab!"

    # exaqlyon "Oof!"

    # "You immediately release the door as it closes, separating Exaqlyon with you."

    # if len(persistent.name) > 2:

    #     exaqlyon "[persistent.name[:2].title()]--"
    
    # else:
    #     exaqlyon "[persistent.name.title()]--"

    # mc "Sorry, but I can\'t let you get hurt."

    # if decision == 'pull':
    #     jump chapter4_pull

    # else:
    #     jump chapter4_antidote

label chapter4_pull:
    
    "You grab a glass beaker and smack it against the side of Serpent\'s head!"

    serpent "Hrkk..."

    "Startled, he releases his grip on Terrence."

    mc "Come on, let's get out of here."

    "You usher Terrence uot and take the lever from Exaqlyon."

    exaqlyon "Wait, what about his wrist?"

    terrence "Hngg... It\'s too late, the venom has spreaded to my arm."

    mc "No! I won\'t let it!"

    "You release the lever and the door closes once more."

    if len(persistent.name) > 2:

        exaqlyon "[persistent.name[:2].title()]--"
    
    else:

        exaqlyon "[persistent.name.title()]--"
    
    "You hear banging on the other side as Exaqlyon tries to open the metal door."

    mc "Sorry, but I can\'t put you in danger."

    "You rush in and take the antidote."

    menu:

        "The Antidote."

        "Take it":
            pass
    
    "As you make your way to the exit..."

    serpent "HRAGH!"

    "Serpent lunges at you from behind, causing you to fall..."

    "{i}{b}CRASH!{/b}{/i} The antidote hits the floor, liquid spilled all over the floor."

    mc "NOOOOO!!!"

    $ notify("Tough Decision!", "Terrence gets out... but you lose the antidote.", color_title="#FF0000")

    $ persistent.tough_decisions_1['TD2'] = "pull"

    "Serpent makes his way on top of you..."

    mc "Get... OFF OF ME!"

    "You plant your foot and kick him in the face... hard!"

    serpent "Gahh!"

    "You deliver another kick, but this time he\'s ready."

    "He grabs it and puts his other arm at your throat... lifting you up!"

    jump chapter4_8

label chapter4_antidote:
    
    "You rush past the two and go for the antidote!"

    serpent "NO!"

    "Serpent lunges forward... releasing his grip on Terrence, who doubles over."

    exaqlyon "Get away from [persistent.pronouns['object'][persistent.gender]]!"

    "Using one hand, Exaqlyon puts out her blaster and shoots at Serpent\'s back."

    serpent "Hrk..."

    jason "HISSS!!!"

    "Jason lashes out towards Exaqlyon, but Terrence uses his tentacles to pin it down!"

    "Meanwhile, you finally arrive at the antidote."

    menu:

        "The Antidote."

        "Take it.":
            pass
    
    "You look back and see Serpent rushing after Terrence, aiming to free Jason!"

    mc "Terrence! Throw the snake at me!"

    terrence "What?!"

    mc "He won\'t hurt you if Jason is in my possession."

    "Terrence does what you asked him and throws Jason at you."

    "At the same time, you throw the antidote at Exaqlyon."

    mc "Exa, catch!"

    "Exaqlyon catches the antidote as Terrence heads for the door..."

    "But since you throw the antidote, you have left youself slightly vulnerable, so Serpent lunges for you with Inhuman Speed."

    serpent "HISSS!!!"

    mc "Urk..."

    exaqlyon "[persistent.name.title()]!"

    "Jason breaks free from your grip as Serpent throws it at both of them!"

    serpent "Kill them, Jason!"

    jason "HISSS!!!"

    "Exaqlyon, shocked at the sight, releases the lever and exits.."
    
    "The door falls down, trapping you and Serpent inside."

    serpent "Times up, human!"

    "He bares his fangs... and bites your right leg!"

    mc "AGHHHHH!!!"

    "You immediately pull an arrow from your back..."

    "And thrust it into his head!"

    serpent "AUGHHH!"

    "Serpent lets out a painful cry as you back away, wincing in agony."

    "But he recovers quickly and he grabs you by the throat and lifts you up."

    jump chapter4_8

label chapter4_8:

    mc "Hrkk..."

    "Serpent\'s grip on you tightens, you can feel your consciousness fading..."

    mc "{i}Hff... Hff...{/i}"

    serpent "Foolish human, coming all the way here to play detectives..."

    serpent "Your kin disgusts me, you were the ones who wreck the place..."

    serpent "You turned me into {b}{color=#ff0000}a MONSTER!{/color}{/b}"

    mc "(Shit! If I don't do something, he\'s gonna kill me.)"

    mc "(I\'m sure the old him is {i}still{/i} in there, his human nature!)"

label menu_loop:

    menu:

        mc "Hrkk... Stop! This isn\'t who you are..."

        "Stanzer":
            
            serpent "That name means nothing to me!"

            serpent "Goodbye human!"

            "His grip completely empowers you, your image starts to blur as your brain starts losing oxygen..."

            $ renpy.pause(1)

            "You have died."

            "Restarting..."

            jump menu_loop

        "Slazer":
            
            serpent "That name means nothing to me!"

            serpent "Goodbye human!"

            "His grip completely empowers you, your image starts to blur as your brain starts losing oxygen..."

            $ renpy.pause(1)

            "You have died."

            "Restarting..."

            jump menu_loop
            
        "Spencer":
            
            "Serpent\'s eyes go wide."

            serpent "That... that name... how did you..."

            "Startled, he lets go of his grip, his eyes switching from snake eyes to human eyes."

            mc "Urghh..."

            "You back away from him, as he continues to have a panic attack."

            "Serpent looks down, looking at his own hands."

            serpent "What... what have I done?"

label chapter4_resolution:

    if decision == "antidote":

        "Meanwhile you notice the veins in your right leg starting to turn blue."

        mc "Ngghh... no... not like this."

        "You see an {b}{color=#ff0000}axe{/color}{/b} near one of the tables..."

        "Grabbing the axe, you prepare youself to do the unthinkable."

        mc "Ngghhh... Come on, you can do this [persistent.name]."

        menu:

            "You lift the axe high, and..."

            "Chop your leg!":

                mc "AGHHHH!!!"

                "It feels painful as ever, but your foot is not cut all the way yet."

                mc "Hrghh... Come on..."

                "{i}BRAK!{/i}"

                mc "NGHHHHH!!!"

                "Unable to handle the pain, you pass out."

                $ notify("Tough Decision!", "You grab the antidote, with the price of your leg.", color_title="#FF0000")

                $ persistent.tough_decisions_1['TD2'] = "antidote"

    else:

        mc "Kf... kff..."

        "You run low on oxygen... and pass out."
        
    scene bg black
    with fade

    $ renpy.pause(1)

    "..."

    "{i}[persistent.name.title()]{/i}..."

    $ renpy.pause(1)

    "[persistent.name.title()]!"

    scene bg spaceship
    with fade

    "You open your eyes, and see Exaqlyon with Terrence. Each standing beside you."

    terrence "[persistent.pronouns['subject'][persistent.gender]]\'s awake!"

    exaqlyon "Thank the stars!"

    "You realize you are aboard Exaqlyon's spaceship."

    "You are lying on a bed, the view of sunrise is visible from the window."

    mc "Wha... what happened?"

    "You tried to get up, but wince due to the pain in your body."

    mc "Hff..."

    exaqlyon "Whoa there."

    terrence "Slowly."

    if persistent.tough_decisions_1["TD2"] == "pull":

        "As you sit up straight, you notice Terrence hides his left arm."

        mc "Terrence, what happened to your arm?"

        terrence "Oh, umm..."

        "He shows you his arm, his skin has been completely {b}{color=#ff0000}peeled off.{/color}{/b} And only his bones remain intact."

        terrence "The poison spreaded quickly, but thankfully, most of the tendons had already grown rotten."

        exaqlyon "I had to cut it out from your arm, idiot! Lest it would\'ve spreaded to the other parts."

        mc "Oh no..."

        "You sit in silence, anxiety started filling your chest again, the same feeling from the woods."

        terrence "Okay, I want none of that."

        "Terrence uses his right arm and gently taps your face. You looked at his face."

        terrence "You don\'t have to feel guilty alright? There\'s nothing left from this rotten body, all that matters is that you\'re safe."
    
    else:

        "As you sit up straight, you started feeling a weird sensation..."

        "Particularly in your right {b}{color=#0000ff}leg.{/color}{/b}"

        mc "My leg... what happened to my leg?!"

        "You opened the blanket covering your body, and found that a {b}{color=#ff0000}metal leg{/color}{/b} is placed at where your old leg used to be."

        terrence "[persistent.name.title()]..."

        mc "What... what happened?"

        exaqlyon "When we found you, you were bleeding... Your leg was already in bad shape."

        terrence "We had no choice but to {b}{color=#ff0000}amputate{/color}{/b} it."

        "Anxiety starts flowing through your body, your leg is gone. You are no longer the same [persistent.name.title()] as you used to be."

        exaqlyon "I... I think you made the right decision, [persistent.name]. Otherwise it could\'ve been worse."

        terrence "Not exactly the kind of comforting words you should say to someone, but I digress."
    
    "You took a deep breath, calming your nerves after everything that happened."

    "Once you feel your pulse has slowed down, you finally muster a word."

    mc "How... how did I even manage to end up here?"

    "Terrence and Exaqlyon both look at each other, their expressions uneasy."

    exaqlyon "You uh... You were brought out by Serpent."

    mc "What?"

    terrence "I don\'t know what black magic did you perform to the man."

    terrence "But he opened the door with a blank expression."

    exaqlyon "He said he wasn\'t fully himself, and that he understand if we want to kill him."

    menu:

        mc "..."

        "So what did you do to him?":
            
            exaqlyon "This man here wanted him dead, but I told him not to do it."

            terrence "Because killing him is the right thing!"

            exaqlyon "You don\'t get to judge that!"

            if persistent.tough_decisions_1["TD2"] == "pull":

                terrence "Look at me, Exa! Look at what happened to me!"
            
            else:

                terrence "Oh so after everything he {i}still{/i} deserves a second chance?!"

        "Wasn\'t fully himself?":
            
            "You recall the moment you call Serpent\'s name, his real name."

            mc "I think I know what happened."

            mc "So what happened."

            terrence "{i}Princess{/i} Exaqlyon here wanted to be the good Samaritan, and decided to not killed him."

            exaqlyon "Ironic, coming from you. We shouldn\'t kill him before he answers to all his crimes, genius!"
        
    mc "Guys! That\'s enough!"

    mc "So where is Serpent right now?"

    exaqlyon "He is locked inside a prison in this ship."

    "You got down from the bed."

    terrence "Where are you going?"

    mc "I want to meet him, Bring me there, Exa."

    exaqlyon "Okay."

    if persistent.tough_decisions_1["TD1"] == "antidote":

        "The three of you walked toward Serpent\'s prison. You walk slowly, limping because you haven\'t adjusted yourself with the new leg yet."
    else:
        
        "The three of you walked toward Serpent\'s prison."

    exaqlyon "There he is."

    "Serpent sits inside a room, a force fields separates him and you as he sits there silently."

    "His feet wrapped tightly on his chest as he sits with his back against the wall."

    "Meanwhile, Jason is wrapped tightly around his neck, his eyes closed, but still open sometimes, sensing if dangers are nearby."

    "They both see you as you come near, but doesn't say anything and instead return to their isolation."

    terrence "What a sickening beast, to think he can just act like that!"

    exaqlyon "Is that all you can think of? Can\'t you see he was really someone else when he attacked us."

    menu:

        mc "Well..."

        "Terrence\'s right":
            
            mc "Possessed or not, that doesn\'t mean he can just walk away!"

            terrence "{i}Thank you!{/i} I don\'t care if he has trauma or whatever!"

            terrence "We all have traumas! Doesn\'t mean we get to do whatever we want because we have {i}{b}mental issues.{/b}{/i}"

            "Exaqlyon shakes her head in disappointment."

            exaqlyon "What if {i}you{/i} were in his shoes right now?"

        "Exa\'s right":
            
            mc "Back there, he genuinely looked troubled, I can\'t even imagine what he would feel right now."

            exaqlyon "See, Terrence? Sometimes you have to looked deeper into people."

            if persistent.tough_decisions_1['TD1'] == "pull":

                terrence "Tell {i}that{/i} to my arm."
            
            else:

                terrence "Yeah, keep being kind to other people, and maybe even give them your life for free too."
    
    mc "In any case, we should head back."

    terrence "And what do we do with him?"

    "You look at Serpent one last time."

    mc "Let\'s just keep him here, worst case scenario he dies because of hunger."

    mc "And besides, if we were to show him to my villagers, they\'ll definitely panic."

    "Just then, you heard commotions from outside."

    exaqlyon "That\'s gotta be them. They must be looking for you."

    mc "Let\'s go."

    "The three of you make your way to the entrance of the spaceship."

    mc "You know, there\'s one thing that I\'m really grateful from this."

    terrence "What could you {i}possibly{/i} appreciate from this disaster?"

    mc "This catastrophe had really brought the two of you closer together."

    exaqlyon "Heh?"

    terrence "Ha?"

    mc "Before, you two looked like you\'re genuinely ready to tear each other apart."

    mc "But now look at you, working together despite your differences."

    "They both looked at each other, and look away."

    terrence "Yeah, hard pass."

    exaqlyon "That was a one time thing, I doubt it\'ll happen again."

    mc "Well, you\'ll never know."

    exaqlyon "Anyways, how are you going to handle the crowd?"

    terrence "Fyi, I am {i}{b}not{/b}{/i} showing my face to those people."

    mc "But if you didn\'t get out, where will you go?"

    terrence "That\'s okay, she\'ll probably drop me off somewhere."

    exaqlyon "Does the surface of the sun works?"

    mc "Anyways, here goes nothing."

    scene bg village day
    with fade

    "As the spaceship door opens, you adjust you see an enormous crowd gathering in front of you."

    "You look closely, and feel relief to see your parents..."

    if persistent.tough_decisions_1["TD1"] == "brother":

        "...with your brother and the other villagers."

        lee "Well I\'ll be damned. [persistent.pronouns['subject'][persistent.gender].title()]\'s alive!"
    
    else:

        "...with Fabien and the rest of the other villagers."

    fabien "There [persistent.pronouns['subject'][persistent.gender]] is!"

    azure "[persistent.name]! You\'re alive!"

    if persistent.tough_decisions_1["TD2"] == "antidote":

        "You hear gasps of the other villagers as you notice they are staring at your fake leg."

        villager "Did you see {i}that?{/i}"

        villager "[persistent.pronouns['determiner'][persistent.gender].title()] leg..."

        villager "Did the alien did this?"

    menu:

        mc "Everyone..."

        "The alien will bother us no more.":
            pass

        "I have made it home safe and sound.":
            pass

        "This is the price for our village." if persistent.tough_decisions_1["TD2"] == "antidote":
            pass
    
    mc "I assure you, I have made peace with the alien."

    "As you made your way down the ship\'s platform, you hear Exaqlyon gasps."

    mc "What\'s the matter?"

    exaqlyon "My kingdom..."

    exaqlyon "It\'s {b}{color=#ff0000}under attack!{/color}{/b}"

    "You feel your stomach sink."

    exaqlyon "I\'m sorry, [persistent.name]. I need to go home immediately."

    mc "No worries, good luck with that."

    "You look past Exaqlyon to catch of glimpse of Terrence. You see him looking back at you."

    terrence "..."

    mc "..."

    "You both exchange a nod, before you step off the platform."

    if persistent.tough_decisions_1['TD1'] == "supplies":

        "As the platform retracts, you see Azure running toward you."
    
    else:
    
        "As the platform retracts, you see Azure and Lee running toward you."

    azure "Are you alright?"

    mc "I\'m okay."

    if persistent.tough_decisions_1['TD1'] == "brother" and persistent.tough_decisions_1['TD2'] == "antidote":

        lee "Are you going to explain what happened to your leg?"
    
    elif persistent.tough_decisions_1['TD1'] == "brother" and persistent.tough_decisions_1["TD2"] == "pull":

        lee "So what happened out there?"
    
    elif persistent.tough_decisions_1['TD1'] == "supplies" and persistent.tough_decisions_1['TD2'] == "antidote":

        azure "We were so worried."

        azure "I mean just look at your leg!"
    
    else:

        azure "So what did you see out there?"

        azure "Can you really speak alien right now?"
    
    mc "I\'m okay. Despite everything, I\'m still standing."

    "You think back on everything that had happened."

    "Meeting Exaqlyon\'s parents... Until almost getting executed."

    "Exploring the \"Failed Experiment\"..."

    "Fighting Serpent, who was the missing kid for over 20 years..."

    if persistent.tough_decisions_1["TD2"] == "antidote":

        "Chopping off your own leg..."
    
    mc "It was fun too."

    azure "You\'re joking."

    if persistent.tough_decisions_1['TD1'] == "brother":

        lee "Who are you and what did you do to my [persistent.pronouns['sibling'][persistent.gender]]?!"
    
    "You look back at Exaqlyon\'s spaceship. Steam starting to come out of it, indicating it\'s almost taking off."

    azure "...I know that look."

    mc "Huh?"

    azure "You want more, aren\'t you?"

    mc "I..."

    "Without waiting for a reply, Azure pointed toward the ship."

    azure "If you can make it, you can still cling onto the platform as it ascends."

    mc "But... are you sure?"

    if persistent.tough_decisions_1["TD1"] == "brother":

        "You look at your brother, and he sighed."

        lee "You\'re always the wild one, [persistent.name]..."

        lee "I say go for it."
    
    else:

        "Azure nods."

        azure "Don\'t worry, I\'ll explain things to your parents."

    "And so, you wait in place, preparing yourself for the most daring getaway you\'ll ever do."

    azure "Three..."

    azure "Two..."

    if persistent.tough_decisions_1["TD2"] == "antidote":

        "Gripping your fake leg, you brace yourself."

    azure "NOW!"

    "Azure flings an empty bottle toward a small house, it shatters with a loud crack."

    villager "What was that?!"

    azure "We\'re under attack!"

    "The villagers start to panic, but you secretely take off..."
    
    "Going for Exaqlyon\'s ship, who\'s already one foot high above the ground."

    mc "{i}Please make it... please make it...{/i}"

    mom "[persistent.name.upper()]! Where are you going?!"

    dad "[persistent.name.upper()]! Stop right now!"

    "You hear your parents from behind you, but you don\'t care, you keep on running."

    "Once you\'re nearby, you took one huge leap for the ship."

    $ renpy.pause(1)

    "..."

    $ renpy.pause(1)

    "And your hand latch onto the platform."

    mc "Hnggh..."

    mom "[persistent.name.upper()]!"

    "As you continue to rise, you bring yourself up... Finally standing on the narrow platform."

    "As you ascend higher, you see the villagers... with your parents from below."

    "Looking at you..."

    scene bg black
    with fade

    $ renpy.pause(1.0)

    $ notify("Chapter 4 Complete", "You've finished Chapter 4. Don't forget to save!")

    $ persistent.progress['complete_ch_4'] = True

    if persistent.gender == "Male":
        $ persistent.romance_points['Exaqlyon'] += exaqlyon_points
    
    else:
        $ persistent.romance_points['Terrence'] += terrence_points
        
    $ renpy.save_persistent()
    $ renpy.pause(1.0)

    menu:

        "Continue?"

        "Yes":

            "Don't forget to save your game."
            jump chapter5
        
        "No":

            call screen episodes
            return