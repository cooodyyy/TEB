m = int(input("Podaj masę ciała w kilogramach: "))
h = float(input("Podaj wzrost w metrach: "))


#najcięższy człowiek < 600kg
#najmniejszy noworodek < 0.2kg
while m <= 0 or m >= 600:
    m==0
    m = int(input("Podaj POPRAWNĄ masę ciała w kilogramach: "))
    
#najwyższy człowiek < 300cm
#najniższy noworodek < 24cm
while h < 0.2 or h >= 3.0:
    h==0
    h = float(input("Podaj POPRAWNY wzrost w metrach: "))

bmi = float(m / h**2)
print("Twoje BMI wynosi: ", bmi)

if bmi < 20:
    print("NIEDOWAGA")
    
elif bmi <= 25:
    print("WAGA W NORMIE")

elif bmi <= 30:
    print("NADWAGA")

else:
    print("OTYŁOŚĆ")