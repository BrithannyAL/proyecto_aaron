class Estudiantes():
    nombre_completo = None
    cedula = None
    hora = None
    fecha = None
    sig = None
    ant = None
    
    def __init__(self, n, c, h, f):
        self.nombre_completo = n
        self.cedula = c
        self.hora = h
        self.fecha = f
        
    def insertar (self, ne):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig = ne
        ne.ant = puntero
        
gente = Estudiantes("Aarón Ugalde", 208600582, " ", " ")