"""
login akun
nama: larry
nim: 026
"""
while True:
    nama = str(input("Masukkan nama Anda: "))
    nim = str(input("Masukkan NIM akhir Anda: "))

    if nama != "larry" or nim != "026":
        print("Maaf Nama/NIM anda salah")
    else:
        print("Selamat datang, " + nama + "!")
        break

while True:
    harga_barang = float(input("Masukkan harga barang: Rp "))
    jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

    total_harga = harga_barang * jumlah_pembelian

    if total_harga > 250000:
        diskon =  total_harga * 0.25
        harga_diskon = total_harga - diskon
        print("Selamat anda mendapatkan diskon 25%")
        print("Jadi total harga yang harus dibayar: Rp " + str(harga_diskon))
    else:
        print("Maaf anda tidak mendapatkan diskon")
        print("jadi total harga yang harus dibayar: Rp " + str(total_harga))

    ulang = input("Ingin menghitung kembali? (yes/no) ")
    if ulang != "yes":
        break

