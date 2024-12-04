import ctypes

class LaserLibrary:
    def __init__(self):
        # Cargar la biblioteca de C proporcionada por FARO
        self.lib = ctypes.CDLL('path/to/faro_library.dll')

        # Definir las funciones de la biblioteca
        self.lib.ConnectLaserTracker.argtypes = []
        self.lib.ConnectLaserTracker.restype = ctypes.c_int

        self.lib.MoveLaserTracker.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
        self.lib.MoveLaserTracker.restype = ctypes.c_int

        self.lib.DisconnectLaserTracker.argtypes = []
        self.lib.DisconnectLaserTracker.restype = ctypes.c_int

    def conectar_laser_tracker(self):
        result = self.lib.ConnectLaserTracker()
        if result == 0:
            print("Laser tracker conectado")
        else:
            print("Error al conectar el laser tracker")

    def mover_laser_tracker(self, x, y, z):
        result = self.lib.MoveLaserTracker(ctypes.c_double(x), ctypes.c_double(y), ctypes.c_double(z))
        if result == 0:
            print(f"Moviendo el laser tracker a las coordenadas ({x}, {y}, {z})")
        else:
            print("Error al mover el laser tracker")

    def desconectar_laser_tracker(self):
        result = self.lib.DisconnectLaserTracker()
        if result == 0:
            print("Laser tracker desconectado")
        else:
            print("Error al desconectar el laser tracker")