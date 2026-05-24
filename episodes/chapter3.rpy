default exaqlyon_points = 0

label chapter3:

    if persistent.gender == 'Male':
        $ exaqlyon_points = 0
        $ persistent.romance_points['Exaqlyon'] = 0

    $ persistent.outfit = persistent.outfits[0]

    if "Solaryx Jumpsuit" in persistent.outfits:
        
        $ persistent.outfits.remove("Solaryx Jumpsuit")

    $ renpy.save_persistent()

    "Chapter 3: An Alien World"

    scene bg spaceship
    with fade

    "You're standing inside Exaqlyon's spaceship. Taken Captive by Princess Exaqlyon to her home planet."
    
    "Glancing out the window, you see the Earth, your home planet, getting smaller and smaller."

    exaqlyon "Kraglin, Larx, Set course for home."

    kraglin "Understood, setting course now."

    larx "Set course for Solaryx, all system ready for takeoff, Your Highness."

    "As the two aliens take their place, Exaqlyon stands in the middle, typing something on her dashboard."

    exaqlyon "Prepare for takeoff. Hyperspeed in Three... Two..."

    "She pulls a lever."

    exaqlyon "...One."

    "You suddenly feel being pulled, going at insane speed."

    "Funny enough, your body doesn't get pulled forward, you feel the sensation, but your body stays where it is."

    mc "Whoa..."

    "After a short while, the hyperspeed disappears, and you slowly regain your balance."

    mc "...Okay, wow."

    exaqlyon "Excellent, how long until we reach home, Larx?"

    larx "Approximately 10 minutes, Your Highness."

    exaqlyon "Okay, let's take a breather. Let the ship do its thing."

    kraglin "Understood."

    "Larx, a purple alien with one eye... Along with Kraglin, the Brown alien with hornets on his head, take their leave."
    
    "Leaving you alone with Exaqlyon, who's still focuses on her console."

    "You muster the courage to approach her, and she snaps her head at you instantly."

    exaqlyon "Can I help you?"

    if persistent.gender == 'Male':
        
        tutorial "You just meet your potential {b}Love Interest{/b} for the story, which means you can choose to flirt with her."
        
        tutorial "Every love interests in this game are Non-Humans."

        tutorial "Alternatively, you can choose not to if you don't like it. Every romantic options are marked with the 💗 symbol."
    
    menu:

        mc "Can I ask you..."

        "What are you doing?":
            
            exaqlyon "None of your business."

            mc "Ouch. Didn't take you as a cold shoulder."

            exaqlyon "Look, whatever it is you're planning, just stop, okay?"

            exaqlyon "It's not going to work. You can't bribe me into letting you go."

            mc "I'm just trying to make a small talk, geez."

        "Who are those two?":
            
            exaqlyon "Why do you want to know so much?"

            mc "Huh?"

            exaqlyon "What's your plan here human? Are you trying to persuade me into letting you go?"

            mc "I'm not--"

            exaqlyon "Well those two are my bodyguards, but I don't need them, I can wreck you with just using my mind."

            exaqlyon "So don't even {i}think{/i} about fighting back!"

            "She leaves an awkward silence in the room."

            mc "Oooookaaaay... Definitely not the time for small talk."

        "💗 I like your ears." if persistent.gender == 'Male':
            
            $ exaqlyon_points += 1

            "Exaqlyon's eyes widen, her ears curled down as she tries to speak."

            exaqlyon "You... you... what?"

            "She shakes her head."

            exaqlyon "What are you trying to do here, human? Are you trying to persuade me to letting you go?"

            mc "No, I genuinely like your ears."

            exaqlyon "Don't lie to me! You're planning something, I know it."

            exaqlyon "And it's not going to work!"

            "She leaves an awkward silence."

            mc "Oooookaaaay then..."

    "You turn back as she continues typing."

    "You take a glance out the window and spot a planet, its surface as bright as a gold."

    mc "Wow, is that your home planet?"

    "Exaqlyon snorts."

    exaqlyon "{i}Technically{/i} yes. But Solaryx hasn't been my home for quite some time now."

    exaqlyon "Who needs a planet when you can have a whole galaxy."

    "You notice the sadness in her eyes."

    exaqlyon "But that doesn't matter."

    "She walks up to you."

    exaqlyon "Listen to me human--"

    mc "I have a {i}name{/i}, you know!"

    exaqlyon "And I have this blaster, would you like it in your mouth as I pull the trigger?"

    mc "...Never mind."

    exaqlyon "When we enter that planet, you do {i}exactly{/i} as I say, got it?"

    menu:

        mc "..."

        "Okay, exactly like you say, got it.":
            
            exaqlyon "Good. I'm glad you're with me on this, [persistent.name]."

        "What happens if I don't?":
            
            exaqlyon "You're not in a position to make demands right now, [persistent.name]."
    
    mc "How did you know my name?"

    exaqlyon "I have {b}precognition{/b} ability. I can read people's minds."

    exaqlyon "Well... a piece of their mind at least, I can't read the entire thing nor can I predict the exact future."

    exaqlyon "I can only sense a {i}glimpse{/i} of it."

    "She walks back to her control panel, and type something on the dashboard."

    exaqlyon "Once we enter the planet's orbit, you will talk to the highest authority in my planet."

    exaqlyon "In other words, {b}my parents.{/b}"

    exaqlyon "They will decide whether or not you can keep your little planet, or everything is destroyed."

    "Exaqlyon looks you up and down."

    exaqlyon "And judging by your outfit, you're not exactly their type."

    mc "Well, maybe because I don't have the same luxury as you."

    exaqlyon "That's not an excuse. Luckily, you have me."

    "She presses a button, and a hologram flickers in front of you, revealing a space jumpsuit."

    exaqlyon "This is a common outfit in Solaryx, I advise you wear it if you want to {i}at least{/i} have a shot in persuading them."

    mc "And if I don't?"

    if persistent.gender == 'Male':
        
        exaqlyon "Are you seriously thinking that handsome face will work on my parents? Yeah sure."

        menu:

            mc "..."

            "💗 Did you just call me handsome?":

                $ exaqlyon_points += 1
                
                "Exaqlyon blushes."

                exaqlyon "I... I didn't say that I--"

                mc "So I'm {i}not{/i} handsome?"

                if exaqlyon_points > 1:

                    "Exaqlyon shakes her head again, but you can see a smile on her face."

                    exaqlyon "You're really pushing your luck here, human."
                
                else:

                    "Exaqlyon shakes her head, realizing you're just teasing her."

                    exaqlyon "Anyways..."

            "There's a first time for everything.":

                exaqlyon "Not with my parents." 

    else:

        exaqlyon "Are you seriously thinking that pretty face will work on my parents? Yeah sure."

        mc "Well... there's a first time for everything."   

        exaqlyon "Not with my parents."
    
    exaqlyon "Now are you going to wear the suit or not?"

    tutorial "Several outfits can be useful in certain situations."

    tutorial "Wear the {b}Solaryx Jumpsuit{/b} to gain respect from the people of Solaryx."

    menu:

        "Outfit: Solaryx Jumpsuit."

        "Take it.":
            
            mc "Okay, suit me up."

            exaqlyon "Hm, that's the best decision you've made so far."

            "She clicks a button on her dashboard, and immediately you see the hologram materialized into an actual jumpsuit."

            "You wear the jumpsuit and look at yourself in the window."

            $ persistent.outfits.append("Solaryx Jumpsuit")

            $ persistent.outfit = persistent.outfits[-1]

            mc "Whoaa..."

            "Even Exaqlyon looks at you with amazed look."

            exaqlyon "You look... nice. Now you're just like a Solaryx citizen."

            mc "I look good, thanks Princess Exaqlyon."

        "Leave it":
            
            mc "I'll pass. I don't really trust your gadgets and trinkets."

            exaqlyon "Suit yourself."

            exaqlyon "No pun intended."

            mc "Thanks anyway, Princess Exaqlyon."
    
    exaqlyon "Ugh, please. Call me Exa."

    exaqlyon "Having others call me by my full name gives me a migraine."

    "The plane enters the Solaryx orbit, and soon you see the glamorous view of Solaryx."

    # Change background here.

    "After a while, a massive white castle stands tall before you as the ship lands on the ground."

    "As the door opens, Exaqlyon gestures you to follow her."

    exaqlyon "Follow me."

    "An alien approaches you."

    alien "Princess Exa, Welcome home. Your parents are waiting for you."

    exaqlyon "Hello Zyphax. Lead the way."

    "The alien bowed as he leads you inside the castle."

    # Change background here

    "Inside, you see lots of aliens in fancy tuxedoes and elegant dresses talking in a group."

    zyphax "Your Highness, Princess Exaqlyon has arrived!"

    if persistent.outfit == "Solaryx Jumpsuit":

        "As you walked through the crowd, a lot of aliens bow their heads, showing signs of respect."
        
        mc "(Heh... I'm glad I wear this.)."

        $ notify("One of the People", "You are respected by Exaqlyon's people.")

    else:

        "As you walked through the crowd, aliens start to murmur to each other, some shake their heads in disgust."

        mc "(I guess I should've worn a better outfit...)."

        $ notify("Cold Shoulders", "You didn't win the respect of Exaqlyon's people", color_title="#FF0000")

    "As you both walk forward together, you see two aliens, sitting on the throne."

    "The King says to his daughter."

    alien "Exaqlyon, you finally decided to return home."

    "The Queen also joins in."

    alien "And it appears you bring yet another {i}garbage{/i} with you."

    "The Queen glares at you menacingly."

    exaqlyon "Father, Mother, I have returned. During my conquest I--"

    alien "Oh spare me the fancy talk, Exa. All you do is wander around and escaping your destiny!"

    exaqlyon "But I--"

    alien "Your Father's right, Exa, it's about time you take up the responsibility and become the {i}{b}heiress{/b}{/i} of Solaryx."

    exaqlyon "But mom--"

    alien "I just can't see what you're actually {i}good at!{/i}"

    "You stand as you see Exaqlyon at a loss for words, her eyes begins to water."

    menu:

        mc "..."

        "Can I speak here?":

            "Exaqlyon's Father raises his voice."

            alien "Dirty slug! How dare you speak your part when you are not permitted!"

            alien "Now, now, {b}Zarktain{/b}, don't waste your energy with this one."

            zarktain "...You're right {b}Othelia{/b}. [persistent.pronouns['determiner'][persistent.gender].capitalize()] life won't be long after this."

        "I am [persistent.name] from Planet Earth.":

            alien "Dirty slug! How dare you speak your part when you are not permitted!"
            
            alien "Now, now, {b}Zarktain{/b}, don't waste your energy with this one."
            
            zarktain "...You're right {b}Othelia{/b}. [persistent.pronouns['determiner'][persistent.gender].capitalize()] life won't be long after this."

        "(Be silent)":

            "You bite your tongue, not daring to speak a word."

            mc "(I would like to back her up, but my life is also on the line here.)"

            "Exaqlyon seems to notice your effort, and you can see her expression relieved."

            alien "Now, {b}Othelia{/b}, what do you think shall we do with this trash our daughter has brought in."

            othelia "[persistent.pronouns['subject'][persistent.gender].capitalize()] won't be any use here. I say we kill it, {b}Zarktain{/b}."
        
    exaqlyon "Wait, what?"

    mc "K... Kill?"

    othelia "Yes, just like your other \"{i}discoveries{/i}\" you brought home."

    exaqlyon "But Mom! this is different! [persistent.pronouns['subject'][persistent.gender].capitalize()] comes from Planet Earth and there's--"

    zarktain "That planet is useless! We have an infinite water supplies, more food than any galaxies."

    if persistent.outfit == "Solaryx Jumpsuit":

        exaqlyon "But look at [persistent.pronouns['object'][persistent.gender]]! [persistent.pronouns['subject'][persistent.gender].capitalize()] already looks the part!"

        "She points at you, trying to win her parents over."

        othelia "[persistent.pronouns['subject'][persistent.gender].capitalize()] {i}does{/i} have enough decency to respect our customs."

        othelia "Still, a mere human from basically a wasteful planet is no good."

    exaqlyon "That's not true! I've found many other stuff from--"

    othelia "If it's \"{i}stuff{/i}\" I wanted I would've had an entire army at my command!"

    othelia "I say the word and they'll bring me the sun itself!"

    othelia "What I need is an {i}heiress{/i}! Someone to take up the throne and command her people!"

    zarktain "Exa, our planet is still rebuilding here. Can't you see what {b}{color=#FF0000}Grex{/color}{/b} did to our people?"

    exaqlyon "Grex hasn't even attacked for {i}milennia!{/i} It's obvious he won't attack us anymore!"

    othelia "He is still alive, Exa! He could attack at any moment!"

    exaqlyon "But--"

    zarktain "{i}{color=#FF0000}{b}ENOUGH{/b}{/color}{/i}!"

    "Zarktain's voice rattle the air around you as he steadies his breathing."

    zarktain "We will continue this discussion later. Throw this filthy human in a cell, we'll have [persistent.pronouns['object'][persistent.gender]] executed first thing next morning."

    mc "But--"

    exaqlyon "Don't bother! I'll take care of [persistent.pronouns['object'][persistent.gender]] right away!"

    "Exaqlyon dragged you by the arm, you can feel her mind locking your lips, preventing it from speaking as she walks outside."

    # Change backdrop here

    "Exaqlyon throws you inside her ship, the door closing in as the ship takes off."

    exaqlyon "Kraglin, Larx, take us to {b}{color=#FF0000}Obsidian Theta{/color}{/b}. Now!"

    kraglin "Understood."

    larx "Will be there in 10 minutes."

    menu:

        mc "Wait!"

        "What about me?":
            
            mc "I haven't even said my piece yet!"

            exaqlyon "Are you seriously thinking you can {i}convince{/i} my parents?"

            exaqlyon "Yeah right, they'll only hear what they want to hear."

            mc "Still! You can't just--"

        "I don't want to die here!":
            
            mc "You can't just--"


    exaqlyon "Oh shut your trap, I ain't going to kill you, idiot!"

    exaqlyon "This whole conquest thing is off."

    "You notice her furious expression."

    exaqlyon "Just who the {i}hell{/i} do they think they are?!"

    exaqlyon "Exa this! Exa that! You must do this! A proper lady must be able to do that!"

    exaqlyon "I'm so PISSED right now!"

    menu:

        mc "Exa..."

        "I'm so sorry...":

            exaqlyon "I don't need your fake sympathy, [persistent.name]!"

            mc "They're not, you might've captured me, Exa. But that doesn't mean I can't relate to you."

            exaqlyon "It's just... after 996 years..."

            "Exaqlyon looks at the window, sighing."

            exaqlyon "I just want to be {i}seen{/i} for once."

        "That must have been rough on you.":
            
            "Exaqlyon snorts."

            exaqlyon "Oh wow really? Wow... I thought it was {i}fun{/i}."

            mc "I'm not trying to be sarcastic, Exa, I really {i}do{/i} feel you."

            exaqlyon "...996 years... And they {i}still{/i} won't acknowledge me."

        "You shouldn't let them talk to you like that!":

            mc "That whole conversation was stressful, I can't believe you managed to stay composed."

            exaqlyon "Yeah well, that's what you get after living together for 996 years."

            "Exaqlyon gazes out the window."

            exaqlyon "Why can't you just look {i}my{/i} way?"
        
    mc "Hold up, {b}{i}Nine hundred and ninety six{/i}{/b} years?! You're 996 years old?"

    exaqlyon "Are you implying that I'm {i}old{/i}?!"

    mc "No! It's just... you look so young!"

    "Exaqlyon looks at you for a moment, before stifling a laugh."

    mc "What's so funny?"

    exaqlyon "Your mind, you're trying to count when I was born..."

    mc "Hey!"

    exaqlyon "Ahh humans, you really {i}are{/i} foolish."

    exaqlyon "Our calendar aren't the same, silly."

    mc "So how old are you in my planet?"

    if persistent.gender == 'Male':

        exaqlyon "Excuse you, you do {i}not{/i} ask a lady that!"

        exaqlyon "And besides, I still control your life!"

    else:

        exaqlyon "Hold up there, human! We're not {i}that{/i} close yet!"

        exaqlyon "Need I remind you that I am still in control of your life?"

    mc "Sorry."

    exaqlyon "It's whatever."

    if persistent.romance_points['Exaqlyon'] > 0:

        "Exaqlyon looks away, but you can see a blush in her cheeks."
    
    else:

        "Exaqlyon looks at her dashboard."

    mc "So... where are we going? I don't recall you saying we're going back to Earth."

    exaqlyon "Yeah, I kinda forgot about that. I was so stressed out that time."

    exaqlyon "Don't worry, I'm rerouting us right now."

    mc "Wait, you mean I could've gone with you to another planet?"

    exaqlyon "Well... I could, but I figure you might have somewhere else you need to go."

    mc "What is that place anyway?"

    exaqlyon "{b}{i}Obsidian Theta{/i}{/b} is a place filled with hot springs. That's where I usually go to clear my head."

    mc "You mean... A place of hot spring?"

    exaqlyon "It's very relaxing, you know."

    exaqlyon "I once go there after a rough training, and my cuts healed right after I jump in."

    tutorial "Join Exaqlyon on her trip to the hot Springs and get to know her better."

    tutorial "You might want this mind controlling Diva to be on your side!"

    if not persistent.injured:

        tutorial "You can even obtain a healing item that can help you in the future battle."

    else:

        tutorial "You can even obtain a {b}{color=#00FF00}healing item{/color}{/b} that can heal your injury!"
    
    menu:

        "Side Quest: An Alien Princess"

        "I can wait, take me with you!":

            exaqlyon "Seriously?"

            mc "I mean... it's not everyday I get to explore space, right? Might as well."

            "Exaqlyon rolls her eyes, but is smiling."

            exaqlyon "Welp, good thing I haven't changed course."

            "You wait as the ship enters the planet's orbit."

            # Change backdrop here

            "After a while, the ship lands on Obsidian Theta, the planet Exaqlyon mentions."

            "You look out the window and see lots of lava geysers erupting from the ground, several lava puddles are visible as well."

            mc "Wow."

            exaqlyon "Like what you see? Wait until we land."

            "The ship door opens, and both of you exit the ship."

            "The atmosphere is hot, so hot you immediately start sweating."

            exaqlyon "Ahh... perfect."

            "Exaqlyon unzips her jumpsuit, revealing her tank top."

            if persistent.gender == "Male":

                menu:

                    mc "Exaqlyon's in a tank top."

                    "Look away!":

                        "Exaqlyon notices you."

                        exaqlyon "Have you never seen a woman in a tank top before?"

                        mc "I have, but it's indecent to look at a woman changing her clothes."

                        exaqlyon "Pfft... You are {i}such{/i} a prude."

                    "💗 Stare.":

                        $ exaqlyon_points += 1

                        "Exaqlyon notices you staring."

                        exaqlyon "Like what you see?"

                        "Mouth wide, you can't muster a word as Exaqlyon looks at her own body, face flushed."

                        exaqlyon "Umm... Well... Try not to stare {i}too{/i} much."
            
            else:

                mc "You really come prepared, huh?"

                exaqlyon "Considering how my parents are, you can say I come here almost everyday."
            
            "As you two walk further, you spot a huge volcanic crater nearby."

            exaqlyon "There it is!"

            "Exaqlyon hurriedly jump into the crater!"

            mc "Exa, wait!"

            "{i}Splash!{/i} Lava popped out of the crater, you reflexively dodge the lava."

            mc "Hey! Watch it!"

            "She reemerges from the crater."

            exaqlyon "Aahhh... Now {i}this{/i} is living the good life."

            mc "You almost hit {i}me{/i} with that!"

            exaqlyon "Well? What are you waiting for? Aren't you going to jump in?"

            menu:

                mc "Excuse me?"

                "No thanks, I like my skin moist.":

                    exaqlyon "But this will {i}also{/i} make your skin moist."

                "Are you trying to kill me?":

                    exaqlyon "I {i}was{/i}, but not anymore, remember?"
            
            exaqlyon "Wait, you're telling me humans {i}cannot{/i} enter lava?"

            mc "We can, it will only melt us to smitherinees that's all..."

            exaqlyon "Then why would you even come with me here, then?"

            mc "When you say {i}Hot Springs{/i}, I didn't think you mean it {i}literally{/i}, you know?"

            mc "I thought it was a pool of water, not lava."

            exaqlyon "Geez, you humans are so fragile."

            exaqlyon "Oh well, guess I can't play splash with you then."

            "As time passes, you notice Exaqlyon becoming more relaxed than ever."

            "Her soaked face glimmers with radiance as you lock eyes with her."

            menu:

                mc "Exa..."

                "Feeling any better?":

                    exaqlyon "Yeah... this really hits the spot."

                    exaqlyon "By the way, sorry with how we started things."

                    exaqlyon "And with making you deal with my absurd parents."

                "I'm sorry with the way we started things.":

                    exaqlyon "Nah, you don't need to apologize."

                    exaqlyon "If anything, I should be the one saying sorry."

                    exaqlyon "It was never my intention to conquer your home planet."
                
                "💗 You look beautiful." if persistent.gender == 'Male':

                    $ exaqlyon_points += 1 
                    
                    "Exaqlyon dips her face halfway into the lava. Sputtering something."

                    exaqlyon "Brbllbrl..."

                    mc "What's that? I didn't catch that."

                    "You can hear her voice in your head."

                    exaqlyon "I said, you're a flatterer."

                    "She pops her head back up, you can feel butterflies in your stomach."
            
            mc "So what are you going to do after this?"

            exaqlyon "What I always do, look for another planet, find something that might make my parents see me."

            exaqlyon "If I fail, I repeat."

            menu:

                mc "..."

                "Why don't you just stay exploring?":

                    exaqlyon "You do realize I have to stop at some point right?"

                    mc "No, I mean as a hobby, let your parents say whatever they want."

                    mc "Don't you think you have the right to enjoy life as well?"

                    mc "My parents won't let me hunt for food too, but I still sneak in from time to time."

                "Are your parents really {i}that{/i} important?":

                    exaqlyon "Excuse me?"

                    mc "Don't take this the wrong way, but it seems like you are trying to move a mountain by yourself."

                    mc "I mean, my parents won't let me fight for my people too at first."

                    exaqlyon "But you were so determined to fight me back there."

                    mc "I guess that's my ego right there."

                    mc "I'm sure you also have that moment, right?"

            "Exaqlyon thinks for a while, before sighing."

            exaqlyon "It's not that simple."

            mc "What do you mean?"

            exaqlyon "I am the only daughter in my family. So basically the crown princess."

            exaqlyon "My parents want me to take over the throne, that's why they get so upset whenever I leave the planet."

            exaqlyon "They want me to lead my people from the throne."

            "You recall what Exaqlyon's parents had said before."

            mc "Exa... This {i}Grex{/i} person, is that why your parents want you to lead?"

            exaqlyon "This Grex is supposedly an enemy in my home planet."

            exaqlyon "I never seen him before though. But it was said that he commited mutiny and wanted to overthrow my parents."

            mc "Is he really that powerful?"

            exaqlyon "Beats me, but I don't have to worry about that, I trust my people. We can defend ourselves."

            "Exaqlyon comes out of the crater."

            exaqlyon "Welp, that's enough stress for today, let's get you home."

            exaqlyon "Oh! I almost forgot! Wait here."

            "Exaqlyon runs inside her ship, before coming back carrying a tumbler."

            "She dips the tumbler inside the crater, collecting its lava."

            "She closes it, presses a button on it, and gives it to you."

            exaqlyon "Here."

            menu:

                "Obsidian Theta's Lava"

                "It's... cold?": 

                    if "Obsidian Theta Lava" not in persistent.healing_items:

                        $ persistent.healing_items.append("Obsidian Theta Lava")
            
            "You take the tumbler, it feels cold, like holding an ice block."

            mc "Whoa."

            exaqlyon "The lava here has healing properties. But it's actually more powerful when cold."

            exaqlyon "If you rub the cold lava along your injury, you'll heal right up."

            if persistent.injured:

                "You open the tumbler and begin applying it to your wound."

                "The cold lava began smoothing your injuries... until you can feel yourself lighter than air."

                mc "Wow, you're right, Exa! I feel much better."

                $ notify("Injury Healed!", "You use Obsidian Theta Lava to heal your injuries.")

                $ persistent.injured = False

                mc "Can I take this again?"

                exaqlyon "Maybe another time, that tumbler needs to recharge, before it can be used again."

                exaqlyon "Charging it while the lava still inside might damage the circuits too, and it's the only bottle that I have."

                mc "Oh okay."
            
            else:

                "You put the tumbler in your bag."

                $ notify("Medicine Acquired", "You acquire the Obsidian Theta Lava!")

                mc "Thanks, Exa. I'll keep this with me."

                exaqlyon "Don't lose that tumbler now, it's the only one I have."
            
            exaqlyon "Let's go."

            "You both make your way back to Exaqlyon's ship."

            $ notify("A Galaxy Next Door", "You visit the Hot Spring with Exaqlyon.")

            $ persistent.side_quests_1['An Alien Princess'] = True

            # Change backdrop here

            "Back in the spaceship, Exaqlyon begins typing in her dashboard."

            exaqlyon "Kraglin, Larx, head for the Milky Way Galaxy, head for the Earth."

            kraglin "Finfing the shortest route now."

            larx "Heading for Planet Earth, approximately less than 10 minutes, Your Highness."

        "Best of luck, then.":

            exaqlyon "Pfft... who needs luck when you have minds like this?"

            exaqlyon "Changing course now."
        
            $ notify("Down to Earth", "You didn't go with Exaqlyon.")
        
            $ persistent.side_quests_1['An Alien Princess'] = False

    # Change backdrop here

    "Within minutes, the spaceship lands on the Earth. Across some flower beds and near a river."

    "The door opens, and both you and Exaqlyon step out."

    mc "Home at last."

    "You look around and notice it's already night time."

    mc "Huh? It's evening already? I thought we were only gone for a few hours?"

    exaqlyon "I told you our calendar system is different. Yours is too long."

    "You take a deep breath, relieved to have finally made it back home."

    if persistent.side_quests_1["An Alien Princess"]:

        exaqlyon "Well then, my job here is done."
    
    else:

        exaqlyon "Well then, I believe there's a hot spring calling my name."
    
    exaqlyon "Goodbye, [persistent.name]."

    menu:

        mc "Goodbye, Exa."

        "I hope we can meet again in the future":
            
            exaqlyon "I wouldn't bet on it."

        "Good luck with your parents.":
            
            exaqlyon "Yeah... with {i}them{/i}."

        "Don't go shooting other people's planets again.":

            exaqlyon "I can still shoot {i}this{/i} planet, you know?"

            mc "I was joking."
    
    "Exaqlyon gives you one last look."

    exaqlyon "Well then, I'll take my leave and--"

    placeholder "And where do you think {i}you're{/i} going?"

    "A familiar voice calls out to you. You look at the direction of the voice, only to find..."

    mc "Terrence!"

    "Terrence steps from the shadows, looking straight at Exaqlyon with fury in his eyes."

    exaqlyon "Ugh, what are {i}you?{/i}"

    "Terrence stretches his tentacles out, his stance ready to fight."

    terrence "How {b}{i}DARE{/i}{/b} you return to this planet!"

    scene bg black
    with fade

    $ renpy.pause(1.0)

    $ notify("Chapter 3 Complete", "You've finished Chapter 3. Don't forget to save!")

    $ persistent.progress['complete_ch_3'] = True

    if persistent.gender == "Male":
        $ persistent.romance_points['Exaqlyon'] += exaqlyon_points
        
    $ renpy.save_persistent()
    $ renpy.pause(1.0)

    menu:

        "Continue?"

        "Yes":

            "Don't forget to save your game."
            jump chapter4
        
        "No":

            call screen episodes
            return