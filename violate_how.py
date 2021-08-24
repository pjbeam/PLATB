import random

stories_beginning = ["I was at Wendy's doing my due diligence when I overheard a conversation.", "I was smoking weed behind my church last Sunday when I hear sobbing.",
                     "I dreamed I had an abortion. It was only a dream but someone has to think of the unborn who are figments of our subconscious.",
                     "There was a loud sound and the shrubbery in my front yard caught fire. I was startled by a loud, booming voice.",
                     "Hooligans vandalized my shop with a hateful quote. A bystander came over and we started talking.",
                     "While at church I fell into a trance and started prophecying.",
                     "My pastor lit a cigarette after we got done having sex.",
                     "I was praying to an image of Governor Abbott, hoping to get his absolution for my sins. He required me to send this as a penance.",
                     "My wife broke down one night, sobbing. She said she had to tell me something from her past.",
                     "My son's preschool teacher confided in me her darkest secret. I felt compelled to send in this information as a result.",
                     "The clerk at my local bank was talking on the phone while she handled my deposit slip. This is what she said."]

stories_middle = ["She told me that she had gotten knocked up, you know what that means, and that she didn't know what to do.",
                  "Apparently there was an ad on the bench outside the bus stop for a doctor not but a few hours away who could help this woman I know with her 'problem'.",
                  "I knew what I had done was wrong, the child of my rapist had every right to live and flourish but I couldn't face down that horror every day.",
                  "They told me the baby's heart was beating, 140 beats per minute. That seemed to fast and I was already depressed.",
                  "Sir, this is a Wendy's, cried Jesus in my dream. He was lamenting what my wife's boyfriend's sister had done.",
                  "She talked very fast, I could hardly understand what she was saying. But I knew, God told me, that she had done something terrible.",
                  "She told me that he made her do it, he could only get off on live she snuffed out through the services of evil coastal abortionists.",
                  "It was her own father's child she had carried, she sobbed. She didn't know it was wrong at the time but the reaction of her friends got her thinking.",
                  "Men had broken into her house carrying pipe wrenches and evolution textbooks. They had their way with her for hours, she didn't know who the father was.",
                  "She had only done one 'video', if you know what I mean. She didn't think she could get pregnant if it happened on camera. The 'actor' said sperm get camera-shy.",
                  "Apparently she had had relations with a horse as well as the stable boy. So she didn't know if she was carrying a human child or a centaur."]

stories_end = ["So she went to this doctor and had the abomination cleansed.",
               "After a great deal of prayer, nothing happened. So she went down to Houston to 'take care of it', so to speak.",
               "It was the mayor's child, of course. Nothing could stop his reelection, so she did what she had to do and the baby was no more.",
               "For the ninth and most recent time, she aborted her sweet, perfect unborn child like the monster she is.",
               "How many times did I tell her condoms were cheaper? But no, she didn't listen. And another unborn baby died.",
               "Then, of course, she ended the pregnancy with the help of that godless abortionist.",
               "She aborted the child.",
               "Then the baby was no more.",
               "And, I'm cryin' while I write this, that little heartbeat stopped. Please save us from these monsters!",
               "Sadly, no amount of convincing could stop her. That doctor had gotten in her head. Now it's too late.",
               "When she came back from her 'trip', I could tell she wasn't with child no more."]


def get_violate_how():
    return random.choice(stories_beginning) + " " + random.choice(stories_middle) + " " + random.choice(stories_end)
