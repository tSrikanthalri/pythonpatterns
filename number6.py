rows = int(input('enter : '))

for row in range(1,rows+1):
    dummy = row
    for col in range(1,rows+1):
        print(dummy,end=" ")

        dummy += 1
    print()


    
