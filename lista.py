class Nodo:
    def __init__(self,elemento):
        self.elemento = elemento
        self.siguiente = None



class Lista:
    
    def __init__(self):
        self.prim = None
        self.ult = None
        self.tamanio = 0

    def insertar(self,elemento):

        nuevo_nodo = Nodo(elemento)
        if self.tamanio ==0 : 
            self.prim = nuevo_nodo
            self.ult = self.prim
        else:
            self.ult.siguiente = nuevo_nodo
            self.ult= nuevo_nodo
        self.tamanio+=1
    def __obtener_nodo(self,posicion):
        if (posicion>= self.tamanio or (-posicion<= -self.tamanio)): raise IndexError("Lista fuera de rango")

        if posicion<0 : posicion=posicion*-1
        elemento_actual = self.prim
        while(posicion>0):
            elemento_actual=elemento_actual.siguiente
            posicion-=1
        return elemento_actual
    def __obtener(self,posicion):
        return self.__obtener_nodo(posicion).elemento

    def __iter__(self):
        actual = self.prim
        while actual:
            yield actual.elemento
            actual = actual.siguiente
    
    def __getitem__(self,n):
        return self.__obtener(n)

    

    def __setitem__(self,posicion,elemento):
        self.__obtener_nodo(posicion).elemento=elemento





