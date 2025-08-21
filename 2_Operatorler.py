
#Bolum2: Operatörler

#4.soru
#%%
x=float(input("1.sayıyı giriniz: "))
y=float(input("2.sayıyı giriniz: "))

print("Toplama", x+y)
print("Çıkarma", x-y)
print("Çarpma", x*y)
print("Bölme", x/y)
print("Mod(Kalan)", x%y)
#%%

#2.yol

x=int(input("1.sayıyı giriniz: "))
y=int(input("2.sayıyı giriniz: "))

print("islem seçiniz(+,-,*,/,%):")
islem=input("islem:")

if islem == "+":
        print("Toplamı:" , x + y)

elif islem == "-":
        print("Çıkarma:", x-y)

elif islem == "*":
        print("Çarpım:", x*y)

elif islem == "/":
        if y!= 0:
         print("Bölümü:", x/y)
        else:
         print("Hata: Sayı 0'a bölünemez.")

elif islem== "%":
        print("Modu:", x%y)

else:
        print("Geçersiz işlem!")


#%%
#5.soru

ort=float(input("ortalamanızı giriniz: "))

if ort>=50 :
    print("Geçti")
else:
    print("Kaldı!")

#%%
#6.soru

yas=int(input("yaşınızı giriniz: "))

if yas>=18:
    print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız.")

#%%
#7.soru
fiyat=float(input("ürünün fiyatını giriniz: "))
yuzde=float(input("indirim oranını giriniz: "))

indirim= fiyat * yuzde /100
indirimli_fiyat= fiyat - indirim
print(indirimli_fiyat)

#%%
#8.soru

a=True
b=False

print("a and b :", a and b)
print("a or b", a or b)
print("not a :", not a)
print("not b:", not b)




#%%
x=70
y=20

print(x>30 or 30<y)
print(x<10 and y<10)
print(not(x>5))

