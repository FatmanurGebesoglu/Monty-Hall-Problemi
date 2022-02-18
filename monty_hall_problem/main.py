import random

A="A"
B="B"
C="C"
kapilar=["A", "B","C"]
araba=random.choice(kapilar)
print("araba olan %r " % araba)
secim= input("\nBir kapı seçiniz:")
print("\nSeçtiğiniz kapı: %r" % (secim))
if secim == araba:
    kalan = list(set(kapilar) - set(araba))
    acik_kapi = random.choice(list(set(kapilar) - set(random.choice(kalan))))
    alternatif_kapi = random.choice(list(set(kapilar) - set(acik_kapi) - set(araba)))
else:
    acik_kapi =random.choice(list(set(kapilar)-set(secim)-set(araba)))
    alternatif_kapi=random.choice(list(set(kapilar)-set(acik_kapi)-set(secim)))
print("sunucu şu kapıyı açıyor: %r" % acik_kapi)

ikinci_sans=input("kapıyı değiştirmek istiyor musunuz? [EVET/HAYIR]")

if ikinci_sans == "EVET":
    print("Seçmiş olduğunuz yeni kapı : %r " %alternatif_kapi)
    if alternatif_kapi== araba:
        print("tebrikler kazandınız...")
    else:
        print("kaybettiniz...")

if ikinci_sans != "YES":
    print("seçmiş olduğunuz kapı değişmedi : %r" % secim)
    if secim != araba:
        print("kaybettiniz...")
    else:
        print("kazandınız...")

print ("araba olan kapı: %r" % araba)
print ("ilk seçtiğimiz kapı: %r " % secim)
print ( "ikinci şans kapısı: %r " % alternatif_kapi)
print ("sunucunun açtığı kapı: %r " % acik_kapi)