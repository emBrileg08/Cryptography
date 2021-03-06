"""
cryptography.py
Author: emBrileg08
Credit: NA

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

choice="space filler"

while choice!= "q":
    choice=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if choice=="q":
        print("Goodbye!")
    elif choice=="e":
        message=list(input("Message: "))
        key=list(input("Key: "))
        length=len(message)
        while len(key)<length:
            key.extend(key[::])
        for x in range(0,length):
            num=associations.find(message[x])
            num2=associations.find(key[x])
            num3=num+num2
            if (num3/84)<1:
                print(associations[num3],end="")
            elif (num3%84)==0:
                print(associations[84],end="")
            else:
                remain=num3%84
                print(associations[remain-1],end="")
        print("")
    elif choice=="d":
        message=list(input("Message: "))
        key=list(input("Key: "))
        length=len(message)
        while len(key)<length:
            key.extend(key[::])
        for x in range(0,length):
            num=associations.find(message[x])
            num2=associations.find(key[x])
            num3=num-num2
            print(associations[num3],end="")
        print("")
    else:
        print("Did not understand command, try again.")
