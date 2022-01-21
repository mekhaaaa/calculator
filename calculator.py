print ("for sum plz enter 1 :")
print ("for Subtraction plz enter 2 :")
print ("for multiplies plz enter 3 :")
print ("for division plz enter 4:")
print ("for average plz enter 4:")

m = int(input("plz enter num of operation"))
x = ""
sum = 0
num = None
count = 0
n = 0
####sum######
if m == 1:
    while x != "=":
        x = input("input: ")
        if x != "=":
            count + 1
            sum += int(x)

    print (sum)
#############################
if m == 2:
    while x != "=":
        x = (input("input: "))
        if x != "=":
            if num is None:
                num = int(x)
            else:
                num -= int(x)
    print(num)
###########################
if m == 3:
    while x != "=":
        x = (input("input: "))
        if x != "=":
            if num is None:
                num = int(x)
            else:
                num *= int(x)
    print(num)
############################
if m == 4:
    while x != "=":
        x = (input("input: "))
        if x != "=":
            if num is None:
                num = int(x)
            else:
                num /= int(x)
    print(num)
############################
if m == 5:
    while x != "=":
        x = (input("input: "))
        if x != "=":
            if num is None:
                num = int(x)
            else:
                count += 1
                num += int(x)
    print(num / count)
