
n = int(input("Enter a number"))

lon = [1000, 500, 200, 100, 50, 20 ,10 ]

for i in (lon) :

    non = n // i

    n %= 1

    if non != 0 :

        print("the n.o of note of " , i , "is" , non)
