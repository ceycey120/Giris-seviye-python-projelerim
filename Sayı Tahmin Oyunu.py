import random

def sayı_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım bu sayıyı kaç denemede bulabileceksiniz?")

    # 1 ile 100 arasında rastgele bir sayı seç
    tutulan_sayı = random.randint(1, 100)
    tahmin_sayısı = 0

    while True:
        try:
            tahmin = int(input("Tahmininizi girin: "))
            tahmin_sayısı += 1

            if tahmin < tutulan_sayı:
                print("Daha büyük bir sayı söyleyin.")
            elif tahmin > tutulan_sayı:
                print("Daha küçük bir sayı söyleyin.")
            else:
                print(f"Tebrikler! {tahmin_sayısı} denemede doğru tahmin ettiniz.")
                break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    # Kullanıcıya tekrar oynamak isteyip istemediğini sor
    again = input("Yeniden oynamak ister misiniz? (E/H): ").strip().lower()
    if again == 'e':
        sayı_tahmin_oyunu()
    else:
        print("Oyun bitti. Teşekkürler!")

if __name__ == "__main__":
    sayı_tahmin_oyunu()
