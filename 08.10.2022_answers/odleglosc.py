n = int(input("Podaj pierwszą liczbę: "))
m = int(input("Podaj drugą liczbę: "))

while n <= -2*10**9 or n >= 2*10**9:
    n = int(input("Podaj POPRAWNĄ pierwszą liczbę: "))
    
while m <= -2*10**9 or m >= 2*10**9:
    m = int(input("Podaj POPRAWNĄ drugą liczbę: "))

print("Twoje liczby to ", n, "oraz ", m)

if n > m:
    print("Odległośc między tymi liczbami to: ", n - m)

elif n < m:
    print("Odległośc między tymi liczbami to: ", m - n)

else:
    print("Twoje liczby są takie same.")