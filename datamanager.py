# datamanager.py
import time
import threading
import random
from ej1 import EventManager

#Clase con datos iniciales
class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        # Inicializacion de actualizaciones en tiempo real
        while True:
            time.sleep(3)
            self.generate_real_time_data()
            self.event_manager.notify("datos_actualizados", self.data)

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

if __name__ == "__main__":
    real_time_data_manager = RealTimeDataManager()

    # Función lambda para el callback
    real_time_data_manager.event_manager.subscribe("datos_actualizados", lambda data: print("Datos en tiempo real actualizados:", data))

    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
        