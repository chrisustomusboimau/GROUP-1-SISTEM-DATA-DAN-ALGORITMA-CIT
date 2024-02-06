#Validasi integer dan Penghasilan Faktorial
def faktorial(Angka):
    faktorial = 1
    for i in range(1, Angka + 1):
        faktorial *= i
    return faktorial

def validasi_integer():
    while True:
        try:
            Angka = int(input("Masukkan sebuah bilangan bulat: "))
            if Angka > 0:
                print("Bilangan tersebut lebih besar dari 0.")
                hasil_faktorial = faktorial(Angka)
                print(f"{Angka}! = {hasil_faktorial}")
            else:
                print("input tersebut tidak lebih besar dari 0.")
            break
        except ValueError:
            print("Input invalid, yang Anda masukkan bukan bilangan bulat. Silakan coba lagi.")

validasi_integer()



#Validasi integer dan Penghasilan Sum

def hitung_jumlah(Angka):
    jumlah = 0
    for i in range(1, Angka + 1):
        jumlah += i
    return jumlah

def validasi_integer():
    while True:
        try:
            Angka = int(input("Masukkan sebuah bilangan bulat: "))
            if Angka > 0:
                print("Bilangan tersebut lebih besar dari 0.")
                hasil_jumlah = hitung_jumlah(Angka)
                print(f"Jumlah (Summation) dari bilangan 1 sampai {Angka} adalah {hasil_jumlah}.")
            else:
                print("Bilangan tersebut tidak lebih besar dari 0.")
            break
        except ValueError:
            print("Input yang Anda masukkan bukan bilangan bulat. Silakan coba lagi.")

validasi_integer()

#Validasi Integer dan Penghitungan Fibonacci

def hitung_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

def validasi_integer():
    while True:
        try:
            Angka = int(input("Masukkan sebuah bilangan bulat: "))
            if Angka > 0:
                print("Bilangan tersebut lebih besar dari 0.")
                hasil_fibonacci = hitung_fibonacci(Angka)
                print(f"Bilangan Fibonacci ke-{Angka} adalah {hasil_fibonacci}.")
            else:
                print("Bilangan tersebut tidak lebih besar dari 0.")
            break
        except ValueError:
            print("Input yang Anda masukkan bukan bilangan bulat. Silakan coba lagi.")

validasi_integer()

print(Angka)