# Lista

# Lista dei gironi della settimana
settimana = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

# Nomi dei giorni di ottobre 2026
prima_settimana = ['Giovedì', 'Venerdì', 'Sabato', 'Domenica']
ultima_settimana = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato']
ottobre_2026 = prima_settimana + 3 * settimana + ultima_settimana

# Dizionario dei giorni di ottobre 2026 con le date
date_ottobre_2026 = {i + 1: ottobre_2026[i] for i in range(len(ottobre_2026))}

print("Giorni della settimana: ", settimana, "\n")
print("Giorni di ottobre 2026: ", ottobre_2026, "\n")
print("Date di ottobre 2026: ", date_ottobre_2026, "\n")