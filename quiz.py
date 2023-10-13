print('Welcome To Quiz Game')

player=input('Do you want to  play?')

if player.lower() != "yes":
    quit()
print('Ok lets play')
score = 0   

question = input("Python Designed By?")
if question.lower() == "guido van rossum":
    print('Correct')
    score += 1
else:
    print('Incorrect') 

question = input("Which Key Can Be Used in Overloading?")
if question.lower() == "operator key":
    print('Correct')
    score += 1
else:
    print('Incorrect') 

question = input("PEP stands for in Python?")
if question.lower() == "python enhancement proposal":
    print('Correct')
    score += 1
else:
    print('Incorrect')     

question = input("What keyword is used in Python to raise exceptions?")
if question.lower() == "raise key":
    print('Correct')
    score += 1
else:
    print('Incorrect')    

question = input("OOPS full form?")
if question.lower() == "object oriented programming system":
    print('Correct')
    score += 1
else:
    print('Incorrect')

print("Your Score"+ str(score))    

if score ==5:
    print('Congratulations Your Passed Level1')
else:
    print('Sorry try again sometime level failed')    