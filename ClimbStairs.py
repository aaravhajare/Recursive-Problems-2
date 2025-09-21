
def ways(stair) :

    if stair < 0 :
        return False
    
    elif stair == 0:
        return 1
    
    onestep = 0
    twostep = 0

    if stair > twostep :
        twostep = ways(stair-2)

    onestep = ways(stair - 1)

    return onestep + twostep

n = int(input("Enter n.o of stairs"))

print(ways(n))
