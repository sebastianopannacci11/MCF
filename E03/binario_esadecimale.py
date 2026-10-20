# Numeri in binario e esadecimale e AND, OR tra i numeri

while True:
    try:
        N = int(input("Inserire un numero naturale: "))
        if N >= 0:
            break
        else:
            print("Errore: inserire un numero naturale.")
    except ValueError:
        print("Errore: inserire un numero naturale.")

while True:
    try:
        M = int(input("Inserire un numero naturale: "))
        if N >= 0:
            break
        else:
            print("Errore: inserire un numero naturale.")
    except ValueError:
        print("Errore: inserire un numero naturale.")

# Stampo i numeri N e M in decimale, binario e esadecimale, lo stesso per i valori OR e AND tra i due numeri

print('\n')
print('{:^10s} {:^10s} {:^10s} {:^10s}'.format('Numero','Decimale', 'Binario', 'Esadecimale'))
print('---------------------------------------')
print('{:^10s} {:^10d} {:>010b} {:^10x}'.format('N', N, N, N))
print('{:^10s} {:^10d} {:>010b} {:^10x}'.format('M', M, M, M))
print('---------------------------------------')
print('{:^10s} {:^10d} {:>010b} {:^10x}'.format('N OR M', N | M, N | M, N | M))
print('{:^10s} {:^10d} {:>010b} {:^10x}'.format('N AND M', N & M, N & M, N & M))