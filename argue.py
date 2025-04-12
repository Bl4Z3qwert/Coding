def total(bill,tip):
    balance = bill*(1+0.01*tip)
    balance = round(balance,2)
    print('you have to pay ',balance)
total(180,20)
                    
    
   