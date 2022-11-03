n=int(input("Podaj liczbę: "))
x=0

for x in range (n+1):
    print(2**x )
    x=x+1
    if x==n+15:
        break
