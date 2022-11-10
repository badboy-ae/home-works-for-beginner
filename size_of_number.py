big = None
mid = None
lit = None

print("hello world  \nlets start game")


x = float(input("enter first : "))
y = float(input("enter secend : "))
z = float(input("enter third : "))

if x >= y and x >= z and y >= z:
    big = x 
    mid = y
    lit = z
    
elif y >= x and y >= z and x >= z :
    big = y
    mid = x 
    lit = z
    
elif x >= y :
    big = z
    mid = x
    lit = y
    
else :
    big = z
    mid = y
    lit = x

print("bigest = {} \nmidest = {} \nlittlest = {}".format(big,mid,lit))



