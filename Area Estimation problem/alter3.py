# y1=2x and y2=8-2x for 0 to 4
import math
import random
random.seed(0)
n=500,1000,5000,10000

a=0
b=2
c=4

for i in n:

  f_sum1=0 #y=2x for 0 to 2
  f_sum2=0 #y=8-2x for 2 to 4
  f_sqr1=0 #y=2x for 0 to 2
  f_sqr2=0 #y=8-2x for 2 to 4

  for j in range(i):

    x1=random.uniform(b,a) #y=2x for 0 to 2
    x2=random.uniform(c,b) #y=8-2x for 2 to 4

    func1=2*x1 #y=2x for 0 to 2
    func2=8-(2*x2) #y=8-2x for 2 to 4

    f_sum1+=func1
    f_sum2+=func2

    f_sqr1+=func1**2 #y=2x for 0 to 2
    f_sqr2+=func2**2 #y=8-2x for 2 to

  f_avg1=f_sum1/i #y=2x for 0 to 2
  f_avg2=f_sum2/i #y=8-2x for 2 to 4

  f_sqravg1=f_sqr1/i
  f_sqravg2=f_sqr2/i

  integral1=(b-a)*f_avg1 #y=2x for 0 to 2
  integral2=(c-b)*f_avg2 #y=8-2x for 2 to 4

  total_integral=integral1+integral2

  error1=((b-a)/math.sqrt(int(i)))*math.sqrt(f_sqravg1-(f_avg1**2)) #y=2x for 0 to 2
  error2=((c-b)/math.sqrt(int(i)))*math.sqrt(f_sqravg2-(f_avg2**2)) #y=8-2x for 2 to 4

  error=error1*error2 #multiply hobe idk why

  print("\n Trial: ",i, "\tIntegral: ",total_integral, "\tError: ", error)

