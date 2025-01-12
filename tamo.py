#  print ('table2')
#  num = 2
#  for i in range(1,31):
#      result =num * i
#     print('17 x %d=%d' %(i,result)) 

num = int(input('pls enter number to check if it is prime or not'))
flag = False
if num>1 :
   for i in range(2,num):
       if num %i ==0:
           flag=True
           break
if flag:
    print(num,' is not a prine number')
else:
    print(num,' its a prime number')       
           