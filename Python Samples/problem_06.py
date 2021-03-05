def prime(n):
    if n>1:
        for i in range(2,num):
            if num%i == 0:
                return 0
        else:
            return 1

    else:
        return 0


num = int(input('Enter a number: '))

if  prime(num)==1:
    print("It's a prime number")
else:
    print("It's not a prime number")
