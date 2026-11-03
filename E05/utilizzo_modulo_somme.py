# Script per testare il modulo somme.py
import somme

# Somma dei primi n numeri naturali
N = int(input("Inserire un numero naturale N, per calcolare la somma dei primi numeri naturali fino a N (incluso): "))

s = somme.somma(N)

print(f"La somma dei primi {N} numeri naturali è: {s}")

# Somma delle radici quadrate dei primi n numeri naturali

N = int(input("Inserire un numero naturale N, per calcolare la somma delle radici quadrate dei primi numeri naturali fino a N (incluso): "))

s_r = somme.somma_radici(N)

print(f"La somma delle radici quadrate dei primi {N} numeri naturali è: {s_r}")

# Somma e prodotto dei primi n numeri naturali

N = int(input("Inserire un numero naturale N, per calcolare la somma e il prodotto dei primi numeri naturali fino a N (incluso): "))

s, p = somme.somma_prodotto(N)

print(f"La somma dei primi {N} numeri naturali è: {s}")
print(f"Il prodotto dei primi {N} numeri naturali è: {p}")

# Somma dei primi n numeri naturali alla potenza alpha

N = int(input("Inserire un numero naturale N, per calcolare la somma dei primi numeri naturali fino a N (incluso): "))

risposta = ""
while risposta not in ["y", "n"]:
    risposta = input(f"{"Inserire la potenza?"} [y/n]: ").strip().lower()
if risposta == "y":
    alpha = int(input("Inserire il valore di alpha: "))
s_a = somme.somma_potenza(N, alpha)

print(f"La somma dei primi {N} numeri naturali alla potenza {alpha} è: {s_a}")