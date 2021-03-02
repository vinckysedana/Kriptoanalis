#Program cek bilangan prima
def prima(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "bukan bilangan prima\n\n")
                break
        else:
            print(num,"adalah bilangan prima\n\n")
    else:
        print(num, "bukan bilangan prima\n\n")

#Program mencari nilai faktorial
def faktorial(f):
    hasil = 1
    for i in range(2, f+1):
        hasil *= i
    return hasil

#Program menemukan FPB dua buah bilangan
def hitung_FPB(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
            
    return fpb
def ulang():
    ul= str(input("Apakah Anda Ingin Kembali Ke Menu Awal ? (Y/N) : "))
    if (ul=="Y" or ul=="y"):
        main()
    else:
        return 0
def main():
    print("Nama:Kadek Vincky Sedana\nNIM:1808561071\n\nTugas Kriptoanalis")
    print("1.Cek Bilangan Prima\n2.Mencari Nilai Faktorial\n3.Mencari Nilai FPB 2 Bilangan")
    pil=int(input("Masukkan Pilihan :"))
    if pil==1:
        num = int(input("Masukkan bilangan: "))
        prima(num)
        ulang()
    elif pil==2:
        n = int(input("Masukkan bilangan: "))
        print("Nilai Faktorial dari", n, "=", faktorial(n))
        print("\n\n")
        ulang()
    elif pil==3:
        num1 = int(input("Masukkan Bilangan Pertama: "))
        num2 = int(input("Masukkan Bilangan Kedua: "))
        print("FPB dari", num1,"dan", num2,"=", hitung_FPB(num1, num2))
        print("\n")
        ulang()
    else:
        print("Inputan Salah\n\n")
        main()

main()
