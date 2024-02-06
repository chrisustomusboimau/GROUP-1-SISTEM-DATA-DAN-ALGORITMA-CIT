def evaluasi_nilai(nilai):
    if nilai >= 0 and nilai <= 50:
        return 'C'
    elif nilai >= 51 and nilai <= 85:
        return 'B'
    elif nilai >= 86 and nilai <= 100:
        return 'A'
    else:
        return 'Nilai tidak valid'

# Contoh penggunaan
nilai_mahasiswa = float(input("Masukkan nilai mahasiswa (0-100): "))

if nilai_mahasiswa >= 0 and nilai_mahasiswa <= 100:
    hasil_evaluasi = evaluasi_nilai(nilai_mahasiswa)
    print(f"Hasil evaluasi: {hasil_evaluasi}")
else:
    print("Nilai tidak valid. Masukkan nilai antara 0 dan 100.")
