def pangkat(a, b):
    hasil = 1
    for i in range(1, b + 1):
        hasil *= a
        print(f"hasil {a} pangkat {i} adalah {hasil}")
    return hasil


def deret(n):
    a, b = 1, 2   
    c, d = 1, 3   
    hasil = 0
    tanda = 1

    for i in range(n):
        if i == 0:
            hasil += 1
        else:
            pecahan = b / d
            hasil += tanda * pecahan

            a, b = b, a + b
            c, d = d, c + d

            tanda *= -1

    return hasil

while True:
    print("\nNim Ganjil")
    print("1. A pangkat B")
    print("2. Hitung deret")
    print("0. keluar")

    pilih = int(input("Masukkan : "))

    if pilih == 1:
        a = int(input("masukan suatu bilangan bulat : "))
        b = int(input("masukan pangkat yang diinginkan : "))
        pangkat(a, b)

    elif pilih == 2:
        n = int(input("Masukkan jumlah N : "))
        hasil = deret(n)
        print(hasil)

    elif pilih == 0:
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")