# Ekrana Yazdırma
# Basit yazdırma
print("Merhaba Dünya")
print('Python öğreniyorum')

# Değişken yazdırma
isim = "Barış"
print("Merhaba", isim)

# Alt satıra geçme
print("Birinci satır\nİkinci satır")

# Tab boşluğu
print("İsim:\tBarış")

# Birden fazla değer yazdırma
print("Sayı:", 42, "Metin:", "Python")

# Variables
# Sayısal değişkenler
yas = 21
boy = 1.75
toplam = 100.5

# Metin değişkenleri
isim = "Barış"
sehir = "İstanbul"

# Boolean değişkenler
aktif = True
ogrenci = False

# Çoklu atama
x, y, z = 10, 20, 30
a = b = c = 50

# Arithmetic Operators
# Toplama
sonuc = 10 + 5  # 15

# Çıkarma
sonuc = 10 - 5  # 5

# Çarpma
sonuc = 10 * 5  # 50

# Bölme
sonuc = 10 / 3  # 3.333...

# Tam bölme
sonuc = 10 // 3  # 3

# Mod alma (kalan)
sonuc = 10 % 3  # 1

# Üs alma
sonuc = 2 ** 3  # 8

# Compare Operators
a = 10
b = 20

# Eşit mi?
print(a == b)  # False

# Eşit değil mi?
print(a != b)  # True

# Büyük mü?
print(a > b)  # False

# Küçük mü?
print(a < b)  # True

# Büyük eşit mi?
print(a >= 10)  # True

# Küçük eşit mi?
print(b <= 15)  # False

# Logical Oparators
x = 15

# and (ve)
print(x > 10 and x < 20)  # True

# or (veya)
print(x < 10 or x > 5)  # True

# not (değil)
print(not(x > 20))  # True

# Conditions
# If-Else
yas = 20

if yas >= 18:
    print("Reşitsiniz")
else:
    print("Reşit değilsiniz")

# If-Elif-Else
puan = 75

if puan >= 90:
    print("A")
elif puan >= 80:
    print("B")
elif puan >= 70:
    print("C")
else:
    print("F")

# İç içe if
sayi = 15

if sayi > 0:
    if sayi % 2 == 0:
        print("Pozitif çift sayı")
    else:
        print("Pozitif tek sayı")
else:
    print("Negatif sayı")

# Kısa if (ternary)
durum = "Reşit" if yas >= 18 else "Reşit değil"

# Loops
# Basit for döngüsü
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Belirli aralık
for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

# Adım değeri ile
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Liste üzerinde döngü
meyveler = ["elma", "armut", "muz"]
for meyve in meyveler:
    print(meyve)

# Enumerate ile
for index, meyve in enumerate(meyveler):
    print(f"{index}: {meyve}")

# While
# Basit while
sayac = 0
while sayac < 5:
    print(sayac)
    sayac += 1

# Break ile döngüden çıkma
while True:
    sayi = int(input("Sayı girin (0 için çıkış): "))
    if sayi == 0:
        break
    print(f"Girilen: {sayi}")

# Continue ile atlama
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)  # Sadece tek sayıları yazdırır

# Collections
# Liste oluşturma
sayilar = [1, 2, 3, 4, 5]
meyveler = ["elma", "armut", "muz"]
karisik = [1, "iki", 3.0, True]

# Eleman ekleme
meyveler.append("çilek")  # Sona ekler
meyveler.insert(1, "kiraz")  # Belirli pozisyona

# Eleman silme
meyveler.remove("muz")  # Değere göre
del meyveler[0]  # İndekse göre
cikarilan = meyveler.pop()  # Son elemanı çıkarır

# Erişim
print(meyveler[0])  # İlk eleman
print(meyveler[-1])  # Son eleman
print(meyveler[1:3])  # Dilim alma

# Liste metodları
sayilar.sort()  # Sırala
sayilar.reverse()  # Ters çevir
uzunluk = len(sayilar)  # Uzunluk

# List comprehension
kareler = [x**2 for x in range(10)]
cift_sayilar = [x for x in range(20) if x % 2 == 0]

# Tuple oluşturma
koordinat = (10, 20)
renkler = ("kırmızı", "yeşil", "mavi")

# Erişim
print(koordinat[0])  # 10
print(renkler[-1])  # mavi

# Tuple unpacking
x, y = koordinat
print(x, y)

# Tuple metodları
sayi = renkler.count("kırmızı")  # Kaç tane var
indeks = renkler.index("yeşil")  # İlk görüldüğü yer

# Tek elemanlı tuple
tek = (5,)  # Virgül gerekli

# Set oluşturma
sayilar = {1, 2, 3, 4, 5}
meyveler = {"elma", "armut", "muz"}

# Tekrar eden elemanlar silinir
sayilar = {1, 2, 2, 3, 3, 3}  # {1, 2, 3}

# Eleman ekleme
meyveler.add("çilek")

# Eleman silme
meyveler.remove("muz")
meyveler.discard("kiraz")  # Yoksa hata vermez

# Küme işlemleri
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

birlesim = set1 | set2  # {1, 2, 3, 4, 5, 6}
kesisim = set1 & set2  # {3, 4}
fark = set1 - set2  # {1, 2}
simetrik_fark = set1 ^ set2  # {1, 2, 5, 6}

# Dictionary oluşturma
kisi = {
    "isim": "Barış",
    "yas": 21,
    "sehir": "İstanbul",
    "ogrenci": True
}

# Erişim
print(kisi["isim"])  # Barış
print(kisi.get("yas"))  # 21
print(kisi.get("ulke", "Türkiye"))  # Yoksa varsayılan

# Ekleme/Güncelleme
kisi["email"] = "baris@example.com"
kisi["yas"] = 22

# Silme
del kisi["sehir"]
deger = kisi.pop("ogrenci")

# Dictionary metodları
anahtarlar = kisi.keys()  # Tüm anahtarlar
degerler = kisi.values()  # Tüm değerler
ciftler = kisi.items()  # Tüm çiftler

# Döngü ile dolaşma
for anahtar, deger in kisi.items():
    print(f"{anahtar}: {deger}")

# Dictionary comprehension
kareler = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}