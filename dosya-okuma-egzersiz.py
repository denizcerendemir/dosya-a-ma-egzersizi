def not_hesapla(satir) :

    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    birinci_not = int(liste[1])
    ikinci_not = int(liste[2])
    final_not = int(liste[3])
    son_not = birinci_not *(3/10) + ikinci_not *(3/10) + final_not * (4/10)

    if (son_not>= 90) :
        harf= "AA"
    elif (son_not >=85):
        harf = "BA"
    elif (son_not >=80):
        harf = "BB"
    elif (son_not >=75):
        harf = "CA"
    elif (son_not >=70):
        harf = "CB"
    elif (son_not >=65):
        harf = "DC"
    elif (son_not >=60):
        harf = "DD"
    elif (son_not >=55):
        harf = "FD"
    else:
        harf = "FF"

    return  isim + "--------------------->" + harf + "\n"




with open("dosya_notlar.txt","r",encoding="utf-8") as file:

    eklenecekler = []
    for i in file:

        eklenecekler.append(not_hesapla(i))

    with open("notlar.txt","w",encoding="utf-8") as file2 :

        for i in eklenecekler:
            file2.write(i)