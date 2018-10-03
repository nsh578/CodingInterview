#Is Unique
#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?

#Questions:
#Is the string ASCII or Unicode?
#What would the return type be? Boolean?
#Can there be null or invalid inputs?

#Sol 1: ASCII: 128 chars. make list of boolean
#Extended ASCII is 1=256

##def isUnique(string):
##    if len(string) > 128:
##        return False
##    boollist = [False]*128
##    for i in string:
##        temp = ord(i)
##        if boollist[temp] == False:
##            boollist[temp] = True
##        else:
##            return False
##
##    return True


#Sol 2: use set

##def isUnique(string):
##    check = set()
##    for i in string:
##        if i not in check:
##            check.add(i)
##        else:
##            return False
##
##    return True



#Sol 3: Iterate string twice -> does not require additional data structure

##def isUnique(string):
##    for i in range(len(string)):
##        for j in range(i+1, len(string)):
##            if string[i] == string[j]:
##                return False
##    return True


#ADDITIONS:
#Sol 1: can reduce space usage by using bit vector if only alphabets are used
#Another way to x use additional data structure is to sort with
#in-place sorting and compare neighboring elements.

