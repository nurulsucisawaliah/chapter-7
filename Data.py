# membuka dan mau membaca file d:/Data.txt
try:
    file = open("c:/data.txt", "r")
except FileNotFoundError :
    print('file tidak ditemukan')

# baca baris pertama dari file
# simpan kedalam variabel bil1 sbg integer
try:
    bil1 = int(file.readline())
    bil2 = int(file.readline())

#hitung dan tampilkan hasil bagi
    hasil = bil1/ bil2
    print(bil1, 'dibagi ',bil2, ' sama dengan ',hasil)
except :
    print('Tidak boleh pembagian dengan nol')
