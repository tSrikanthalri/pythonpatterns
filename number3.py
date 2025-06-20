rows = int(input())

dummy = 1
for row in range(1,rows+1):
    
    for col in range(1,rows+1):
        print(dummy,end=" ")

        dummy += 1
    print()
        
