# Funzione che calcola la somma dei primi n numeri naturali
while True:
    try:
        N = int(input("Inserire un numero naturale: "))
        if N >= 0:
            break
        else:
            print("Errore: inserire un numero naturale.")
    except ValueError:
        print("Errore: inserire un numero naturale.")

def somma(n):
    somma = 0
    for i in range(n + 1):
        somma = somma + i
    return somma

print(f"La somma dei primi {N} numeri naturali è: ", somma(N))