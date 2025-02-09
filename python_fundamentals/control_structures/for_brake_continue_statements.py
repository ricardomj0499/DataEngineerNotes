# Finds non prime number and print the first two factor of the number on that list that are not primer
# Shows the use of break

#print("primero rango> ", list(range(2, 10)))
for n in range(2, 10):
    #print("N>", n)
    #print("segundo rango> ", list(range(2, n)))
    for x in range(2, n):
        #print("X> ", x)
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
