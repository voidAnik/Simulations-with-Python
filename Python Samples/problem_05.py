def area_tri(a,b,c):
    t=(a+b+c)/2
    return (t*(t-a)*(t-b)*(t-c)) ** 0.5

a=int(input('Enter 1st side:'))
b=int(input('Enter 2nd side:'))
c=int(input('Enter 3rd side:'))
print("Area of the triangle is = ",area_tri(a,b,c))