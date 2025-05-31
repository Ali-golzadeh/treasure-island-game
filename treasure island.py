print ('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
       
       ''')
print("welcome to treasure island, your mission is to find a treasure")
direction_1=input("left or right?")
if direction_1 == "left" :
    q1=(input("do you want swimm or wait? "))
    if q1=="wait" :
        q2=input("which door do you choose?red,blue or yellow? ")
        
        if q2 == "red" :
         print("Burned by fire.Game Over.")
        elif q2=="blue" :
            print("Eaten by beasts. Game Over.")
        elif q2=="yellow" :
            print("You Win!")
        else :
            print("Game Over")
    else : 
        print("Attacked by trout , Game Over")
else : 
    print("GAME OVER!!!")