while True :
    NIM = int(input('Masukan NIM : '))
    Nama = str(input('Masukan Nama : '))
    pilih = input('Ingin Tambah lagi? : ')
    if pilih == 'ya':
        continue
    else:
        pilih == 'tidak'
        print(f'Nama : {Nama} dengan NIM : {NIM}')
        break