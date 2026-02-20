import serial
import datetime

ser = serial.Serial("COM7", 9600)

numero_evento = 0

with open("eventi.csv", "w") as file_eventi:
    
    file_eventi.write("Timestamp,Numero_evento,Colore_LED")
    
    while True:
        data = ser.readline().decode("utf-8").strip()
        
        if data in ["rosso", "verde", "blu"]:
            
            numero_evento += 1
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            file_eventi.write(f"{timestamp},{numero_evento},{data}\n")
            file_eventi.flush()
            
            print(f"Registrato evento {numero_evento} - {data}")