rows = int(input('enter : '))

spaces = rows - 1
numbers = 1
for row in range(1,rows+1):

   for spaces in range(1,spaces+1):
       print(" ",end=" ")
   for col in range(1,numbers+1):
       print(str(row),end=" ")
   spaces -=1
   numbers += 1
   print()
