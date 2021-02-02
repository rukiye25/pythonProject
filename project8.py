metin=input("bir metin giriniz")
def first_repat(metin):
    metin=list(metin)
    tekar=[]
    for i in metin:
        sayi=metin.count(i)
        if sayi>1:
            tekar.append(i)
    if len(tekar)<1:
        print(0)
    else:
        print(tekar)
        print(tekar[0])
first_repat(metin)