def asterisk():
    
    for i in range(1, 5):
        print ('****')
        
        
def asterisk2():
    x = 0
    y = 4
    
    while x < y: 
        x += 1
        print ('*'*x)
    
    # Reversing loop
    x = 0
    while x < y:
        y -= 1
        print ('*'*y)
        
def containsLetter(string, target): #Returns true if there's letter a in string
    letters = list(string)
    length = len(letters)
    
    index = 0
    status = False
    
    while index < length:
        if letters[index] == target:
            status = True
        index += 1
        
    return status


def containsSM(string):
    
    if containsLetter(string, 's') and containsLetter(string, 'm'):
        return True
    else:
        return False

