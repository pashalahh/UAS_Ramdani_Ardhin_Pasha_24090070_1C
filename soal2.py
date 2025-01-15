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

