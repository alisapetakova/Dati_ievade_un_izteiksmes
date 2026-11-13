#1 - akmens
#2 - papīrs
#3 - šķēres
import random

datora_izvele = random.randint(1, 3)

spēlētāja_izvele = int(input("Izvēlies: #1 - akmens, #2 - papīrs, #3 - šķēres: "))

if spēlētāja_izvele == datora_izvele:
    print("Neizšķirts!")
elif (spēlētāja_izvele == 1 and datora_izvele == 3) or (spēlētāja_izvele == 2 and datora_izvele == 1) or (spēlētāja_izvele == 3 and datora_izvele == 2):
    print("Tu uzvarēji!")
else:
    print("Dators uzvarēja!")