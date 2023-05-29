class Ciudad():
    def __init__(self, ciudad, g_x, h_x, ruta):
        self.ciudad = ciudad
        self.g_x = g_x
        self.h_x = h_x
        self.f_x = g_x + h_x
        self.ruta = ruta
    