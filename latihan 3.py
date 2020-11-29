print("------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("------------------------")

angka = 0
sum = 0

while True:
    try :
        bilBulat = int(input('Masukan bilangan bulat : '))
        sum += bilBulat
        angka += 1
        lagi = input('lagi(y/n)? ')
        if(lagi == 'n'):
            break
        else:
            print('Input tidak valid')
    except ValueError :
        print('bukan bilangan bulat')
        continue

rerata = sum/angka
print('rata - ratanya adalah : ', rerata)
