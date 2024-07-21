def metin_analizi(metin):
    # Karakter adedi
    karakter_adedi = len(metin)
    
    # Sözcük adedi
    sözcük_adedi = len(metin.split())
    
    # Boşluksuz harf adedi
    boşluksuz_harf_adedi = len(metin.replace(" ", ""))
    
    # Paragraf adedi
    paragraf_adedi = len(metin.split('\n'))

    return karakter_adedi, sözcük_adedi, boşluksuz_harf_adedi, paragraf_adedi

def main():
    print("Metin Analiz Programı")
    while True:
        metin = input("Metni girin: ")
        karakter_adedi, sözcük_adedi, boşluksuz_harf_adedi, paragraf_adedi = metin_analizi(metin)
        
        # Sonuçları yazdır
        print(f"Karakter adedi: {karakter_adedi}")
        print(f"Sözcük adedi: {sözcük_adedi}")
        print(f"Boşluksuz harf adedi: {boşluksuz_harf_adedi}")
        print(f"Paragraf adedi: {paragraf_adedi}")

        # Kullanıcıya tekrar çalıştırmak isteyip istemediğini sor
        again = input("Yeni bir metin girmek ister misiniz? (E/H): ").strip().lower()
        if again != 'e':
            print("Çıkış yapılıyor...")
            break

if __name__ == "__main__":
    main()
