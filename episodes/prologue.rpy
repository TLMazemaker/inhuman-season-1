default gun = False
label prologue:

    "⚠️Warning! This story contains depictions of violence, gore, and a relationship between a human and something Inhuman. Viewer discretion is advised.⚠️"

    "Prologue: How it All Started"

    "Planet: Earth.\n100 years ago..."

    "{i}Now Playing as Dr. Megan.{/i}"

    show bg lab
    with fade

    "You're in a laboratory doing an illegal experiment with your mentor... Professor Tondor."
    
    char1 "How is it going Prof.?"

    char2 "The experiment is working perfectly. After all these years of hard work... we can finally reap the fruit."

    menu:
        
        char1 "Does this mean..."

        "We can finally tell the government?":
            
            char2 "What? No! Absolutely not!"

            char1 "But why? I thought--"

            char2 "You'd think the governments would thank us if we told them about this?"

            char2 "What will happen is we will be thrown into a penitentiary while THEY use this for their own ambition!"

            char1 "Oh."

        "We will finally be rich?":
            
            char2 "I won't say rich actually..."

            char2 "More like, powerful."

            char2 "Imagine this, the revolution is born... Through us!"

    "Professor Tondor walks towards the experiment table once again."

    "Taking 2 empty intramuscular injections in his hand, he then began placing them both on a strange device."

    "Strange chemicals can be seen inside a transparent tube on top of the machine."

    char2 "For years they have underestimated us... For years we've been mocked..."

    char2 "But now, it all ends here!"

    char2 "I couldn't be more proud of you, Megan."

    char1 "Me too, sir."

    "Tondor grabs a hamster from a cage, and slowly positions it in front of the first injection needle."

    "He keeps the hamster steady by strapping it on a small handmade chair."

    char1 "Sir... Are you sure about this? What if the experiment was a total miscalculation?"

    char2 "I believe in science Megan... More than my own faith. This hypothesis couldn't be more true to reality itself."

    char2 "Then again... If I {i}am{/i} wrong, you know what to do."

    "He nods toward a glass cabinet, a gun is visible resting from the inside."

    char1 "{i}Gulp.{/i}"

    "Prof. Tondor sits on a chair next to the hamster, in front of the other empty needle."

    menu:

        char1 "Sir, now that we're doing this..."

        "What should I do?":

            char2 "What you always do, Megan. You start the procedure, and watch as I do what God cannot."

            char1 "And then?"

            char2 "And then… I will do the same to you, and together…"

            char2 "We'll defy reality as the conquerors of Science."

            char1 "I see."

        "Anything I should be aware of?":

            char1 "Like what's the first reaction that should happen in this procedure?"

            "Tondor falls silent for a bit… His expression is unreadable."

            char2 "It's still rather fuzzy I must say."

            char2 "But that's really what {i}every{/i} experiment is all about."

            char2 "We can't know what the results are if we don't try. We can only guess by the hypothesis that existed."

            char1 "Well {i}that's{/i} reassuring"

    char2 "You may begin, Megan."

    char2 "Let the revolution... Be true! Let humans be able to have the ability each animal possesses..."

    char1 "Okay, starting the procedure now."

    "You press a button on the strange device, and both needles start to advance forward. In less than 10 seconds, the first needle makes its way inside the hamster's chest… Extracting its blood."

    "The blood got transferred inside the tube in the machine, mixing its contents, which then got transferred into Tondor's needle and got injected into Tondor's heart."

    char2 "Gahhh…"

    char2 "AGGGHHHHHH…"

    char1 "Professor!"

    "Tondor trashes on his chair, just as the last liquid made it inside his body, he fell to the floor, unresponsive."

    char1 "Professor... Please say something!"

    "It doesn't take long before you realize brown and white hairs started growing from his skin. Claws start to replace his fingernails."

    char1 "My God..."

    "You look back at the hamster, who also fell unconscious, but is still okay. Your mentor on the other hand..."

    char3 "..."

    "Nervous, you make your way towards the cabinet."

    char3 "M-M-Megan..."

    "Tondor reaches a hand out."

    char1 "(Is... Is this normal? Does the experiment work? Or was it all a fluke?)"

    char1 "(Is this experiment a total failure and... He is no longer a human?)"

    menu:

        char1 "(I should...)"

        "Shoot him!":

            $gun = True
            
            "Not taking any risk, you open the glass cabinet... Professor Tondor seems to hear the sound."

            char3 "No..."

            char3 "NOOOOOOO!!!!!!!"

        "Approach him!":

            "You push yourself to take a step toward your mentor..."

            char1 "...Professor Tondor?"

            char3 "Grr..."

            char3 "RRAAAGHHHHH!!!"

    "In an instant, Tondor lashes forward!"

    char1 "Gah!"

    if gun:
        
        menu:

            "Hands on the gun, you..."
        
            "Shoot!":

                pass

        "BAM! BAM! BAM! You shot 3 bullets at your mentor! 2 in his chest and 1 in his stomach."

    else:
    
        "He tackles you to the ground, his hands squeezing your neck. Cutting your air circulation."

        char1 "Ugh..."

        "Your hand searches around the floor... Looking for something to fight back! Eventually, your hand touches Tondor's fallen chair!"

        char1 "Ggghh... Take this!"

        "Filled with adrenaline, you lift the chair single handedly and smash it into your mentor's head as hard as you can!"

    char2 "Urkkk..."

    "He fell to the ground… lifeless. You look around, completely realizing that you've killed someone!"
    
    char1 "Oh God… What have I done?! I gotta get rid of the evidence!"

    "You immediately pack some things and leave the lab."

    show bg car
    with fade

    "Your forehead is filled with sweat. Hands shaking, you slowly breathe to calm your nerves as you drive the car."

    char1 "{i}It's okay... Everything's gonna be okay.{/i}"

    "At the back of the car, lies Professor Tondor's dead body... Along with a container filled with liquids from the failed experiment, and some shovels."

    "After a while, near the outskirts of town, around the public cemetery... You stop the car."

    char1 "Time to get my hands dirty."

    show bg cemetery
    with fade

    "You went out to the cemetery... Dig a hole just deep enough, and carefully lie Professor Tondor's body down before covering it back again."

    char1 "Forgive me professor... I'm a doctor, not a mortician. I can't give you a proper coffin or even a good final resting place."

    menu:

        char1 "..."

        "I hope you find peace in the afterlife.":

            char1 "Wherever you're heading next, I hope you can rest easy."

            char1 "{i}Not that it matters anyway.{/i}"
        
        "I'm sorry it had to come to this.":

            char1 "I... I didn't mean to kill you... But I gotta do what I gotta do."
        
        "I'll carry on your legacy.":

            char1 "I promise, this experiment might've failed now, but it's not over."

            char1 "I believe I can bring a much better future for humanity!"

    "You make your way back to the car... But stop for a moment, you think about the remaining liquids."

    char1 "(Hmm... Professor Tondor was mutated when he was alive. But the liquid doesn't seem to affect unliving objects.)"

    "You look around the cemetery... Completely empty with no one watching."

    char1 "(It {i}does{/i} violate the proper etiquette of science experiment, but everyone will grow suspicious once I bring this in town.)"

    "You lift the container from the truck, just when you're about to drop the contents..."

    placeholder "Hey! The hell do you think you're doing?!"

    char1 "Aaah!!!"

    "Startled, you drop the container, dropping all of the liquids into the cemetery ground."

    "You look over to the source of the voice earlier... And see a police officer! Completely witnessing your action!"

    char1 "Damn!"

    "You immediately drop the container and make a run for the car when--"

    "BAM! The officer fires..."

    char1 "Ack!"

    "You can't feel your leg, you drop down and see a paralyzing dart attached to your knee."

    char1 "No... Not like this."

    "The officer comes behind you and handcuffs your hand to your back."

    char4 "That's it madam, you have a lot of explaining to do back at the office."

    "The officer reaches for his communicator, leaving you sitting on the street behind your car... When you hear a distant noise."

    placeholder "Urkkk…"

    placeholder "Hrgg…"

    placeholder "Blarrggg…"

    "You look back at the cemetery... And realize you've just screwed up... bad."

    char1 "Oh no..."

    char4 "...Yeah I'm at the garrote street near the public--"
    
    char4 "HOLY SHIT!"

    "The officer finally realizes it too. Several hands clawed their way out from the ground."

    char4 "...Send backups quickly!"

    "He went to face the zombies... When something grabs his foot!"

    char4 "What the--"

    "Several teeth rise from the ground. The zombies are pulling the officer down. Gnashing at his leg!"

    char4 "AAAAHHHHH!!!"

    char1 "I gotta get out of here!"

    "You start to make a run for it... But can't because your leg is still paralyzed."
    
    "It doesn't take long for the zombies to go after you."

    zombie "Grr..."

    char1 "No... Please! Don't!"

    "Hopeless... You can't run... You can't fight either thanks to the handcuffed hands."
    
    "The zombies finally reach you... And begin feasting on your body."

    char1 "AHHHHH!!!!!!!!"

    "You feel every single pain as the zombies mutilate your body..."

    show bg black
    with fade
    
    "Until there's no more light you see from your eyes when the zombies chow on your head."

    $ notify("Prologue Completed", "You've completed the prologue. Don't forget to save your game.")

    menu:

        "Continue?"

        "Yes":

            "Don't forget to save your game."

            jump chapter1

        "No":

            return
