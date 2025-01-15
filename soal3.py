antrian = ['papa','pipi']

def enqueue(value): 
    antrian.append (value)

while True:
    print(f'Antrian Sekarang : {antrian[0]}') 
    print(f'Jumlah Antrian : {len(antrian)}')
    print(f'Daftar Antrian : {antrian}')
    print('pilihan :')
    print(' 1.Tambah Antrian')
    print(' 2.Hapus Antrian')
    print(' 3.Keluar')

    print('='*50)
    pilih = int(input('Pilihan Operasi (1/2/3/4) : '))
    print('='*50)

    if pilih == 1:
        nama = str(input(f'Masukan Nama Pelanggan : '))
        enqueue(nama) 
        print(f'"{nama}" Berhasil ditambahkan ke antrian')
        print('='*50)

    elif pilih == 2:
        remove = antrian.pop(0) 
        print(f'Daftar Antrian sekarang "{remove}"')
        print('='*50)

    
    if pilih == 3 :
        print('Terimakasih Telah Berkunjung')
        print('='*50)
        break