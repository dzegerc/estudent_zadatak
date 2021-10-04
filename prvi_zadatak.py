n=int(input("Unesite broj elemenata u nizu:"))
b=[]

for i in range(0,n):
    a=int(input("Broj: "))
    b.append(a)

    prviElement=0
    drugiElement=0

    for p in b:
        if(p>0):
            prviElement=prviElement+p

        else:
                drugiElement=drugiElement+p


print("[", prviElement, ',', drugiElement, "]")