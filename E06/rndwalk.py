# Modulo python per un Random Walk
import numpy as np
def random_walk(s, n):
    """
    Simula un Random Walk in 2D con n passi di lunghezza s.
    s: lunghezza del passo
    n: numero di passi
    returns: array con lo spostamento rispetto all'origine dopo n passi
    """
    delta_x = np.array([0])
    delta_y = np.array([0])
    tmpx = 0
    tmpy = 0
    phi = np.random.uniform(0, 2*np.pi, n) # angoli casuali
    
    for p in phi:
        tmpx = tmpx + s * np.cos(p)
        tmpy = tmpy + s * np.sin(p)
        delta_x = np.append(delta_x, tmpx)
        delta_y = np.append(delta_y, tmpy)
    return delta_x, delta_y