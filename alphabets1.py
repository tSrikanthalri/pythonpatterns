rows = int(input())

dummy = 1

for row in range(1,rows+1):

    for col in range(1,rows+1):
        print(chr(64+dummy),end=" ")

        dummy += 1
    print()
