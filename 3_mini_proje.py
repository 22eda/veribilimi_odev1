#%%
#9)Alışveriş Sepeti

peynir=float(input("peynirin fiyatınızı giriniz: "))
tavuk=float(input("tavuğun fiyatını giriniz:"))
ekmek=float(input("ekmeğin fiyatını giriniz:"))

toplam_fiyat=peynir+tavuk+ekmek

indirim= toplam_fiyat * 10 /100
son_fiyat=toplam_fiyat

if (toplam_fiyat>200):
    son_fiyat= toplam_fiyat - indirim

print("Toplam sepet tutarı:",toplam_fiyat,"TL")
print("İndirimli sepet tutarı",son_fiyat,"TL")

#%%
#10.soru

dogum_yil=int(input("doğum yılınızı giriniz: "))
güncel_yil=2025

yas=güncel_yil- dogum_yil
print(yas)

if yas>=0 and yas<=12 :
    print("Çocuksunuz")
elif yas>=13 and yas<=17:
    print("Ergensiniz")
elif yas>=18:
    print("Yetişkinsiniz")