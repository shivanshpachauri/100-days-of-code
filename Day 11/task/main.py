import art
print(art.logo)

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_list=[]
computer_list=[]
my_sum=0
computer_sum=0
should_stop=False

my_number1=random.choice(cards)
my_number2=random.choice(cards)
computer_first=random.choice(cards)
computer_second=random.choice(cards)
computer_list.append(computer_first)
computer_list.append(computer_second)
my_list.append(my_number1)
my_list.append(my_number2)
while not should_stop and my_sum <= 21:
    user_input=input("Do you want to play a game of black y for yes n for no\n").lower()
    if user_input=='y':
        
        my_sum=sum(my_list)
        computer_sum=sum(computer_list)
        print("Your cards : ",my_list," current_score: ",my_sum)
        print("Computer first card : ",computer_first)
        my_number3=random.choice(cards)
        my_list.append(my_number3)
        my_sum = sum(my_list)
        if my_sum > 21:
            print("Your final hand : ",my_list,"final score : ",my_sum)
            print("computer final hand: ",computer_list,"computer_score",computer_sum)
            if(computer_sum>my_sum):
                print("You lose")
            elif(my_sum>computer_sum):
                print("You won")
            elif(my_sum==computer_sum):
                print("draw")
            should_stop = True
        else:
            computer_third=random.choice(cards)
            computer_list.append(computer_third)
            computer_sum = sum(computer_list)
            if computer_sum > 21:
                
                print("Your final hand : ",my_list,"final score : ",my_sum)
                print("computer final hand: ",computer_list,"computer_score",computer_sum)
                if(computer_sum>my_sum):
                    print("You lose")
                elif(my_sum>computer_sum):
                    print("You won")
                elif(my_sum==computer_sum):
                    print("draw")
                should_stop = True
    elif user_input=='n':
        should_stop=True
        print("Your final hand : ",my_list,"final score : ",my_sum)
        print("computer final hand: ",computer_list,"computer_score",computer_sum)
        if(computer_sum>my_sum):
            print("You lose")
        elif(my_sum>computer_sum):
            print("You won")
        elif(my_sum==computer_sum):
            print("draw")
        