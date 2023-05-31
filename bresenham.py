from fractions import Fraction

x1 = -7
y1 = -5

x2 = -2
y2 = -2

m = Fraction(3/5)
e = 1

for i in range(1,6):    
        
    while(e > 0):
        
        print('e ->', e)
        print('({},{})'.format(x1,y1))
        print('==============')
        y1 += 1
        e -= 1
        

    print('({},{})'.format(x1,y1))
    print('e -> ', e)
    print('==============')
    x1 += 1 
    e += m
    
    
    print('({},{})'.format(x1,y1))
    print('e -> ', e)
    print('==============')
        
