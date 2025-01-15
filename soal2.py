import pandas as pd

data = pd.DataFrame([
    [90,80],
    [50,60],
    [65,70],

],
index=['Mahasiswa 1','Mahasiswa 2','Mahasiswa 3'],
columns =['Algoritma dan Struktur Data 2','Matematika Numerik'])

nilai_mk = data.sum(axis=0) 
nilai_mhs = data.sum(axis=1) 

print(data)
print('='*100)
print('Rata-rata nilai untuk setiap mata kuliah')
print(nilai_mk)
print('='*100)
print('Rata-rata nilai untuk setiap mahasiswa')
print(nilai_mhs)
print('='*100)

# ef hitung_rata_rata(nilai):
#     rata_mk = [sum(col) / len(col) for col in zip(*nilai)]
#     rata_mhs = [sum(row) / len(row) for row in nilai]
#     return rata_mk, rata_mhs

# def tampilkan_hasil(nilai):
#     print("Tabel Nilai:")
#     for i, baris in enumerate(nilai, start=1):
#         print(f"Mahasiswa {i}: {baris}")

#     rata_mk, rata_mhs = hitung_rata_rata(nilai)
#     print("\nRata-rata per Mata Kuliah:")
#     for i, rata in enumerate(rata_mk, start=1):
#         print(f"Mata Kuliah {i}: {rata:.2f}")

#     print("\nRata-rata per Mahasiswa:")
#     for i, rata in enumerate(rata_mhs, start=1):
#         print(f"Mahasiswa {i}: {rata:.2f}")

# tampilkan_hasil(nilai)