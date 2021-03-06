#membuat file txt
def buat_file():
    file = (input("Masukkan Nama File : "))
    teks = (input("Masukkan Kalimat : "))
    file2 = open(file+'.txt', "w")
    file2.write(teks)
    file2.close()
    
#membaca file txt
def baca_file():
    baca = (input("Masukkan Nama File : "))
    file = open(baca+'.txt', "r")
    baca2 = file.read()
    print(baca2)
    file.close()
    
#menghitung frekuensi
def hitung_kata1():
    masukkan_kata = input('Masukkan Kalimat: ')
    cari_kata = input('Masukkan Kata atau Huruf: ')
    print('Jumlah kemunculan ',cari_kata, 'adalah :', masukkan_kata.count(cari_kata))

def hitung_kata2():
    masukkan_kata = input('Masukkan Nama File : ')
    file = open(masukkan_kata+'txt', "r")
    baca = file.read()
    print(baca)
    cari_kata = input('Masukkan Kata atau Huruf: ')
    print('Jumlah kemunculan ',cari_kata, 'adalah :', baca.count(cari_kata))
    file.close()
    
def hitung_frekuensi():
    print("1.Input Kalimat \n2.Input Nama File Yang Sudah Ada")
    hitung = int(input("Masukkan Pilihan : "))
    if hitung==1:
        hitung_kata1()
    elif hitung==2:
        hitung_kata2()

#Main Menu
while(1):
    print('\nNama : Kadek Vincky Sedana\nNIM : 1808561071')
    print('\nTugas Kriptoanalis')
    print('1.Buat File\n2.Baca File\n3.Hitung Frekuensi\n0.Exit\n')
    pilih = int(input('Masukkan Pilihan : '))
    if pilih==1:
        buat_file()
    elif pilih==2:
        baca_file()
    elif pilih==3:
        hitung_frekuensi()
    else:
        break
