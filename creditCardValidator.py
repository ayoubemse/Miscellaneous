import math

def validateCreditCardNumber(credtCardNumber):
    
    numberLength = int(math.log10(credtCardNumber)) + 1
    
    checkSum = 0
    for num in range(0, numberLength, 2):
        doubledEvenNumber = int(str(credtCardNumber)[num]) * 2
        oddNum = int(str(credtCardNumber)[num+1])
        if (len(str(doubledEvenNumber))> 1):
            doubledEvenNumber = doubledEvenNumber // 10 + doubledEvenNumber % 10
        
        checkSum += doubledEvenNumber + oddNum
    
    if checkSum % 10:
        print("invalid card number !!")
    else:
        print("this credit card is valid :)")


validateCreditCardNumber(4778232130395307)
