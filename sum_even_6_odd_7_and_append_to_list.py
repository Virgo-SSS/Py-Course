angka = [1900]

def tambah_angka(angka):
    angka_baru = angka

    i = True
    while i:
        jumlah_angka = len(angka_baru) -1
        if jumlah_angka % 2 == 0:
            angka_baru.append(angka_baru[jumlah_angka] + 6)
        else:
            angka_baru.append(angka_baru[jumlah_angka] + 7)

        if angka_baru[jumlah_angka] > 2500:
            i = False
    return angka_baru 

print(tambah_angka(angka))