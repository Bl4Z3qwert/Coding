def match_word(words):
    ctr=0
    lst =[]
    for word in words:
        if len(word) >1 and word[0]==word[-1]:
            ctr +=1
            lst.append(word)
    print('word with last& first letter same\n', lst)    
    return ctr
count= match_word(['abvabagaba', 'ffd', 'sfdfs', 'ggdffg', '1323231'])    
print('number of words  with same characters')
