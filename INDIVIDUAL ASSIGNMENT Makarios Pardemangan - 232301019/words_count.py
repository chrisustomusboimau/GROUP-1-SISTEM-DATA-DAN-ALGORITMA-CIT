def hitung_jumlah_kata(kalimat):
    kata = kalimat.split()
    return len(kata)

# Contoh penggunaan
kalimat_input = input("Masukkan sebuah kalimat: ")
hasil_hitung_kata = hitung_jumlah_kata(kalimat_input)

print(f"Jumlah kata dalam kalimat '{kalimat_input}' adalah: {hasil_hitung_kata}")
