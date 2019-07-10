def evens(int1, int2):
    
    x = int1
    y = int2 - 1
    while x < y:
        
        x += 1
        
        if (x%2) == 0:
            print (x)
        


def reverse_evens(int1, int2):
    
    x = int1 + 1
    y = int2
    while x < y:
        
        y -= 1
        
        if (y%2) == 0:
            print (y)
            
    
            