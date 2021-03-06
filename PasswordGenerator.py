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
        [password.append(charList[random.randint(0, len(charList)-1)]) for i in range(totalNum - (numNum + symbolNum))]
        
        #numbers
        [password.append(numList[random.randint(0, len(numList)-1)]) for i in range(numNum)]
        
        #symbols
        [password.append(symbolList[random.randint(0, len(symbolList)-1)]) for i in range(symbolNum)]

        random.shuffle(password)  #randomize/shuffle the list elements
        #convert password list to string and concat
        password = ''.join(password)
        print("Your password is: " + password)

        store = input("Would you like to store the password?(Y/N)  ")
        if (store.lower().__contains__("y")):
            site = input("Enter the name of website or app that you want to use the password for: ")
            try:
                with open("passwords.txt", "a") as f:  #open in append mode
                    f.write(site + ": " + password+"\n")
                    print("added to passwords.txt successfully")
            except:
                print("Unable to write to file")
                    
    
if __name__ == "__main__":
    generate()