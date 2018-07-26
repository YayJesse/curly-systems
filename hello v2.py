#This program says hello and asks for my name.

print('Hello world! Welcome to my very first python script!')
print('What is your name?') #asks for name
myName = input()
print('It is good to meet you, ' + myName)
print('What is your age? (If you dont mind me asking of course!)')  #asks for age
myAge = input()
print("What! I swear you look like you don't look a day over " , str(int(myAge)-2) , "!")
print("So, " , myName , "is your refrigerator running?")
print("Type Y for yes, or N for no")
myRspnse = input()  #Yes or no call
if myRspnse == 'Y':
    print("Well why don't you go run after it! Hahahaha")
else:
    print('Well go get it fixed!')

print("This doesn't seem like", myName, "typing. What's", myName, "'s secret password?")
userPassEntry = input()
if userPassEntry == 'purplemonkeydishwasher':
    print('Access Granted!')
else:
    print("You're not " , myName , "frig off outta here!")
print("################")
print("################")
print("################")
print("###LOADING 99%#.")
print("----------------")
print("You are now connected to the super secret useful network")
print("Enter at your own risk.")
