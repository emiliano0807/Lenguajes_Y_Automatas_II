class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos  
        self.padre = None
        self.costo = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos 
        if self.hijos != None:
            for h in hijos:
                h.padre = self

    def get_hijos(self):
        return self.hijos #Aqui se cambio de padres a hijos

# Se agrego get datos
    def get_datos(self):
        return self.datos

# Aqui se agrego get_padre
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def set_costo(self, costo):
        self.costo = costo

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def __str__(self):
        return str(self.get_datos())
    
    #def nodo(self):
        #return self.nodo