def uzzimet_apli():
    radius = int(input("Kāds radius? "))

    for rinda in range(radius):
        if rinda < radius//2:
            atstarpe =(radius-1) // 2 - rinda

        else:
            atstarpe = rinda - radius//2

    

uzzimet_apli()