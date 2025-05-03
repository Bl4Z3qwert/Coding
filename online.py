# def match_word(words):
#     ctr=0
#     lst =[]
#     for word in words:
#         if len(word) >1 and word[0]==word[-1]:
#             ctr +=1
#             lst.append(word)
#     print('word with last& first letter same\n', lst)    
#     return ctr
# count= match_word(['abvabagaba', 'ffd', 'sfdfs', 'ggdffg', '1323231'])    
# print('number of words  with same characters')

weather =(1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,1,0)
sun = 0
rain = 0
for i in range(0,18):
    if (weather[i] == 0):
        rain+=1
        print('The number of zeros that appeared is ',rain)
    else:
        sun+=1
        print('The number of zeros that appeared is ',sun)
if (sun > rain):
    print('the weather is good you can go outside')
else:
    print('stay indoors the weatheris bad')            
