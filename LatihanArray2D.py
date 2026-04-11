mahasiswa = [
    {"nim": "10121001", "nama": "Asep"},
    {"nim": "10121002", "nama": "Budi"},
    {"nim": "10121003", "nama": "Cecep"},
]

nilai = [
    {"nim": "10121001", "MK1": 50, "MK2": 70, "MK3": 40, "MK4": 80},
    {"nim": "10121002", "MK1": 78, "MK2": 78, "MK3": 80, "MK4": 65},
    {"nim": "10121003", "MK1": 57, "MK2": 88, "MK3": 67, "MK4": 69},
]

rata_mahasiswa = []

for n in nilai:
    total = n["MK1"] + n["MK2"] + n["MK3"] + n["MK4"]
    rata = total / 4

    data = {
        "nim": n["nim"],
        "rata": rata
    }
    rata_mahasiswa.append(data)

tertinggi = rata_mahasiswa[0]

for r in rata_mahasiswa:
    if r["rata"] > tertinggi["rata"]:
        tertinggi = r

nama_tertinggi = ""

for m in mahasiswa:
    if m["nim"] == tertinggi["nim"]:
        nama_tertinggi = m["nama"]

mk1 = mk2 = mk3 = mk4 = 0

for n in nilai:
    mk1 = mk1 + n["MK1"]
    mk2 = mk2 + n["MK2"]
    mk3 = mk3 + n["MK3"]
    mk4 = mk4 + n["MK4"]

jumlah = len(nilai)

rata_mk1 = mk1 / jumlah
rata_mk2 = mk2 / jumlah
rata_mk3 = mk3 / jumlah
rata_mk4 = mk4 / jumlah

mk_terkecil = "MK1"
nilai_terkecil = rata_mk1

if rata_mk2 < nilai_terkecil:
    mk_terkecil = "MK2"
    nilai_terkecil = rata_mk2

if rata_mk3 < nilai_terkecil:
    mk_terkecil = "MK3"
    nilai_terkecil = rata_mk3

if rata_mk4 < nilai_terkecil:
    mk_terkecil = "MK4"
    nilai_terkecil = rata_mk4

print("Mahasiswa Terpintar :", nama_tertinggi, 
      "(Nilai :", round(tertinggi["rata"], 2), ")")

print("Mata Kuliah Nilai Terkecil :", mk_terkecil, 
      "(Nilai :", round(nilai_terkecil, 2), ")")