import math

# Memeriksa inputan user
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            # Jika input angka negatif
            if value < 0:
                print("Maaf, sebuah ukuran tidak mungkin negatif, silakan ulangi lagi.")
            # Jika input angka nol
            elif value == 0:
                print("Ukuran tidak boleh bernilai 0, silakan ulangi.")
            else:
                return value
        # Jika inputan bukan angka
        except ValueError:
            print("Maaf, yang Anda masukkan bukan angka bilangan bulat/desimal. Silakan ulangi lagi.")

# Keliling segitiga
def segitiga():
    sisi1 = get_float('Masukkan ukuran sisi pertama: ')
    sisi2 = get_float('Masukkan ukuran sisi kedua: ')
    sisi3 = get_float('Masukkan ukuran sisi ketiga: ')
    keliling = sisi1 + sisi2 + sisi3
    return f'Keliling segitiga dengan ukuran sisi pertama {sisi1} cm, sisi kedua {sisi2} cm, dan sisi ketiga {sisi3} cm, adalah {keliling:,} cm'

# Keliling persegi panjang
def persegip():
    panjang = get_float('Masukkan ukuran panjang: ')
    lebar = get_float('Masukkan ukuran lebar: ')
    keliling = 2 * (panjang + lebar)
    return f'Keliling persegi panjang dengan ukuran panjang {panjang} cm, dan lebar {lebar} cm adalah {keliling:,} cm'

# Keliling persegi
def persegi():
    sisi = get_float('Masukkan ukuran sisi: ')
    keliling = 4 * sisi
    return f'Keliling persegi dengan ukuran sisi {sisi} cm, adalah {keliling:,} cm'

# Keliling jajar genjang
def jajar():
    alas = get_float('Masukkan ukuran alas: ')
    sisi_miring = get_float('Masukkan ukuran sisi miring: ')
    keliling = 2 * (alas + sisi_miring)
    return f'Keliling jajar genjang dengan ukuran alas {alas} cm, dan sisi miring {sisi_miring} cm adalah  {keliling:,} cm'

# Keliling trapesium
def trapesium():
    sisi1 = get_float('Masukkan ukuran sisi pertama: ')
    sisi2 = get_float('Masukkan ukuran sisi kedua: ')
    sisi3 = get_float('Masukkan ukuran sisi ketiga: ')
    sisi4 = get_float('Masukkan ukuran sisi keempat: ')
    keliling = sisi1 + sisi2 + sisi3 + sisi4
    return f'Keliling trapesium dengan ukuran sisi pertama {sisi1} cm, sisi kedua {sisi2} cm, sisi ketiga {sisi3}, dan sisi keempat {sisi4} cm adalah {keliling:,} cm'

# Keliling lingkaran
def lingkaran():
    r = get_float('Masukkan ukuran jari-jari: ')
    keliling = 2 * math.pi * r
    return f'Keliling lingkaran dengan ukuran jari-jari {r} cm adalah {keliling:,.2f} cm'

# Keliling layang-layang
def layang():
    sisi1 = get_float('Masukkan ukuran sisi pertama: ')
    sisi2 = get_float('Masukkan ukuran sisi kedua: ')
    keliling = 2 * (sisi1 + sisi2)
    return f'Keliling layang-layang dengan ukuran sisi pertama {sisi1} cm, dan sisi kedua {sisi2} cm adalah {keliling:,} cm'

# Keliling belah ketupat
def kupat():
    sisi = get_float('Masukkan ukuran sisi: ')
    keliling = 4 * sisi
    return f'Keliling belah ketupat dengan ukuran sisi {sisi} cm adalah {keliling:,} cm'