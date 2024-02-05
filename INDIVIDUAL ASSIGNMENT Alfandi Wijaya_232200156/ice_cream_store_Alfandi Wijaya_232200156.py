# FUNCTION
def create(flavorlist,hargalist):
    flavorlist.append(input("Masukan Rasa Baru: "))
    hargalist.append(input("Masukan Harga: $"))
    print("Rasa dan Harga sudah ditambahkan :)\n")

def read(flavorlist,hargalist):
    print("Berikut List Rasa & Harga:")
    for i in range(len(flavorlist)):
        print(f"{i+1}. Rasa: {flavorlist[i]} (Harga: ${hargalist[i]})")

def update(flavorlist,hargalist):
    print("List Rasa & Harga:")
    for i in range(len(flavorlist)):
        print(f"{i+1}. Rasa: {flavorlist[i]} (Harga: ${hargalist[i]})")
    updatevalue = int(input("Komponen ke berapa yang ingin diubah: "))
    while updatevalue > len(flavorlist):
        print ("Angka anda tidak ada dalam pilihan!")
        updatevalue = int(input("Komponen ke berapa yang ingin diubah: "))
    flavorlist[updatevalue-1] = input("Masukan Rasa Baru: ")
    hargalist[updatevalue-1] = input("Masukan Harga Baru: ")
    print("Komponen telah diupdate!\n")

def delete(flavorlist,hargalist):
    print("List Rasa & Harga:")
    for i in range(len(flavorlist)):
        print(f"{i+1}. Rasa: {flavorlist[i]} (Harga: ${hargalist[i]})")
    flavorlist.pop(int(input("Masukan Nomor yang ingin dihapus: "))-1)
    print("Komponen telah diHapus!\n")

def main():
    tanya = ""
    flavor = []
    harga = []
    
    print("Selamat Datang di Ice Store!\n")
    while tanya != 0:  
        tanya = int(input("Silahkan pilih opsi berikut! \n 1(create) / 2(read) / 3(update) / 4(delete): "))
        while tanya > 4:
            print ("Angka anda tidak ada dalam pilihan!")
            tanya = int(input("1(create) / 2(read) / 3(update) / 4(delete): "))  
        if tanya == 1:
            create(flavor,harga)
        elif tanya == 2:
            read(flavor,harga)
        elif tanya ==3:
            update(flavor,harga)
        elif tanya == 4:
            delete(flavor,harga)
        else:
            print("Terima Kasih!")

# MAIN
main()
