number = int(input("Enter a number: "))
l = len(bin(number)[2:])

for i in range(1, number+1):
    print(str(i).rjust(l , ' ') , oct(i)[2:].rjust(l , ' ') , hex(i)[2:].upper().rjust(l , ' ') , bin(i)[2:].rjust(l ,' '))
