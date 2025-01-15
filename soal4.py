class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    
    def setMerk(self,item): #Ganti Nama Mobil
        self.nama = item 
    
    def setWarna(self,colour):
        self.warna = colour

    def setRasa(self,enak):
        self.rasa = enak

    def information(self):
        return f'Buah : {self.nama} | warna : {self.warna} | rasa : {self.rasa}'
    


buahan = Buah('melon','hijau', 'manis')
buahan.setMerk('anggur')
buahan.setWarna('ungu')
buahan.setRasa('kecut')
print(buahan.information())