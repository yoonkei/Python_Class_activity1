import easygui

name = easygui.enterbox("Write your name.")

import random
time = 3
human_s = []


easygui.buttonbox("Play rolling a dice.",
                                  choices = ['roll'])
for i in range(2):
    human = random.randint(1, 6)
    time = time - 1
    easygui.msgbox("You got {} \n {} times left.".format(human, time))
    human_s.append(human)

human = random.randint(1, 6)
easygui.msgbox("You got {} \n No more chance...".format(human))
human_s.append(human)

human_score = sum(human_s)
computer_score = random.randint(3, 18)

if int(human_score) > int(computer_score):
    easygui.msgbox("{}'s Final Score : {} \n Computer score : {} \n You Win ^^".format(name, human_score, computer_score))
else:
    easygui.msgbox("{}'s Final Score : {} \n Computer score : {} \n You Lose T^T".format(name, human_score, computer_score))
