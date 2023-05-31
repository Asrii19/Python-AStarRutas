class Ciudad():
    def __init__(self, ciudad, g_x, h_x, ruta):
        self.ciudad = ciudad
        self.g_x = g_x
        self.h_x = h_x
        self.f_x = g_x + h_x
        self.ruta = ruta
    def __str__(self):
        return f"Ciudad: {self.ciudad}, g_x: {self.g_x}, h_x: {self.h_x}, f_x: {self.f_x}, ruta: {self.ruta}"
    