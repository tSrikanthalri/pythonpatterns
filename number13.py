rows = int(input())

spaces = rows//2
stars = 1 

for row in range(1,rows+1):
    
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    dummy = 1
    for st in range(1,stars+1):
        print(dummy,end=" ")
        if st <= stars//2:
            dummy += 1
        else:
            dummy -= 1
    print()
    if row <= rows//2:
        spaces -= 1 
        stars += 2 
    else:
        spaces += 1 
        stars -= 2 
