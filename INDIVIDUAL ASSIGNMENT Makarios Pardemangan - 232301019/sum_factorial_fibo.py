def hitung_sum(n):
    return sum(range(1, n+1))

def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n-1)

def hitung_fibonacci(n):
    if n <= 0:
        return "Input harus lebih besar dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n-2):
            a, b = b, a + b
        return b

# Contoh penggunaan
angka = int(input("Masukkan angka: "))

print(f"Sum({angka}) = {hitung_sum(angka)}")
print(f"{angka}! = {hitung_faktorial(angka)}")
print(f"Fibo({angka}) = {hitung_fibonacci(angka)}")
