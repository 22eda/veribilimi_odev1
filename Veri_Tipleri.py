
# Bolum1: Veri Tipleri

#Soru1:
#%%
ad=input("Adınızı giriniz: ")
yas =int(input("Yaşını giriniz= "))
boy=float(input("Boyunuzu giriniz= "))

print(f"Adınız: {ad} , Yaşınız: {yas}, Boyunuz: {boy}  ")
#print(f"Adınız:", ad, "Yaşınız:",yas, "Boyunuz:", boy)

#%%
#Soru2:
mat_not=int(input("Matematik notunuzu giriniz:"))
fiz_not=int(input("Fizik notunuzu giriniz:"))
kim_not=int(input("Kimya notunuzu giriniz:"))

ortalama=float((mat_not+fiz_not+kim_not)/3.0)
print("ortalamanız: ", ortalama)

#%%
#Soru3:
degisken= "Edanur"

print(degisken[0:6:5])
print(len(degisken))
print(degisken[::-1])

#%%
#2.yol
print("ilk karakter", degisken[0])
print("Son karakter", degisken[-1])
print("Uzunluk", len(degisken))
print("Metnin tersi", degisken[::-1])