
def paren(s,l,r,p,n) :

    if (p == 2*n) :

        for ss in s :

            print(ss ,  end=" ")
        print("\n")
        return
    
    # if left is grater we print right

    if l > r :
        s[p] = "}"
        paren(s,l,r+1,p+1,n)

    if l < n :
        s[p] = "{"
        paren(s,l+1,r,p + 1 , n)

n = int(input("Enter a n.o"))
s = [" "] * 2 * n
print("\n")
paren(s,0,0,0,n) 
