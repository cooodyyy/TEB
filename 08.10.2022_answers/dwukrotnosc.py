n = int(input("Podaj liczbę: "))

while n <= -10**9 or n >= 10**9:
    n = int(input("Podaj POPRAWNĄ liczbę: "))

print("Dwukrotność ", n , " to ", n*2)

