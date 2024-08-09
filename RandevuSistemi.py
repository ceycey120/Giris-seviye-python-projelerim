import json
# Kullanıcıların verdiği bilgileri bu dosyaya kaydedeceğiz. Sonraki çalıştırmalar için rezervasyonları buradan kontrol edeceğiz. 
import os
from datetime import datetime

# Masalar ve kapasiteleri. Her masanın kaç kişilik olduğu bilgisi. Daha dinamik hale geldi.
masalar = {
    1: {"kapasite": 4, "dolu": False},
    5: {"kapasite": 2, "dolu": False},
    7: {"kapasite": 6, "dolu": False},
    13: {"kapasite": 4, "dolu": False},
    15: {"kapasite": 8, "dolu": False},
    16: {"kapasite": 2, "dolu": False},
    6: {"kapasite": 3, "dolu": False},
    8: {"kapasite": 5, "dolu": False},
    19: {"kapasite": 4, "dolu": False},
}

# Kullanıcıların rezervasyonları ve rezervasyon tarihleri. Bu sayede daha spesifik bilgi edindik.
rezervasyonlar = {
    "ali": {"masa_no": 5, "tarih": "2024-08-09"},
    "veli": {"masa_no": 5, "tarih": "2024-08-10"},
    "ahmet": {"masa_no": 1, "tarih": "2024-08-09"},
    "mehmet": {"masa_no": 7, "tarih": "2024-08-09"},
    "fuat": {"masa_no": 13, "tarih": "2024-08-09"},
    "ayse": {"masa_no": 15, "tarih": "2024-08-09"},
    "fatma": {"masa_no": 16, "tarih": "2024-08-09"},
    "sevgi": {"masa_no": 6, "tarih": "2024-08-09"},
    "nil": {"masa_no": 8, "tarih": "2024-08-09"},
    "deniz": {"masa_no": 19, "tarih": "2024-08-09"},
}

# Güncel rezervasyon bilgilerini JSON dosyasından yükleme. Rezervasyon bilgileri kontrolü
def rezervasyonlari_yukle():
    if os.path.exists("rezervasyonlar.json"):
        with open("rezervasyonlar.json", "r") as dosya:
            return json.load(dosya)
    return rezervasyonlar

# Güncel rezervasyonları JSON dosyasına kaydetme
def rezervasyonlari_kaydet(rezervasyonlar):
    with open("rezervasyonlar.json", "w") as dosya:
        json.dump(rezervasyonlar, dosya)

# Masa seçimi ve rezervasyon güncelleme. 
def masa_secimi():
    uygun_masalar = [masa for masa, bilgi in masalar.items() if not bilgi["dolu"]]
    if not uygun_masalar:
        print("Maalesef, mevcut boş masa yok.")
        return None
    print("Uygun Masalar:", uygun_masalar)
    secilen_masa = int(input("Bir masa seçin: "))
    if secilen_masa in uygun_masalar:
        return secilen_masa
    else:
        print("Geçersiz masa seçimi.")
        return None

# Ana program
def ana_program():
    rezervasyonlar = rezervasyonlari_yukle()
    isim = input('İsminiz Nedir? ').lower()
    
    if isim in rezervasyonlar:
        tarih = input('Rezervasyon tarihiniz nedir? (YYYY-MM-DD) ')
        if rezervasyonlar[isim]["tarih"] == tarih:
            masa_no = rezervasyonlar[isim]["masa_no"]
            print(f"{masa_no} Numaralı Masada {tarih} için Rezarvasyonunuz Var.")
        else:
            print("Rezervasyonunuz bu tarih için değil.")
        
        # Rezervasyon güncelleme seçeneği
        guncelleme = input("Rezervasyonunuzu güncellemek ister misiniz? (E/H) ").lower()
        if guncelleme == "e":
            yeni_masa_no = masa_secimi()
            if yeni_masa_no:
                rezervasyonlar[isim] = {"masa_no": yeni_masa_no, "tarih": tarih}
                masalar[yeni_masa_no]["dolu"] = True
                print(f"Rezervasyonunuz {yeni_masa_no} Numaralı Masaya güncellenmiştir.")
    elif isim not in rezervasyonlar:
        print("Rezervasyonunuz yok.")
        yeni_rezervasyon = input("Yeni bir rezervasyon yapmak ister misiniz? (E/H) ").lower()
        if yeni_rezervasyon == "e":
            tarih = input('Rezervasyon yapmak istediğiniz tarihi girin (YYYY-MM-DD): ')
            yeni_masa_no = masa_secimi()
            if yeni_masa_no:
                rezervasyonlar[isim] = {"masa_no": yeni_masa_no, "tarih": tarih}
                masalar[yeni_masa_no]["dolu"] = True
                print(f"{yeni_masa_no} Numaralı Masada {tarih} için rezervasyonunuz yapılmıştır.")
    
    rezervasyonlari_kaydet(rezervasyonlar)

if __name__ == "__main__":
    ana_program()
