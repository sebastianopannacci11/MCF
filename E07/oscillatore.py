# Oscillatore
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def parse():
    parser = argparse.ArgumentParser(description='Opzioni di potenziale da analizzare')

    parser.add_argument('-V', '--potenziale', type=str, default='x6', choices=['x2', 'x4', 'x6', 'x3/2'], help='Tipo di potenziale che si può scegliere da analizzare (default: x6)')
    parser.add_argument('-c', '--confronto', type=str, nargs=2, default=['x2', 'x6'], choices=['x2', 'x4', 'x6', 'x3/2'], help='Due potenziali da confrontare nel secondo grafico (default: x2 x6)')
    parser.add_argument('-m', '--massa', type=float, default=1, help='Valore della massa (default: 1)')
    parser.add_argument('-k', '--costante', type=float, default=0.1, help='Valore della costante nel potenziale (default: 0.1)')

    return parser.parse_args()

def pot_1(k, x):
    return k * x**2

def pot_2(k, x):
    return k * x**4

def pot_3(k, x):
    return k * x**6

def pot_4(k, x):
    return k * (np.abs(x))**(3 / 2)

def periodo(massa, potenziale, k, x_0):
    '''
    Calcola il periodo di oscillazione per un potenziale speicifcato, in funzione di x_0.
    Parametri:
    - massa: massa della particella;
    - potenziale: funzione del potenziale V(x):
    - x_0: ampiezza massima dell'oscillazione.

    Restiuisce:
    - T: periodo di oscillazione.
    '''
    epsilon = 1e-10 * x_0 # epsilon per evitare la divisione per zero nell'integrale
    x = np.linspace(0, x_0 - epsilon, 10001) 
    integranda = 1 / (np.sqrt(potenziale(k, x_0) - potenziale(k, x)) + epsilon)
    return np.sqrt(8 * massa) * integrate.simpson(integranda, x=x)

if __name__ == '__main__':
    args = parse() # lettura degli argomenti dal terminale

    # Dizionario per mappare le opzioni di potenziale alle funzioni e alla relativa scrittura LaTeX
    pot = {
        'x2'    : (pot_1, r'$V(x) = k x^2$'),
        'x4'    : (pot_2, r'$V(x) = k x^4$'),
        'x6'    : (pot_3, r'$V(x) = k x^6$'),
        'x3/2'  : (pot_4, r'$V(x) = k |x|^{3/2}$')
    }

    # Dati per il potenziale
    x = np.linspace(-2, 2, 2000)

    # Dati per il periodo (ampiezze x_0 > 0)
    x_0 = np.linspace(0.1, 5, 1000)
    pot_scelto, label_pot = pot[args.potenziale]
    t = np.array([periodo(massa=args.massa, potenziale=pot_scelto, k=args.costante, x_0=amp) for amp in x_0])

    # Grafico del periodo in funzione di x_0
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    ax1.plot(x, pot_scelto(k=args.costante, x=x), label=f'Potenziale {label_pot}')
    ax2.plot(x_0, t, label='Periodo $T$ in funzione di $x_0$')

    # Formattazione grafico
    ax1.set_title('Potenziale')
    ax2.set_title('Periodo di oscillazione in funzione di $x_0$')
    ax1.set_xlabel('$x$')
    ax2.set_xlabel('$x_0$')
    ax1.set_ylabel('$V(x)$')
    ax2.set_ylabel('$T$')
    ax1.grid(True, alpha=0.3)
    ax2.grid(True, alpha=0.3)
    ax1.legend()
    ax2.legend()
    plt.tight_layout()

    # Mostro grafico
    plt.show()

    # Due grafici di periodo in funzione di x_0 per potenziali diversi
    # Dati per il potenziale
    x = np.linspace(-2, 2, 2000)
    
    # Dati per il periodo (ampiezze x_0 > 0)
    pot_c1, label_c1 = pot[args.confronto[0]]
    pot_c2, label_c2 = pot[args.confronto[1]]

    x_0_confronto = np.linspace(0.1, 5, 1000)

    t_pot1      = np.array([periodo(massa=args.massa, potenziale=pot_c1, k=args.costante, x_0=amp) for amp in x_0_confronto])
    t_pot2      = np.array([periodo(massa=args.massa, potenziale=pot_c2, k=args.costante, x_0=amp) for amp in x_0_confronto])

    # Grafico del periodo in funzione di x_0
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    
    ax1.plot(x, pot_c1(k=args.costante, x=x), color='navy', label=f'Potenziale 1: {label_c1}')
    ax1.plot(x, pot_c2(k=args.costante, x=x), color='darkorange', label=f'Potenziale 2: {label_c2}')
    ax2.plot(x_0_confronto, t_pot1, color='navy', label=f'Periodo $T$ per {label_c1}')
    ax2.plot(x_0_confronto, t_pot2, color='darkorange', label=f'Periodo $T$ per {label_c2}')

    # Formattazione grafico
    ax1.set_title('Potenziale')
    ax2.set_title('Periodo di oscillazione in funzione di $x_0$')
    ax1.set_xlabel('$x$')
    ax2.set_xlabel('$x_0$')
    ax1.set_ylabel('$V(x)$')
    ax2.set_ylabel('$T$')
    ax1.grid(True, alpha=0.3)
    ax2.grid(True, alpha=0.3)
    ax1.legend()
    ax2.legend()
    plt.tight_layout()

    # Mostro grafico
    plt.show()