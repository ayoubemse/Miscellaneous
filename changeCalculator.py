import math

def changeCalculator(cost, money):
    
    numOfQuarters = 0
    numOfDimes = 0
    numOfNickels = 0
    numOfPennies = 0
    
    change = money - cost
    change_coins = {}

    if change < 0:
        print("money paid can't be less than the cost !")
    
    elif change == 0:
        print("no change is due")

    else:
        numOfQuarters = math.floor(change/0.25)
        change_coins["quarters"] = numOfQuarters
        change = round(change - numOfQuarters * 0.25, 3)
        
        numOfDimes = math.floor(change/0.1)
        change_coins["dimes"] = numOfDimes
        change = round(change - numOfDimes * 0.1, 3)
        
        numOfNickels = math.floor(change/0.05)
        change_coins["nickels"] = numOfNickels
        change = round(change - numOfNickels * 0.05, 3)
        
        numOfPennies = math.floor(change/0.01)
        change_coins["pennies"] = numOfPennies
        change = round(change - numOfPennies * 0.01, 3)

        assert(change==0)
        
        assert(round(numOfPennies * 0.01 + numOfNickels*0.05 + numOfDimes*0.1 + numOfQuarters*0.25, 3) == round(money - cost, 3))

        print("due change is : ", end = " \n")
        for coins, amount in change_coins.items():
            if (amount):
                print(f"{amount} {coins} ", end = " \n")

changeCalculator(1.2, 5.69)