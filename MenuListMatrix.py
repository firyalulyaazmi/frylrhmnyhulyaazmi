while True:
    print("\n==== MENU ====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilih = int(input("Pilih menu: "))

    if pilih == 0:
        print("Program selesai")
        break

    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))

    print("\nMatriks A")
    A = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(int(input(f"A[{i}][{j}] = ")))
        A.append(row)

    print("\nMatriks B")
    B = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(int(input(f"B[{i}][{j}] = ")))
        B.append(row)

    hasil = []

    if pilih == 1: 
        for i in range(baris):
            row = []
            for j in range(kolom):
                row.append(A[i][j] + B[i][j])
            hasil.append(row)

        print("\nHasil Penjumlahan:")
        for r in hasil:
            print(r)

    elif pilih == 2:
        for i in range(baris):
            row = []
            for j in range(kolom):
                row.append(A[i][j] - B[i][j])
            hasil.append(row)

        print("\nHasil Pengurangan:")
        for r in hasil:
            print(r)

    elif pilih == 3: 
        for i in range(baris):
            row = []
            for j in range(kolom):
                total = 0
                for k in range(kolom):
                    total += A[i][k] * B[k][j]
                row.append(total)
            hasil.append(row)

        print("\nHasil Perkalian:")
        for r in hasil:
            print(r)

    else:
        print("Pilihan tidak ada!")