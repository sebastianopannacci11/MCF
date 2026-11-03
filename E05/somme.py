# Modulo con funzioni somma
import math

def somma(n):
    """
    Funzione che calcola la somma dei primi n numeri naturali.

    Parametri:
        n: numero naturale fino al quale calcolare la somma.
    Ritorna:
        somma dei primi n numeri naturali.
    """
    s = 0
    for i in range(n + 1):
        s += i
    return s

# Funzione somma delle radici quadrate dei primi n numeri naturali
def somma_radici(n):
    """
        Funzione che calcola la somma delle radici quadrate dei primi n numeri naturali.
    
        Parametri:
            n: numero naturale fino al quale calcolare la somma.
        Ritorna:
            somma delle radici quadrate dei primi n numeri naturali.
    """
    s = 0
    for i in range(n + 1):
        s += math.sqrt(i)
    return s

# Update del file somme per aggiunta di nuove funzioni
# Funzione somma e prodotto dei primi n numeri naturali
def somma_prodotto(n):
    """
            Funzione che calcola la somma e il prodotto dei primi n numeri naturali.
        
            Parametri:
                n: numero naturale fino al quale calcolare la somma e il prodotto.
            Ritorna:
                somma e prodotto dei primi n numeri naturali.
    """
    s = 0
    p = 1
    for i in range(1, n + 1):
        s += i
        p *= i 
    return s, p

# Funzione somma dei primi n naturali alla potenza alpha (di default alpha=1)
def somma_potenza(n, alpha=1):
    """
            Funzione che calcola la somma dei primi n numeri naturali.
        
            Parametri:
                n: numero naturale fino al quale calcolare la somma.
                alpha: esponente alla quale elevare i numeri naturali.
            Ritorna:
                somma dei primi n numeri naturali elevati alla potenza alpha.
    """
    s = 0 
    for i in range(n + 1):
        s += i**alpha
    return s