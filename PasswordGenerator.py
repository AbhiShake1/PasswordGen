import random

def generate():
    charSmall = "abcdefghijklmnopqrstuvwxyz"

    charList = list(charSmall + charSmall.upper())  #string list with all capital and small chars
    numList = list("1234567890") #string list with all numbers
    symbolList = list("!@#$%^&*()_+?><,.:;'")  #string list with some symbols

    msg = "(Please enter length in number): "
    totalNum = int(input("How long would you like your password to be?" + msg))

    if (totalNum < 8):
        print("A strong password must always contain more than 8 characters. Please re-consider the length")
        generate() #restart
    else:
        numNum = int(input("How many numbers would you like in your password?"+msg))
        symbolNum = int(input("How many symbols would you like in your password?"+msg))

        password = []

        #chars
        for i in range(totalNum - (numNum + symbolNum)):
            charIndex = random.randint(0,len(charList))
            password.append(charList[charIndex])

        #nums
        for i in range(numNum):
            charIndex = random.randint(0, numNum)
            password.append(numList[charIndex])

        #symbols
        for i in range(symbolNum):
            charIndex = random.randint(0, symbolNum)
            password.append(symbolList[charIndex])

        random.shuffle(password)  #randomize/shuffle the list elements
        #convert password list to string and concat
        print("Your password is: " + ''.join(password))
    
if __name__ == "__main__":
    generate()