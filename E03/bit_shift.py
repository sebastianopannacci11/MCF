# bit shift di un numero

# Richiedo un numero naturale
while True:
    try:
        N = int(input("Inserire un numero naturale: "))
        if N >= 0:
            break
        else:
            print("Errore: inserire un numero naturale.")
    except ValueError:
        print("Errore: inserire un numero naturale.")

# Richiedo il numero di posizioni da shiftare
while True:
    try:
        M = int(input("Inserire il numero di posizioni da shiftare: "))
        if M >= 0:
            break
        else:
            print("Errore: inserire un numero naturale.")
    except ValueError:
        print("Errore: inserire un numero naturale.")

print('\n')
print('{:^10s} {:^10s} {:^10s} {:^10s}'.format('Numero','Decimale', 'Binario', 'Esadecimale'))
print('---------------------------------------')
print('{:^10s} {:^10d} {:>010b} {:^10x}'.format('N', N, N, N))
print('{:^10s} {:^10d} {:>010b} {:^10x}'.format('N << M', N << M, N << M, N << M))
print('{:^10s} {:^10d} {:>010b} {:^10x}'.format('N >> M', N >> M, N >> M, N >> M))