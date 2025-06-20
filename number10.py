rows = int(input('enter the : '))

for row in range(1,rows+1):
    dummy = row

    for col in range(1,row+1):
        print(dummy,end=" ")

        dummy += row
    print()
