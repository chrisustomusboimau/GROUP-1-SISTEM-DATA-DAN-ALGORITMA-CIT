def hitung_jumlah_huruf(kata):
    jumlah_huruf = 0
    for huruf in kata:
        
        if huruf.isalpha():
            jumlah_huruf += 1
    return jumlah_huruf


kata_input = input("Masukkan sebuah kata: ")
hasil_hitung = hitung_jumlah_huruf(kata_input)

print(f"Jumlah huruf dalam kata '{kata_input}' adalah: {hasil_hitung}")
