def hitung():
    #Menginput nama file yang ingin dicari
    input_kata = input('Masukkan Nama File : ')
    file = open(input_kata+'.txt', "r+")
    baca = file.read()
    print(baca)

    #Menghitung jumlah keseluruhan karakter
    baca2 = baca.replace(" ", "")
    jadikan_list = baca2.split()
    hitung_kata = len(jadikan_list)
    print ('Jumlah Karakter :', len(baca2))

    #Menghitung jumlah salah satu krakter
    detail = str(input('Apakah anda ingin tau jumlah sebuah huruf? (Y/N) : '))
    if(detail=="Y" or detail=="y"):
        cari_huruf = input('Masukkan huruf yang ingin dihitung : ')
        print('Jumlah kemunculan',cari_huruf, 'adalah :', baca.count(cari_huruf))
    else:
        print("")

    #Menukar karakter
    Tukar = str(input('Apakah anda ingin menukar sebuah huruf? (Y/N) : '))
    if(Tukar=="Y" or Tukar=="y"):
        temp = 0
        string = input('Masukkan huruf pertama : ')
        string2 = input('Masukkan Huruf kedua : ')
        baca = baca.replace(string,str(temp))
        baca = baca.replace(string2,string)
        print(baca.replace(str(temp),string2))
    else:
        print('Terimakasih')
    file.close()

#Main Menu
print('\nNama : Kadek Vincky Sedana\nNIM : 1808561071')
print('\nTugas Kriptoanalis\n')
hitung()
