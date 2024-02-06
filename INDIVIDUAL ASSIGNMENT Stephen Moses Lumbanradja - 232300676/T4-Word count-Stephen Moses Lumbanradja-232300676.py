# Membuka file teks
import re

nama_Kitab = input("Masukkan Nama Kitab: ")
with open(nama_Kitab, 'r') as file:
    # Pembacaan  teks dari file
    teks = file.read()

    # Pengubahan menjadi string yang dapat dipisahkan
    teks = str(teks)
    # Pemisahan kata-kata dalam teks menggunakan split() untuk penyusunan  list kata-kata yang terpisahkan dari teks
    kata_kata = re.split(r'\s|,|.-', teks)

    # Placeholder berupa list  untuk menyimpan kata-kata yang sudah dipisahkan
    kata_kata_terpisah = []

    # Menambahkan setiap kata dari list kata_kata ke list kata_kata_terpisah
    for kata in kata_kata:
        kata_kata_terpisah.append(kata)

    # Membuat kamus untuk menghitung frekuensi kemunculan kata-kata
    frekuensi = {}
    for kata in kata_kata_terpisah:
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1

    # Penampilan kata spesifik yang diminta dan frekuensinya
    kata_spesifik = input("Masukkan kata spesifik: ")
    if kata_spesifik in frekuensi:
        print("Kata '{}' dalam kitab ini muncul sebanyak {} kali.".format(kata_spesifik, frekuensi[kata_spesifik]))
    else:
        print("Kata '{}'  tidak ditemukan dalam kitab ini.".format(kata_spesifik))