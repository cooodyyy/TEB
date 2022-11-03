allNmbrs=[]
length = int(input("Podaj długość ciągu: "))

for element in range(length): 
    print("Podaj liczbę nr ", element+1)
    allNmbrs.append(int(input()))