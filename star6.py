rows = int(input())
spaces = rows - 2
stars = 1
for row in range(1,rows-2+1):
    for sp in range(1,spaces+1):
        print(" ",end=' ')
    for st in range(1,stars+1):
        print("+",end=" ")
    print()
    spaces -= 1
    stars += 2
    
spaces = 1
stars = 2 * (rows - 3) - 1  

for row in range(rows - 3):  
    for sp in range(spaces+1):
        print(" ", end=' ')
    for st in range(stars):
        print("+", end=' ')
    print()
    spaces += 1
    stars -= 2
    
