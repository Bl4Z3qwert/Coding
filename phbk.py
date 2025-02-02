import sys
def initial_phonebook():
    rows,cols=int(input('Please enter initial number of contacts:')),5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print('\nEnter contact %d details in the following order (ONLY):'%(1 + 1))
        print('Note: *indicate mandatory field')
        print('***********************************************************************************************************************')
        temp=[]
        for j in range(cols):
            if j ==0:
                temp.append(str(input('Enter name;')))
                if temp[j] == '' or temp[j]=='':
                    sys.exit('Name is a mandatory field')
            if j ==1:
                temp.append(int(input('Enter number;')))
                if temp[j] == '' or temp[j]=='':
                    sys.exit('Number is a mandatory field')
            if j ==2:
                temp.append(str(input('Enter email;')))
                if temp[j] == '' or temp[j]=='':
                    sys.exit('Email is a mandatory field')
            if j ==3:
                temp.append(str(input('Enter DoB;')))
                if temp[j] == '' or temp[j]=='':
                    sys.exit('DoB is a mandatory field')
            if j ==4:
                temp.append(str(input('Enter category(family friends,colleagues);')))
                temp[j] =None
        phone_book.append(temp) 
    print (phone_book )   
    return phone_book 
x =initial_phonebook()
print(x)           
             