import datetime

file_eventi = open("eventi.csv", "r")

conteggio = {
    "rosso" : 0,
    "verde" : 0,
    "blu" : 0
}

timestamps = []

with open("eventi.csv", "r") as file_eventi:
    
    next(file_eventi)
    
    for line in file_eventi:
        line = line.strip()
        if line == "":
            continue
        
        dati = line.split(",")
        
        timestamps.append(dati[0])
        conteggio[dati[2]] += 1
        
print("Conteggio LED:")
for colore in conteggio:
    print(colore, conteggio[colore])
    
primo = datetime.datetime.strptime(timestamps[0], "%Y-%m-%d %H:%M:%S")
ultimo = datetime.datetime.strptime(timestamps[-1], "%Y-%m-%d %H:%M:%S")

durata = ultimo - primo

print("Primo evento:", primo)
print("Ultimo evento:", ultimo)
print("Durata totale:", durata)