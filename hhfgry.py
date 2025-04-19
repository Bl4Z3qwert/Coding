try:
    num1 = eval(input('enter your age :'))
    result= num1
    print('result is', result)
except ValueError:
    print('only numbers')
# except SyntaxError:
#     print('comma is missing. Enter numbers seperated by comma like this 3,4,5')
except:
    print('wrong input')
else:
    print('no exceptions')
finally:
    print('congratulations you did great work')                
# try:
#     nun = int(input('please enter the number '))
#     if nun%2==0:
#         print('number is even')
#     else:
#         print('number is uneven or odd')   
# except :
#     print('invalid input')                 