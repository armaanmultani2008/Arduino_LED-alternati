import csv
from datetime import datetime
import dearpygui.dearpygui as dpg
 
file_csv = "eventi.csv"
 
def get_data():
    conteggio_led = {}
    primo_timestamp = None
    ultimo_timestamp = None
 
    with open(file_csv, "r") as file_eventi:
        buffer = csv.reader(file_eventi)
 
        for riga in buffer:
            if len(riga) != 3:
                continue
 
            timestamp_str, evento, led = riga
 
            conteggio_led[led] = conteggio_led.get(led, 0) + 1
 
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            if primo_timestamp is None:
                primo_timestamp = timestamp
            ultimo_timestamp = timestamp
 
    durata = None
    if primo_timestamp and ultimo_timestamp:
        durata = ultimo_timestamp - primo_timestamp
 
    return conteggio_led, primo_timestamp, ultimo_timestamp, durata
 
 
def aggiorna_gui():
    conteggio_led, primo_timestamp, ultimo_timestamp, durata = get_data()
 
    dpg.set_value("txt_primo", str(primo_timestamp))
    dpg.set_value("txt_ultimo", str(ultimo_timestamp))
    dpg.set_value("txt_durata", str(durata))
 
    label = list(conteggio_led.keys())
    valori = list(conteggio_led.values())
 
    indici = list(range(len(label)))
 
    dpg.configure_item("bar_series", x=indici, y=valori)
 
    ticks = [(i, label[i]) for i in range(len(label))]
    dpg.set_axis_ticks("x_axis", ticks)
 
dpg.create_context()
 
with dpg.window(label="Statistiche LED", width=600, height=700):
 
    dpg.add_text("Primo evento:")
    dpg.add_text("", tag="txt_primo")
 
    dpg.add_text("Ultimo evento:")
    dpg.add_text("", tag="txt_ultimo")
 
    dpg.add_text("Tempo totale:")
    dpg.add_text("", tag="txt_totale")
 
    with dpg.plot(label="Conteggio LED", height=300, width=400):
        dpg.add_plot_axis(dpg.mvXAxis, label="LED", tag="x_axis")
        dpg.add_plot_axis(dpg.mvYAxis, label="Conteggio", tag="y_axis")
 
        dpg.add_bar_series([], [], parent="y_axis", tag="bar_series")
 
    dpg.add_button(label="Aggiorna", callback=lambda: aggiorna_gui())
 
 
dpg.create_viewport(title="Dashboard LED", width=600, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()