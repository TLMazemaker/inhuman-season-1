default persistent.name = "Lynn"
default persistent.gender = "Male"
default persistent.pronouns = persistent.pronouns_male

label setup_character:

    $ persistent.name = renpy.input("Before we start, who are you: ", default=persistent.name)
    $ persistent.name = persistent.name.strip()

    menu:

        "What gender should you be known as?"

        "Man":

            $ persistent.gender = "Male"
            $ persistent.pronouns = persistent.pronouns_male
        
        "Woman":

            $ persistent.gender = "Female"
            $ persistent.pronouns = persistent.pronouns_female

    menu:
        
        "Welcome [persistent.name], ready to face the apocalypse?"

        "Only one way to find out.":

            return

        "Actually... I'm not ready yet.":
            
            jump setup_character

label chapter1:

    "Chapter 1: The Human Survivor"

    "Planet: Earth.\nPresent Day."

    call setup_character

    show bg van
    with fade

    "You're sitting in a van, ready for your first mission."

    mc "..."

    "You're lost in your own thoughts, trying to remember your training."

    mc "(I got this, just have to remember the prep.)"
    
    mc "(Always have a {color=#00FF00}weapon{/color}, Finish things {color=#00FF00}as quickly as possible{/color}, And {color=#00FF00}no loud noises{/color}.)"

    "Beside you, your brother Lee pats you on the back."

    lee "There's still time to go back if you're too scared."

    menu:

        mc "..."

        "No, I can do this. I'm ready.":

            lee "Says the person who's shaking like crazy."

            mc "Wow, thanks for the comfort. Really just what I needed right now."

            lee "I'm not here to make you feel better. I'm here to make sure you're {i}prepared.{/i}"

        "Lay off bro! Don't mess with me right now.":

            "Your brother lay off his hands."

            lee "You know, there's a saying 'Better safe than sorry.'"

            mc "And there's also a saying 'Mind your own business.'"

            "Your brother shrugs."

            lee "Whatever your say kid."
    
    mc "It's just... I've been wanting this my whole life and now..."

    lee "You're starting to regret it. Yeah I've been there."

    mc "Really?"

    lee "Yeah, when I said I wanted to babysit you here."

    lee "Turns out you are a handful."

    mc "You are seriously {i}not{/i} helping the situation here!"

    lee "What else do you want me to say? Thing is, in the wilderness, it's {i}you{/i} or {i}them.{/i}"

    menu :

        mc "Well..."

        "I know how to take care of myself.":

            "Your brother snorts."

            lee "You got a lot of confidence for someone on their first mission."

            mc "And you got a lot of ego for someone who's about to be murdered."
        
        "That's no excuse to be such a jerk!":

            "Your brother snaps his head at you, you can tell he's offended."

            lee "Excuse me?"

            "You look away, averting his eyes."

            mc "Hmpf."

            lee "Listen kid, I don't care what you think of me..."
            
            lee "But once you see what's {i}really{/i} out there, you'll wish there's more people like me."

            mc "{i}I wish people like you got devoured by the zombies.{/i}"

    lee "What did you just say to me?!"

    mc "I said--"

    "The van jerks to a stop."

    driver "Cut it, both of you! We're here."

    "You both step out of the van, fuming at each other..."
    
    show bg jungle
    with fade

    "The woods are dark, you carefully remember your training. How to observe your surroundings in poor lighting."

    mc "..."

    menu:

        "Carrying your bag of supplies with you, you take out..."

        "A bow and arrows":

            $ notify("New Weapon!", "You've acquired a bow and arrows!")

    tutorial "The apocalypse could be a devastating place."

    tutorial "A weapon in hand can help you in tricky situations."

    "You track the forest, side by side with Lee. You saw a deer at the corner of your eye."

    deer "{i}Munch... Munch...{/i}"

    lee "{i}Over there, see if you can shoot it.{/i}"

    "You put your bag to the ground and take out an arrow."

    menu:

        "Take aim, and..."

        "Shoot!":
            pass

    "Your arrow soars... and passes just above the deer's body."

    deer "?"

    "The deer takes off running."

    mc "{i}Damn.{/i}"

    "Lee shakes his head, turning to you."

    lee "{i}Stay here, I'm going after it.{/i}"

    mc "{i}What?{/i}"

    lee "{i}I'll go there and finish it off.{/i}"

    mc "{i}Like hell you are. We move together.{/i}"

    lee "{i}Seriously kid, I'm running out of patience here.{/i}"

    mc "{i}Like you know anything about patience.{/i}"

    lee "{i}Don't make this harder than it already is.{/i}"

    menu:

        mc "{i}Screw that, Lee!{/i}"

        "{i}I can take care of that deer.{/i}":
            
            lee "{i}Yeah? Like what you just did by amazingly missing the shot? You had one job, [persistent.name].{/i}"

            mc "{i}So abandoning me here is a good idea?{/i}"

            lee "{i}Whoever says anything about abandoning you?{/i}"

        "{i}You've been an ass since we started this mission.{/i}":
            
            lee "{i}We're NOT talking about this right now!{/i}"

            mc "{i}Why not? I'm sick of you constantly judging me and treating me like a liability.{/i}"

            lee "{i}With this attitude of yours? Who wouldn't think of you as one?{/i}"
        
    lee "{i}Face it [persistent.name], you're not ready yet!{/i}"

    mc "{i}Screw that! I'm outta here!{/i}"
    
    mc "{i}I hope you get eaten alive by the zombies!{/i}"

    "And just like that, you take off running... Running deeper into the woods!"

    lee "{i}[persistent.name]{/i}"

    "You run through the forest, you don't even follow the sound anymore. You just keep running, and hope that you'll make it back to the van..."
    
    "But you don't, you're lost!"

    mc "Hff... Hff..."

    "Suddenly... You're being tackled down... by your brother!"

    mc "A--"

    "He shuts your mouth before you could scream."

    lee "{i}The hell's wrong with you, you maniac?!{/i}"
    
    lee "{i}Even if we argue, you can't just run away like that!{/i}"

    menu:

        mc "Hrr..."

        "{i}Fine, Let me up!{/i}":

            lee "{i}I don't think so, kid.{/i}"

            lee "{i}Clearly, you're not ready. I'm bringing you back to the village.{/i}"

            "He starts to get up..."

            "When he trips!"

        "(Shove him!)":

            "You shove your brother... hard!"

            "The force causes him to trip!"
    
    lee "Gahh..."

    lee "AHHHH!!!"

    "Lee screams as he plummets down the hill."
    
    "His scream manages to attract some zombies from the forest. Your brother's trapped!"

    mc "Lee!"

    "You want to help your brother... but you realize that you only have your bow and arrows."
    
    "While the rest of your supplies are located in your bag... at the entrance of the forest!"

    lee "[persistent.name]! Go! Get outta here!"

    mc "What about you? There are too many of them!"

    lee "The longer you stay here the smaller your chances are of escaping this forest!"

    "Lee tosses you a compass."

    lee "Go south! That's the exit to this forest! I can take care of this!"

    "Mind racing, you think of the best thing you could do in this situation."

    mc "(I can't let him die because of me... but what hope do I have?)"
    
    mc "(Then again... I could go back to my supplies THEN save Lee... but is it fast enough?)"

    tutorial "Throughout Inhuman, you will encounter several ☠️{b}TOUGH DECISIONS{/b}☠️."
    
    tutorial "These are certain situations in which case, there's {b}NO{/b} right answer. You just gotta make a call, and then live with whatever results you get."
    
    tutorial "Keep in mind that aside from {color=#00FF00}{b}benefits{/b}{/color}, there are also {color=#FF0000}{b}consequences{/b}{/color}."
    
    tutorial "No pressure though..."

    menu :

        mc "(What should I do?)"

        "☠️ Get to your supplies! ☠️":

            jump chapter1_supplies

        "☠️ Get to your brother! ☠️":
            
            jump chapter1_brother
            
label chapter1_supplies:
        
    mc "J-just hold on, okay?"

    "You sprint as fast as you can back to the entrance of the forest."

    lee "Alright assholes, do your worst!"

    "You're running even further... further... hoping you can make it in time."
    
    "Up ahead... You see a tree trunk laying {color=#00FF00}{b}horizontally{/b}{/color} blocking your path."

    tutorial "Some choices are timed! Hurry!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter1_timer_out1'
    show screen countdown
    menu:

        mc "(I should...)"

        "(Run!)":
            hide screen countdown

            jump chapter1_timer_out1

        "(Jump!)":
            hide screen countdown

            "You leap! Crossing the trunk with ease."

            mc "Come on! COME ON!"

            jump chapter1_supplies1
        
        "Duck!":
            hide screen countdown

            jump chapter1_timer_out1

label chapter1_timer_out1:
    
    "Filled with adrenaline, you tripped against the tree trunk."

    mc "Oof!"

    "You quickly recovered and continue running!"

    jump chapter1_supplies1

label chapter1_supplies1:

    "You finally make your way to your bag... Which is surrounded by 3 zombies!"

    mc "(Damn!)"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter1_timer_out2'
    show screen countdown
    menu:

        mc "(I should...)"

        "(Fire an arrow!)":
            hide screen countdown

            "You take an arrow and shoot it at one of the zombies."

            zombie "Blarghhh..."

            "The other two spot you!"
            
            "But you're faster, you take out two more arrows and shoot them dead in the skull."

            zombie "Urk..."

            zombie "Ggghhh..."

            jump chapter1_supplies2

        "(Smash them with a rock!)":
            hide screen countdown

            "You pick up a rock and bash it on one zombie's head."

            zombie "Urk..."

            "You whip around and bash the other zombies in the skull."

            zombie "Aghh..."

            zombie "Hrkk..."

            jump chapter1_supplies2

label chapter1_timer_out2:
    
    "Panic overwhelms you... You stay there, motionless."

    "One of the zombies turned around... Spotting you!"

    zombie "Hissss..."

    mc "Uh oh..."

    "You immediately rush forward, slamming the zombies as you pass through."

    zombie "Ggh?"

    "You almost reach your bag when one zombie pulls your foot down."

    mc "Oof!"

    "You turn around and kick it in the jaw before it could bite you."

    zombie "Grkk..."

    jump chapter1_supplies2

label chapter1_supplies2:

    mc "Die, you filth!"

    "You make your way to your bag and strap it to your shoulders..."

    "And run back to the forest."

    mc "(Hang on Lee, hang on for me...)"

    "While running back to your brother's location, you hear a loud screaming."

    lee "ARGGGHHHHH!!!!!"

    mc "LEE NO!"

    "You see your brother already pinned down by a bunch of zombies..."
    
    "So much you don't know how many."

    mc "Lee I... Oh God..."

    lee "Urgh... [persistent.name]... G-go! G-g-get outta--"

    "Before he could finish, a zombie stabs him in the eye! Pulling his eye from its socket!"

    lee "G-ggh-brr Ac-ghh..."

    "Unable to save your brother, you feel your legs running. Running back to where you came from."

    $ notify("Tough Decision!", "You manage to save your supplies... But not your brother!", color_title="#FF0000")

    $ persistent.tough_decisions_1['TD1'] = "supplies"

    jump chapter1_1

label chapter1_brother:
    
    mc "G-get... Get away from him!"

    "Without hesitation, you slide down the cliff."

    lee "What the hell do you think you're doing?"

    mc "Saving your ass! Are you gonna help me or what?"

    "You take aim with your bow and..."

    tutorial "Some choices are timed! Hurry!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter1_timer_out3'
    show screen countdown
    menu:
        
        mc "(I should aim the arrow...)"

        "(Into the distance!)":
            hide screen countdown
            jump chapter1_brother_wrong

        "(At the zombie's head!)":
            hide screen countdown

            "Your arrow soars..."

            "...And lands right into the zombie's skull."

            zombie "Ggrghh..."

            lee "Damn kid, nice moves."

            mc "I told you I can do it, now focus!"

            jump chapter1_brother1

        "(Just shoot it!)":
            hide screen countdown
            jump chapter1_brother_wrong

label chapter1_brother_wrong:

    "Your arrow soars... but hits none."

    mc "Uh oh..."

    "The zombies surround you, one of them scratches your face!"

    mc "Aghh!"

    lee "Get the hell away from my [persistent.pronouns['sibling']]!"

    "Lee charges forward, breaking the zombie's neck with his bare hands."

    mc "Okay, wow."

    lee "Focus kid!"

    jump chapter1_brother1

label chapter1_timer_out3:

    "You can't decide where to shoot the arrow."

    mc "Um... Uhh..."

    lee "Do something dammit! Shoot the damn arrow!"

    mc "Don't rush me! I--"

    "You're being cut short when a zombie scratches your face!"

    mc "Ack!"

    lee "Oh hell no!"

    "Lee takes an arrow from your hand and stabs it into the zombie's skull."

    zombie "Urgg..."

    mc "Thanks for that."

    lee "You're supposed to save me, not the other way around."

    jump chapter1_brother1

label chapter1_brother1:
    
    "The other zombies get closer... you're starting to feel claustrophobic."

    lee "We need to get out of this hellhole!"

    "You think of a way to clear the path... When your foot steps on something."
    
    "You look down, and see a {color=#00FF00}{b}deer's antler{/b}{/color} on the ground."

    mc "I have an idea."

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'chapter1_timer_out4'
    show screen countdown
    menu:

        mc "(I'll...)"

        "(Flail wildly!)":
            hide screen countdown
            jump chapter1_brother_right

        "(Smack it around!)":
            hide screen countdown
            jump chapter1_brother_right

label chapter1_timer_out4:
    
    "You stand still... holding the antler in your hand."

    lee "Well? What are you waiting for?"

    mc "I... I'm not sure if I'm--"
    
    mc "Oof!"

    "One zombie pushes you to the ground."

    lee "You are {i}seriously{/i} hopeless. Give me that!"

    "Lee takes the antler and begins bashing the zombies!"

    jump chapter1_brother2

label chapter1_brother_right:

    "You swing the antler heavily, it hits some zombies... tearing their heads from their necks."

    zombie "Grkkk..."

    lee "Nice mo--"

    lee "Hey! Watch it!"

    mc "Sorry..."

    jump chapter1_brother2

label chapter1_brother2:

    "Within minutes, the road has been cleared."

    mc "There! Let's get out of here!"

    lee "After you."

    "You both run toward the exit when..."

    mc "Lee, wait! My bag, we can't--"

    lee "[persistent.name] please, we have to get out of here."

    mc "But--"

    lee "I'm begging you, if we don't get out now I don't think we'll ever see the light of day again."

    "Your stomach drops... Deep down you know that he's right."

    mc "Dammit..."

    "Heart heavy, you go out from the forest."

    $ notify("Tough Decision!", "You save your brother... but were forced to abandon your supplies!", color_title="#FF0000")

    $ persistent.tough_decisions_1['TD1'] = "brother"

    jump chapter1_1

label chapter1_1:
    
    "You finally make your way to the van."

    driver "There you are! What took you so long, and where's the food?"

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        mc "No time! We must leave quickly!"

        driver "But what about--"

        driver "Oh... I'm so sorry."
    
    else:

        lee "We have to get out now! There are zombies after us!"

        driver "Alright, hop in!"
    
    "The driver starts the engine and drives you back to the colony."

    show bg van
    with fade

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        "You sit there... alone, you look at the empty bench beside you."
        
        "The spot where Lee is supposed to be..."
        
        "Before your argument with him... When you said you wanted him to die..."

        show bg jungle
        with fade

        mc "{i}Screw that! I'm outta here!{/i}"

        mc "{i}I hope you get eaten alive by the zombies!{/i}"

        show bg van
        with fade

        mc "{i}Lee...{/i}"

        "Your brother is gone... he's really {i}gone{/i}. And he won't be coming back."
        
        "From the front seat the driver calls out to you."

        driver "You uhh... you okay back there?"

        mc "I'm good... just a little bit shaken."

        menu:

            "You open your bag of supplies and take out..."
            
            "Almond milk":
                pass
        
        "You chug down your favorite beverage since you were a kid."
        
        "Slowly your nerves start to relax."

        mc "..."

        "You rummage through the contents of your bag, and find a {color=#00FF00}{b}key{/b}{/color}."
        
        "The key to your secret {color=#0000FF}{b}food stash{/b}{/color}, along with other {color=#0000FF}{b}medicines{/b}{/color} and {color=#0000FF}{b}weapons{/b}{/color}."

        mc "{i}At least your sacrifice won't go in vain...{/i}"

        "After a while, the van finally arrives at your colony."
    
        "Putting Lee's compass into your pocket, you step out..."

    else:

        "You both sit in an uncomfortable silence, until..."

        lee "Hey, sorry about earlier. I shouldn't be cross with you."
        
        lee "And thanks for saving my life."

        "You look at your brother's eyes and sigh."

        mc "Our supplies Lee... everything important is in that bag, including our {color=#00FF00}{b}key{/b}{/color}."

        "Your brother fell silent, you can tell he's also worried."
        
        "Regardless, he manages to muster a smile at you."

        lee "Naw, don't worry about that, we can think of something else."
        
        lee "If not at least we can return here one day and {i}hope{/i} that bag is still there and not completely tarnished."

        mc "Well {i}that's{/i} reassuring."

        lee "Look, I know you're still mad about my behavior earlier but know this."
        
        lee "I am really proud of what you did back there, The whole reason I got all sappy was because..."
        
        lee "I was afraid of losing you. So I tried to make you change your mind."

        mc "But didn't you say I was ready? On my birthday?"

        lee "Anxiety got to me I guess... But you've proven me wrong."
        
        lee "I promise I won't treat you like a deadweight again."

        "You punch his shoulder playfully."

        mc "Gee... Thanks, punk."

        lee "Heh... whatever you say, brat."
    
        "After a while, the van finally arrives at your colony."
        
        "Putting Lee's compass back into your bag, you step out..."
    
    # Change backdrop here
    
    "...And immediately several pairs of eyes look at your direction."
    
    "You walk for a while, until your parents spot you."

    mc "Oh boy..."

    mom "[persistent.name]! You're okay!"

    dad "We were so worried!"

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        dad "Wait... Where's Lee?"

        "You muster the courage to tell your parents."

        menu:

            mc "Mom, Dad..."

            "I'm so sorry.":

                pass

            "He didn't make it.":

                pass

            "This is all my fault":

                pass
        
        "The townsfolk gasp, your mother starts to cry while your dad simply nods."

        dad "I see..."
    
    else:

        mom "How was it?"

        lee "It's uhh... It's something."

        mc "I'm sorry mom and dad, but I lost my bag."

        "Your parents look at each other, but they turn back to you and smile."

        dad "Don't worry about it. Those are nothing compared to you both."

    "Just then, Fabien, the head townsfolk who happens to be a good friend to your parents, comes to you."

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        fabien "Lee was a brave and kind young man. We will remember this day to honor him."
        
        fabien "Why don't you take a break [persistent.name]? We could find something else for dinner."

        "Your parents walk with Fabien, leaving you alone."
    
    else:

        fabien "I'm sure you both have had a tiring day, why don't we take a breather?"
        
        fabien "We could find something else for dinner. And maybe start thinking about your {color=#00FF00}{b}key{/b}{/color}."

        "Your parents walk with Fabien, leaving you with Lee."

        lee "I guess I'll also see you soon. And thanks again, for saving my life."
    
    "You started going for your house... when you ran straight to your best friend Azure!"

    azure "[persistent.name]!"

    mc "Azure? What are you doing here?"

    azure "Uhh {i}duh...{/i} being nosy of course, my best friend just finished [persistent.pronouns['determiner']] first mission."
    
    azure "I need to know how you felt."

    menu:

        mc "It was..."

        "Terrible":

            mc "Everything was falling apart. That was {i}not{/i} how I imagined my first mission would turn out."

            azure "Aw [persistent.name], I'm so sorry for what happened to you."

            azure "I'm sure you'll bounce back."

        "Kinda good, actually.":

            mc "I don't know why, but I feel this adrenaline inside me."
            
            mc "Does that make me a crappy person?"

            azure "Well, that depends. How much of a douchebag are you?"

            mc "Hey!"

            azure "Okay okay, sorry. Didn't mean to pry."
        
    azure "Look, what happened to you both were... terrible. But you can't keep dwelling on it."

    azure "What's done is done, and if you keep focusing on the past, you won't have time focusing on the future."

    "Despite yourself, you still manage to smile at [persistent.pronouns['object']]."

    mc "Thanks, Azure. I... needed to hear that."
    
    mc "Well, I think I've had enough of this whole shenanigans. I'm gonna take a walk outside the colony."

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        azure "Umm... you know your brother just died right? You're off adventuring again?"

        mc "I'm just clearing my head. Let this whole thing pass."

        mc "Besides, I didn't catch anything tonight."
    
    else:

        azure "Before dinner?"

        mc "I didn't catch anything tonight. And I'm not feeling it either."
    
    "Azure watches you intensely."

    azure "You know, you {i}could{/i} go with me. There's this awesome villa that I found the other day and I've been dying to explore it with you."

    mc "Wait, what villa?"

    azure "Just at the outskirts of town, I'm sure it has a {i}lot{/i} of {color=#00FF00}{b}valuables{/b}{/color} that would be helpful."

    tutorial "{b}Side Quests{/b} are a great way to earn collectibles that could help you later in the story, get close to your companion, or even take a break from the craziness of this universe."
    
    tutorial "Join Azure on [persistent.pronouns['determiner']] quest to the Abandon Villa, and obtain a {color=#00FF00}{b}Healing Item{/b}{/color}."

    menu:

        "Side Quest : Abandoned Villa."

        "Join Azure":

            jump premium1
        
        "Skip it":

            mc "I think an abandoned place is the last thing I needed right now."

            azure "Ah shoot. Well, I understand."

            azure "If you need to talk, you know where to find me, okay?"

            mc "Sure, thanks Azure."

            "You and Azure part ways. You walk outside your colony outpost, past some flower beds in the meadow."
            
            "Simultaneously, all the incident flashbacks started to kick in once more."

            # Change backdrop here

            if persistent.tough_decisions_1['TD1'] == 'supplies':

                mc "Lee I... Oh God..."

                lee "Urgh... [persistent.name]... G-go! G-g-get outta--"

            else:

                lee "If we don't get out now I don't think we'll ever see the light of day again."

                mc "Dammit..."
            
            # Change backdrop here

            mc "Oh no... No no no... Get out of my head!"

            # Change backdrop here

            mc "{i}I hope you get eaten alive by the zombies!{/i}"

            # Change backdrop here

            mc "Agh!!! Why won't you leave me alone!"

            "Just then, you hear a rustling sound from the distance."

            mc "Wha-- Who's there?"

            "Gripping your bow, you take out an arrow from your bag. You slowly walk away from the sound, hoping to get back to your colony."

            mc "{i}It's probably nothing, just the wind [persistent.name], just the wind.{/i}"

            "The sound appears again, you squint through the distance... And spot some pair of eyes, coming out from the trees."
            
            "A zombie horde, running to you!"

            mc "Holy..."

            "You run back to where you came from. Past some abandoned buildings, until..."

            azure "[persistent.name!]"

            mc "Azure? What are you doing here?"

            azure "I was going to the villa when I saw you got chased by zombies."
            
            azure "Come on, this way!"

            jump chapter1_resolution

label premium1:

    mc "Okay, I'm in!"

    azure "Sweet! Come on, this way."

    "Azure leads you out from your colony, past some bushes and flower beds along the way."
    
    "After some time walking, the villa came into view."

    mc "Wow, okay yeah you were right Azure. This is lit."

    azure "{i}Duh...{/i} Of course I was, I'm always right."

    "You look at the old sign in front of the villa."

    mc "'Daffodil Residence'. Hmm, weird."

    azure "What's up?"

    mc "It's just that, this villa was a part of some residence."
    
    mc "Yet, this is the only villa here, there are no other villas in the distance."

    azure "The materials of this house are old too. See the scrapes in the wall?"
    
    azure "Now come on, we're supposed to explore the inside part of the villa."

    "You both step inside, the cold and eerie wind suddenly blows down your body. Making you shiver."

    mc "Uhh... This place is empty right? I don't want to see any living corpses wandering in here right now."

    azure "Relax, most likely we're just going to see some old furnitures. If we're lucky we might see an actual dead body."

    mc "Ew."

    "Suddenly, you hear a whispering sound."

    placeholder "{cps=10}Aaaaaaahhhhh...{/cps}"

    mc "You hear that?"

    azure "It sounds like it's coming from up the second floor. Come on."

    "You and Azure go up the staircase, following the sound..."
    
    "Eventually, you found yourself facing a giant door."

    placeholder "{cps=10}Iiiiiiii'm nnnnoooootttt hhhaaappppppyyyyyyyy...{/cps}"

    azure "It sounds like it's coming from behind this door. Let me open it."

    mc "Are you sure this is a good idea?"

    azure "I mean, what's the worst that could hap--"

    placeholder "What are you two doing in MY villa?!"

    azure "Ahhhh!!!"

    "A ghost suddenly jumps out from the door... looking at you both with a mad expression on her face."

    placeholder "I told you already this building is NOT for sale!"

    menu:

        mc "Umm... uhh..."

        "We don't want any trouble!":

            placeholder "You standing right here is {i}already{/i} a trouble!"
            
            placeholder "Get out, or are you looking for your early grave?!"
        
        "Sorry, we're here to fix a pipe leak.":

            placeholder "Pipe leak? But no one is--"

            placeholder "Oh for ghost's sake you're working for Jeremy aren't you?"
            
            placeholder "Well I'm going to--"
        
        "What are you?":

            placeholder "What are {i}you{/i}? News reporter? I don't need the likes of you wandering in my territory."

            placeholder "Get out, before I make you stay here forever!"
    
    azure "Wait, we're just a pair of ghostbusters."

    mc "We are?"

    "Azure eyes you, you get the signal."

    mc "I mean, yeah. We're investigating this old building to umm... Make some friends?"

    placeholder "Ghostbusters you say?"

    "The ghost circles you both, you're starting to sweat when the ghost offers an answer."

    placeholder "Well why didn't you say so? I love ghostbusters, I've watched them since I was alive."

    azure "If I could ask... Who are you, Miss Ghost?"

    placeholder "My name is {color=#00ff00}{b}Clover{/b}{/color}, I've lived here since my death from the White Plague in 1985."

    mc "Nice to meet you, Miss Clover. I'm [persistent.name], and this is Azure."

    azure "I must say, your villa is looking {i}good{/i}. Like a castle from the Victorian Age."

    clover "Thank you, I quite enjoy it myself. My parents are from England so when they bought this villa, they used that theme so we could always feel at home."
    
    clover "But that... doesn't matter."

    "You notice her frowning, like brushing away a bad memory."

    mc "Miss Clover--"

    clover "Please, just clover is okay. We are about the same age."

    menu:

        mc "Right. Okay then Clover, could you tell me..."

        "Why are you a ghost?":

            clover "I beg your pardon?"

            mc "Sorry, I didnt mean to pry a bad memory but--"

            clover "No no, that's not what I meant."
            
            clover "You're saying you don't know why someone is a ghost after death?"

            "Clover eyes you suspiciously..."

            azure "Oh we know, we just want to know why {i}you{/i} become a ghost."
            
            azure "If a death is natural, then you shouldn't be wandering these walls for eternity."

        "Where are your parents?":

            clover "They uhh... They died, {cps=5}{color=#FF0000}{b}painfully.{/b}{/color}{/cps}"

            azure "Are they here right now?"

            "Clover suddenly looks annoyed."

            clover "No! Why would they? They aren't anything like me!"
            
            clover "They were lucky enough to die on their own terms while {i}I{/i} have to endure this madness."

            mc "Any specific reason?"
    
    "Clover suddenly goes pale. You can see the sadness in her eyes."

    clover "Look, I know you both are curious about me, but the truth is..."
    
    clover "I don't know much about my death and its connections to my ghostly being right now. I don't even know how I'm a ghost."

    "Clover stares at the wall, you can't tell if she's sad or angry."

    clover "Ughhh... It's like being dead all over again, everytime I think about it it hurts."

    "While Clover continues to grunt to herself, Azure pulls you aside."

    azure "{i}Okay, I don't know how we get into this mess but I feel like we need to help that girl.{/i}"

    mc "{i}But how? We're not the real ghostbusters. I don't even know that's a real thing.{/i}"

    azure "{i}If we look at her, she clearly doesn't want to be a ghost. She wants to be free.{/i}"
    
    azure "{i}But something prevents her from leaving. You know what it is, right?{/i}"

    menu:

        mc "{i}You mean...{/i}"

        "{i}Her parents?{/i}":
            pass

        "{i}Death memories?{/i}":
            pass

        "{i}This villa?{/i}":
            pass
    
    azure "{i}No, what prevents her is her {color=#00FF00}{b}attachment.{/b}{/color}{/i}"

    mc "{i}Uhh... Come again?{/i}"

    azure "{i}There are some things that she just couldn't tell yet.{/i}"
    
    azure "{i}Maybe, those things were the ones keeping her here because she isn't ready to let it go.{/i}"

    mc "{i}So what do you propose we do?{/i}"

    azure "{i}We get her to open up about her parents, with games.{/i}"

    "Azure walks back to Clover."

    azure "So, Clover. Let's do something fun now shall we?"

    clover "I don't think I'm in any way to have some 'fun' but... I'll try."

    azure "I'll ask about a category like fruits, sports, et cetera, and my friend [persistent.name] is going to ask some questions for me to spill some clues."
    
    azure "You must answer what object I'm thinking of. You have 3 chances so make sure to give your best answer, clear?"

    clover "Hmm... Okay, sounds promising."

    azure "Okay, I'll start. The first category is... {color=#00FF00}{b}Vehicle.{/b}{/color}"

    default opt1 = False
    default opt2 = False
    default opt3 = False

    call loop1

    azure "Come on, Clover. It's already too many clues that I've spilled."

    clover "I don't really remember much though, I'm guessing my final answer is a tank?"

    azure "Ooohh so close, but still wrong."

    clover "Drats!"

    mc "So what was the answer?"

    azure "Isn't it obvious? It's M1A2 SEP Battle Tanks."

    clover "Wha... that's, how on earth would {i}anyone{/i} guess that?"

    azure "Well, why don't we switch roles?"

    clover "I wanna try, it is {i}so{/i} on."

    mc "Oh boy, I'm the one answering."

    "After a while, the three of you finally ease up, laughing and playing."
    
    "It's almost as if there's not a single worry in the world."

    azure "Tomato isn't a fruit! It's a vegetable!"

    mc "Well, yeah. But why would it have seeds? Vegetables don't have seeds, right?"

    clover "Hahahaha, Azure {i}really{/i} got tricked there."

    "Eventually, you calmed down and started to talk on the sensitive subject."

    clover "Hey..."

    mc "Yeah?"

    clover "...Thanks for doing this, I can't remember the last time I laughed this loud."

    azure "What about your family? You never did any of this stuff?"

    clover "Well... My family was complicated. My parents always wanted me to be independent, to not depend on them."
    
    clover "But they didn't realize what they're missing."

    azure "You mean..."

    clover "When they found out I was sick, it was too late. I was at the end of my life."
    
    clover "My parents blame themselves for my death, so they committed suicide."

    mc "Oh no. Clover, I'm so sorry."

    clover "Everyday I hear whispers of them apologizing to me, they wanted to make sure I was at peace."
    
    clover "But I wasn't ready to forgive them yet. So those whispers are keeping me here. I couldn't escape because I just can't."
    
    clover "But you both showed me kindness, more kindness than {i}anyone{/i} I've ever met before. So, I guess I'm ready."

    "And with that, a shining light emerges from the ceiling. So bright you and Azure have to cover your eyes, You catch a glimpse of Clover being ascended back to the light."

    mc "Whoa."

    clover "Thank you, both of you."
    
    clover "For releasing me, I have left you something precious. Do use it wisely."

    "And just like that, she disappears."

    menu:

        "And in her place is... A box."

        "Open the box.":
            
            if 'Medkit' not in persistent.healing_items:

                $ persistent.healing_items.append('Medkit')

    "You open the box and reveal a med kit."

    mc "Whoa, look at this."

    azure "Nice."

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        "You put the med kit into your bag."

    else:

        "You lift the box of med kit."

    $ notify("Medicine Acquired", "You acquire the Med Kit!")

    mc "I guess I'll hold on to this for now."            

    azure "Sure thing. If anything, it'll come in handy."

    azure "Now come on, let's get out of here."

    "You both make your way out of the villa."

    $ notify("Ghostbusters", "You explored the abandoned villa with Azure.")

    $ persistent.side_quests_1['An Abandoned Villa'] = True

    azure "You know, that encounter really taught us something."

    mc "And that is?"

    azure "That you shouldn't let your past grief be attached to you."
    
    azure "If you keep on thinking about the past, you can't move on to the future, and you won't."

    mc "That... actually makes sense. You're right, Azure."
    
    mc "Instead of focusing on what I've failed to accomplish, I rather focus on what I can accomplish in the future."

    azure "{i}Duh...{/i} My name is Azure for a reason, [persistent.name]."

    azure "And that's not because my hair is blue."

    mc "Pffttt... Come on, we both know it's becau--"

    azure "Stop talking!"

    "Suddenly, Azure stops in [persistent.pronouns['determiner']] tracks."

    azure "There are zombies nearby, come!"

    mc "Wait, what? Whoaaa..."

    jump chapter1_resolution

label loop1:

    menu:
        
        mc "(I should ask...)"

        "Where does it operate?" if not opt1:
            $ opt1 = True
            
            azure "By land, of course."

            clover "A car!"

            azure "{i}Bzzzttt...{/i} Try again. You really think I'm gonna use something so simple?"

            clover "Drats!"

        "Is it common to use?" if not opt2:
            $ opt2 = True
            
            azure "Hmm... Depends on how you see it, For us? Not so much."

            azure "For some people however, it's pretty common."

            clover "I gotta need more clues to answer this."

        "When was it first invented?" if not opt3:
            $ opt3 = True
            
            azure "How the {i}hell{/i} would I know that, [persistent.name]?"

            mc "You know the answer, Azure. You gotta know everything."

            azure "I don't know. Around the 1900s maybe?"

            clover "Oh, I know! A carriage!"

            azure "{i}Bzzzttt...{/i} Try again. Nice try though."
    
    if opt1 and opt2 and opt3:
        return

    else:
        jump loop1

label chapter1_resolution:
    
    "Azure quickly pulls your hand into a secluded alley."

    azure "{i}Ssshhh...{/i}"

    "You look outside the alley, not seeing any signs of zombies nearby."

    mc "{i}Where is it?{/i}"

    azure "{i}There.{/i}"

    "Azure points toward the distance, two zombies making their way toward you."

    azure "[persistent.pronouns['subject']] looks back at you with a concerned expression."

    azure "Listen to me, I want you to go straight down this alley, go north to Mahomes Street."
    
    azure "There, you should be able to return to the colony."

    mc "But what about you, Azure?"

    "You look into Azure's eyes."

    if persistent.tough_decisions_1['TD1'] == 'supplies':

        mc "I can't lose you too, Azure."
    
    else:

        mc "I can't lose you, Azure."
    
    azure "It'll take more than a bunch of these bastards to kill me."
    
    azure "You won't lose me [persistent.name], that's a promise."

    "Azure takes out [persistent.pronouns['determiner']] daggers from [persistent.pronouns['determiner']] boots. The blades gleaming in the moonlight."

    azure "Now go! Return to the colony, I'll see you by sunrise."

    "With that, Azure gets out of the alley. It doesn't take long until you hear sounds of zombies being crushed."

    mc "Oh God..."

    "You immediately run towards the opposite direction."
    
    "Up on your track, you spot a zombie coming out of an alley."

    zombie "Grrr..."

    mc "Uh-oh."

    "You're about to take out an arrow... When someone grabs you by the shoulder and pulls you to the right!"

    mc "Aaahh..."

    "You're being shoved, before the figure steps out and finishes the zombie who was in front of you."

    zombie "Arrgghh..."

    "After a while, the figure comes back. You can't quite see his face completely due to poor lighting."

    placeholder "There, you can go now!"

    "He shoves you out, you look back to where he hides."

    mc "Okay, I appreciate whatever that was... But who are you?"

    placeholder "None of your business, that's who."

    mc "Excuse me?"

    placeholder "You wanna start something? Leave me alone [persistent.pronouns['child']]!"

    mc "No."

    placeholder "What do you mean no?!"

    mc "I want to know who you are!"

    placeholder "Give me one good reason."

    menu:

        mc "Because"

        "I want to thank you.":

            placeholder "Well there ya go, you said it."

            placeholder "Now piss off!"

            mc "What is your problem with me?!"

            placeholder "Ask yourself that damn question. All I want is to be left alone, is that too much to ask?"

            mc "You think I don't know? You're stalking me in this alley and secretly playing hero."

        "I want to know if you're friendly.":
            
            placeholder "Wasn't saving your ass friendly enough to you?"

            mc "Oh great! You're {i}certainly{/i} showing me your friendliness by stalking me in this alley."
        
        "I don't need a knight in shining armor!":

            placeholder "Whoever says anything about being {i}your{/i} hero?"

            mc "Then you are a stalker. And I have to know why you're stalking me!"

    placeholder "What did you just call me?"

    placeholder "I'm not a stalker, why would I be stalking you anyway?"

    mc "If that were the case then you shouldn't have a problem revealing yourself."

    placeholder "Trust me. You {i}don't{/i} want to see my face."

    mc "I've had it with your secrecy!"

    "You take out an arrow and take aim."

    mc "I can take care of my own damn self. If you don't want to show me your face then you are a creeper. And that means you are my enemy."
    
    mc "So I'll say this again, show me your face before I {color=#FF0000}{b}fire this arrow through your skull.{/b}{/color}"

    $ renpy.pause(1.0)

    placeholder "...Heh heh heh. Really?"
    
    placeholder "Very well, don't tell me I didn't warn you!"

    "The air suddenly feels cold. You can see his hands coming out from the alley, gripping the wall..."
    
    "...Followed by four more arms, two at the top and two at the bottom. You take a step closer and realize..."
    
    "They're not arms."
    
    $ renpy.pause(1.0)

    "They're tentacles."

    placeholder "RRRAGGGGHHHHHH!!!"

    mc "AAAHHHH..."

    "Startled, you drop your bow and arrows."
    
    "It was the scariest thing you've ever seen, his flesh is rotten, his skeleton can be seen on his right head, gross saliva dripping from his mouth..."
    
    "Also, four tentacles stretch from behind his back!"

    mc "I warned you! I WARNED YOU!"

    "Too much pressure, you pass out."

    $ notify("Chapter 1 Complete", "You've finished Chapter 1. Don't forget to save!")

    $ renpy.pause(1.0)
    
    return