# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
import re
print(art.logo)
auc={}
def add_bid(name,bid):
    auc[name]=bid

def find_winner(auc):
    winner=""
    for i in auc:
        for j in auc:
            if auc[i]>auc[j]:
                winner=i
    try:
        print(f"The winner is {winner} with a bid of ${auc[winner]}")
    except KeyError as ke:
        print("No bids were made")


should_continue=False
while should_continue!=True:
    
    try:
        name=input("What is your name? ")
        # print(re.sub("^/\d/g$","",name))
        bid=int(input("What is your bid? $"))
        add_bid(name,bid)
        yes_or_no=input("Are there any other bidders? Type 'yes' or 'no'. ")
        if yes_or_no.lower()=="no":
            should_continue=True
            # print(auc)
            find_winner(auc)
        elif yes_or_no.lower()=="yes":
            print("\n"*100)
            should_continue=False
    except ValueError as ve:
        print("Please enter a valid number")
        continue

