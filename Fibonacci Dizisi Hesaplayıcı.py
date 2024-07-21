def fibonacci(n):
    if n <= 0:
        return "Lütfen pozitif bir sayı girin."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence

def main():
    print("Fibonacci Dizisi Hesaplayıcı")
    while True:
        try:
            n = int(input("Kaç terim hesaplamak istersiniz? "))
            if n <= 0:
                print("Lütfen pozitif bir sayı girin.")
            else:
                fib_sequence = fibonacci(n)
                print(f"İlk {n} terim: {fib_sequence}")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
        
        again = input("Yeni bir hesaplama yapmak ister misiniz? (E/H): ").strip().lower()
        if again != 'e':
            print("Çıkış yapılıyor...")
            break

if __name__ == "__main__":
    main()
