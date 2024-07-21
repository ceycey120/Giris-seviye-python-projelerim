import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Hata! Payda sıfır olamaz."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Hata! Negatif sayının karekökü reel kümede tanımlı değildir."
    else:
        return math.sqrt(x)

def log(x):
    if x <= 0:
        return "Hata! Logaritma pozitif sayılar için geçerlidir."
    else:
        return math.log(x)

def factorial(x):
    if x < 0:
        return "Hata! Negatif sayının faktöriyeli."
    else:
        return math.factorial(x)

def trigonometry(x, func):
    if func == 'sin':
        return math.sin(x)
    elif func == 'cos':
        return math.cos(x)
    elif func == 'tan':
        return math.tan(x)
    else:
        return "Geçersiz trigonometri fonksiyonu."

def display_menu():
    print("İleri Seviye Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Karekök")
    print("7. Logaritma")
    print("8. Faktöriyel")
    print("9. Trigonometri")
    print("10. Çıkış")

def main():
    while True:
        display_menu()
        choice = input("Yapmak istediğiniz işlemin numarasını yazın: ")

        if choice == '10':
            print("Çıkış yapılıyor...")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("İlk sayıyı girin: "))
            num2 = float(input("İkinci sayıyı girin: "))

        if choice == '1':
            print(f"Sonuç: {add(num1, num2)}")

        elif choice == '2':
            print(f"Sonuç: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"Sonuç: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"Sonuç: {divide(num1, num2)}")

        elif choice == '5':
            print(f"Sonuç: {power(num1, num2)}")

        elif choice == '6':
            num = float(input("Sayıyı girin: "))
            print(f"Sonuç: {square_root(num)}")

        elif choice == '7':
            num = float(input("Sayıyı girin: "))
            print(f"Sonuç: {log(num)}")

        elif choice == '8':
            num = int(input("Sayıyı girin: "))
            print(f"Sonuç: {factorial(num)}")

        elif choice == '9':
            num = float(input("Sayıyı girin (radyan cinsinden): "))
            func = input("Fonksiyonu girin (sin, cos, tan): ")
            print(f"Sonuç: {trigonometry(num, func)}")

        else:
            print("Geçersiz seçim, tekrar deneyin.")
        
        # Kullanıcıya yeni bir işlem yapmak isteyip istemediğini soralım
        again = input("Yeni bir işlem yapmak ister misiniz? (E/H): ").strip().lower()
        if again != 'e':
            print("Çıkış yapılıyor...")
            break

if __name__ == "__main__":
    main()
