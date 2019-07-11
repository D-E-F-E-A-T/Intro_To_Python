def evens(numbers):
    total = 0
    for number in numbers:
        if (number % 2) == 0:
            total += number
    return total


def get_age():
    user_age = int(input("Please enter your age "))
    
    if user_age < 25:
        print ("You're still a kid")
    else:
        print ("You're getting old, man")
        
        
def age_calculator(yob):
    age = 2019 - yob
    return "You're " + str(age) + " years old"

def leapyear(yob):
    if (yob % 4) == 0:
        print (str(yob) + " is a leap year")
    else:
        print (str(yob) + " is not aleap year")
        