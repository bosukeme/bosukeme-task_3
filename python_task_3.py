#python task 3. author @bosukeme

import random
game_level=input("select a level: ").lower()

#difficulties 
easy_level=random.randint(1,10)
medium_level=random.randint(1,20)
hard_level=random.randint(1,50)
chances=0

#################################################
#EASY LEVEL
try:
    if game_level=="easy":
        while chances<6:
            user_guess= int(input("Guess a number: "))
            if user_guess==easy_level:
                print('Correct. You got it right')
                chances+=1
                break
                
            else:
                print('That was Wrong. Try again')
                print("You have", 6-chances-1, "chances left")
                chances+=1


        if not chances<6:
            print()
            print("the number is", easy_level)
            print("You took", chances, "chance(s)")
            print("GAME OVER")
except:
    print("Wrong imput. Run the program again")
        
#######################################################
#MEDIUM LEVEL        
try:
    if game_level=="medium":
        while chances<4:
            user_guess= int(input("Guess a number: "))
            if user_guess==medium_level:
                print('Correct. You got it right')
                chances+=1
                break
            else:
                print('That was Wrong. Try again')
                print("You have", 4-chances-1, "chances left")
            chances+=1


        if not chances<4:
            print()
            print("the number is", medium_level)
            print("You took", chances, "chance(s)")
            print("GAME OVER")
except:
    print("Wrong imput. Run the program again")
    
############################################################## 
#HARD LEVL
try:
    if game_level=="hard":
        while chances<3:
            user_guess= int(input("Guess a number: "))
            if user_guess==hard_level:
                print('Correct. You got it right')
                chances+=1
                break
            else:
                print('That was Wrong. Try again')
                print("You have", 3-chances-1, "chances left")
            chances+=1



        if not chances<3:
            print()
            print("the number is", hard_level)
            print("You took", chances, "chance(s)")
            print("GAME OVER")

except:
    print("Wrong imput. Run the program again")


