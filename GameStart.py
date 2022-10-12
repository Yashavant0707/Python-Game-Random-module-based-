import random
l=['rock','scissor','paper']
while True:
    Computer_CounT=0
    Your_CounT=0
    Your_choice=int(input('''
Game start.....
1 Yes
2 No | Exit   
    '''))
    if Your_choice==1:
        for a in range(1,6):
            Your_Input=int(input('''
1 Rock
2 Scissor 
3 Paper          
'''))
            if Your_Input==1:
               Your_wish = "rock"
            elif Your_Input==2:
                 Your_wish="scissor"
            elif Your_Input==3:
                 Your_wish="paper"
            comp_choice=random.choice(l)
            if (comp_choice==Your_wish):
               print('computer value:-',comp_choice)
               print('your value:-',Your_wish)
               print('Game Draw')
               Your_CounT=Your_CounT+1
               Computer_CounT=Computer_CounT+1
            elif ((Your_wish=="rock" and comp_choice=="scissor") or (Your_wish=="paper" and comp_choice=="rock")
               or (Your_wish=="scissor" and  comp_choice=="paper")):
               print('computer value:-', comp_choice)
               print('your value:-', Your_wish)
               print('You win')
               Your_CounT=Your_CounT + 1
            else:
                print('computer value:-', comp_choice)
                print('your value:-', Your_wish)
                print('computer win')
                Computer_CounT=Computer_CounT + 1
        if Computer_CounT==Your_CounT:
            print("Final Game Draw...")
            print("Your score:-",Your_CounT)
            print("Computer score:-",Computer_CounT)
        elif Your_CounT>Computer_CounT:
            print("Final You won the Game ...")
            print("Your score:-", Your_CounT)
            print("Computer score:-", Computer_CounT)
        else:
            print("Final Computer won the  Game ...")
            print("Your score:-", Your_CounT)
            print("Computer score:-", Computer_CounT)

    else:
        break  