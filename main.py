#Rishabh Shah
#2016
#Find three in a row

#two arrays to work with
a = [1,1,2,3,4]
b = [3,4,4,4,5]
listToTest = b

#dummy variable
c = listToTest[0]

#counter
d = 1

#create for loop with the upper bound being the length of the list
for i in range(1, len(listToTest)):
    #if the previous value is the same as the next value
    if c == listToTest[i]:
        #increase the counter by 1
        d += 1
    #if the counter hits 3, exit the loop
    elif d == 3:
        break
    #if the previous value is not the same set the new value to c to test the next value
    elif c != listToTest[i]:
        c = listToTest[i]

#if the counter is greater than or eqaul to three then print out the statement with the value
if d >= 3:
    print("There are three in a row and the value is " + str(c) + ".")
#if not, then print out this new statement
else:
    print("There are not three in a row.")