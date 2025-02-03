from geometri import segitiga, persegip, persegi, jajar, trapesium, lingkaran, layang, kupat

nama = input('Masukkan nama Anda: ')

def main():
    print(f"Selamat Datang {nama} di Program Penghitung Keliling Bangun Datar")
    
    while True:
        print("\nPilih jenis perhitungan:")
        print("1. keliling Segitiga")
        print("2. keliling Persegi Panjang")
        print("3. keliling Persegi")
        print("4. keliling Jajar Genjang")
        print("5. keliling Trapesium")
        print("6. keliling Lingkaran")
        print("7. keliling Layang-layang")
        print("8. keliling Belah Ketupat")
        print("9. Keluar")
                        
        try:
            pilihan = int(input("Pilih jenis perhitungan (1-9): "))
        except ValueError:
            print("Masukkan angka yang valid antara 1-9.")
            continue

        if pilihan == 1:
            print(segitiga())
        elif pilihan == 2:
            print(persegip())
        elif pilihan == 3:
            print(persegi())
        elif pilihan == 4:
            print(jajar())
        elif pilihan == 5:
            print(trapesium())
        elif pilihan == 6:
            print(lingkaran())
        elif pilihan == 7:
            print(layang())
        elif pilihan == 8:
            print(kupat())
        elif pilihan == 9:
            print(f"Terima kasih {nama} telah menggunakan program ini.")
            break
        else:
            print(f"Mohon maaf {nama}, pilihan Anda tidak sesuai, silakan pilih 1-9.")
            continue

        while True:
            ulang = input("\nApakah Anda ingin mencoba lagi? (yes/no): ").lower()
            if ulang == 'yes':
                break 
            elif ulang == 'no':
                print(f"Terima kasih kepada {nama} yang sudah mencoba Project Sederhana saya.")
                return
            else:
                print("Jawaban tidak valid. Mohon masukkan 'yes' atau 'no'.")

if __name__ == "__main__":            
    main()