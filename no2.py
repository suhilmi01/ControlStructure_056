angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

if angka1 == angka2 and angka2 == angka3:
    print("Tidak ada angka yang terbesar karena semua angka sama")
elif (angka1 >= angka2) and (angka1 >= angka3):
    terbesar = angka1
    print("Angka terbesar adalah:", terbesar)
elif (angka2 >= angka1) and (angka2 >= angka3):
    terbesar = angka2
    print("Angka terbesar adalah:", terbesar)
elif (angka3 >= angka1) and (angka3 >= angka2):
    terbesar = angka3
    print("Angka terbesar adalah:", terbesar)
else:
    print("Tidak ada angka terbesar")