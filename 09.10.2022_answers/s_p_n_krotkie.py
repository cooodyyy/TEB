allNmbrs=[]
sumEven=0
sumOdd=0
length = int(input("Podaj długość ciągu: "))

for element in range(length): 
    print("Podaj liczbę nr ", element+1)
    allNmbrs.append(int(input()))

for element in allNmbrs:
    if element % 2==0:
        sumEven+=element
    else:
        sumOdd+=element

if sumEven > sumOdd:
    print("Suma liczb parzystych jest większa.")
elif sumEven < sumOdd:
    print("Suma liczb nieparzystych jest większa.")
else:
    print("Suma licz parzystych i nieparzystych jest taka sama.")