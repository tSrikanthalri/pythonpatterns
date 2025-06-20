rows = int(input('enter : '))

numbers = rows
for row in range(1,rows+1):

   for col in range(1,numbers+1):
        print(row,end=" ")

   numbers -= 1
   print()
        

        
