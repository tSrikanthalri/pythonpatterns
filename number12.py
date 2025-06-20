rows = int(input())

spaces = rows//2
stars = 1 

for row in range(1,rows+1):
    
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    dummy = row
    for st in range(1,stars+1):
        print(dummy,end=" ")
        if st <= stars//2:
            dummy += row
        else:
            dummy -= row
    print()
    if row <= rows//2:
        spaces -= 1 
        stars += 2 
    else:
        spaces += 1 
        stars -= 2 
        
