# num = [1,2,3,4,7,8,9,]
# even=[x for x in num if x % 2 ==0]
# print('list of even numbers : ', even)
# 
# 
# 



#List comprehension

# def square(n):
#     return n *n
# nmber= (1,2,3,4,5,6,7,8,3,5,4,6,7)
# result=map(square,nmber)

# print(list(result))


# zip function

name = ('sfsdf','sfsfsfd','fdghfghfgh')
grade =('a','S', 'd')
mapped=zip(name,grade)

print(list(mapped))

#exit

ages =[19,37,62,45,6,78,7]
for age in ages:
    if age < 18:
        print('u cant vote')
        print (exit)
        exit()
    else :
        print('you can vote')
        
  