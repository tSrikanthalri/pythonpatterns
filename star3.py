rows = int(input())


stars = rows

for row in range(1,rows+1):
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars -= 1 
    
