from datetime import datetime
while True:
    try:
        data_stringa = input("Inserire la propria data di nascita (formato: gg-mm-aaaa hh:mm:ss): ")
        data_nascita = datetime.strptime(data_stringa, "%d-%m-%Y %H:%M:%S")
        break
    except ValueError:
        print("Errore: formato non valido. Assicurarsi di usare gg-mm-aaaa hh:mm:ss.")

data_nascita = datetime.strptime(data_stringa, "%d-%m-%Y %H:%M:%S")
data_attuale = datetime.now()
diff_tempo = data_attuale - data_nascita

anni = int(diff_tempo.days / 365.25)
giorni = diff_tempo.days
secondi = int(diff_tempo.total_seconds())

eta = {'Anni' : anni, 'Giorni' : giorni, 'Secondi' : secondi}

# Età in anni, giorni, secondi
for dato in eta:
    print('{: <10} {:d}'.format(dato, eta[dato]))