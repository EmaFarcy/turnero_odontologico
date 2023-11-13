# Bradley N. Miller, David L. Ranum
# Solución de problemas con algoritmos y estructuras de datos usando Python
# Copyright 2014
# Correcciones Matias Bordone 2023
# abb.py

class ArbolBinarioBusqueda:

    def __init__(self): #constructor. Inicializa un árbol vacío. Representa el ABB en sí.
        self.raiz = None # referencia al nodo raíz. Como el árbol está vacío, la referencia es None.
        self.tamano = 0 # cantidad de nodos en el árbol. Como el árbol está vacío, el tamaño es 0.

#agrega y _agregar método para agregar un nuevo nodo al árbol. 
    def agregar(self,clave,valor): #método "agregar" que inicializa la inserción de un nuevo nodo en el árbol.
        if self.raiz: #si el árbol no está vacío, se llama al método "_agregar" para realizar la inserción.
            self._agregar(clave,valor,self.raiz)
        else: #si el árbol está vacío, se crea un nuevo nodo y se lo asigna a la raíz.
            self.raiz = NodoArbol(clave,valor) 
        self.tamano = self.tamano + 1

    def _agregar(self,clave,valor,nodoActual): #método "_agregar" (recursivo) que realiza la inserción de un nuevo nodo en el árbol.
        if clave < nodoActual.clave: #si la clave del nodo a insertar es menor a la clave del nodo actual, se inserta a la izquierda.
            if nodoActual.tieneHijoIzquierdo(): #si el nodo actual tiene hijo izquierdo, se llama al método "_agregar" para realizar la inserción.
                self._agregar(clave,valor,nodoActual.hijoIzquierdo) #se pasa como parámetro el hijo izquierdo del nodo actual.
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
 
    def __setitem__(self,c,v): #método especial para agregar un nuevo nodo al árbol.
        self.agregar(c,v) #se llama al método "agregar" para realizar la inserción.

    def obtener(self,clave): #método para obtener un nodo del árbol.
        if self.raiz: #si el árbol no está vacío, se llama al método "_obtener" para realizar la búsqueda.
            res = self._obtener(clave,self.raiz) #se pasa como parámetro la raíz del árbol.
            if res: #si se encuentra el nodo, se retorna la carga útil del nodo.
                return res.cargaUtil #se retorna la carga útil del nodo.
            else:
                return None #si no se encuentra el nodo, se retorna None.
        else:
            return None

    def _obtener(self,clave,nodoActual): #método "_obtener" (recursivo) que realiza la búsqueda de un nodo en el árbol.
        if not nodoActual: #si el nodo actual es None, se retorna None.
            return None #se retorna None.
        elif nodoActual.clave == clave: #si la clave del nodo actual es igual a la clave del nodo buscado, se retorna el nodo actual.
            return nodoActual #se retorna el nodo actual.
        elif clave < nodoActual.clave: #si la clave del nodo buscado es menor a la clave del nodo actual, se llama al método "_obtener" para realizar la búsqueda.
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)        

    def __getitem__(self,clave): #método especial para obtener un nodo del árbol.
        res = self.obtener(clave)  #se llama al método "obtener" para realizar la búsqueda.
        if res: #si se encuentra el nodo, se retorna la carga útil del nodo.
            return res
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __contains__(self,clave): #método especial para verificar si un nodo está en el árbol.
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False
       
    def longitud(self): #método para obtener la cantidad de nodos del árbol.
        return self.tamano

    def __len__(self): #método especial para obtener la cantidad de nodos del árbol.
        return self.tamano

    def __iter__(self): #método especial para iterar sobre el árbol.
        return self.raiz.__iter__()

    def eliminar(self,clave): #método para eliminar un nodo del árbol.
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave): #método especial para eliminar un nodo del árbol.
        self.eliminar(clave)

    def remover(self,nodoActual): #método para remover un nodo del árbol.
        if nodoActual.esHoja(): #hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos(): #interior
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil

        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)

    def inorden(self): #método para recorrer el árbol en orden.
        self._inorden(self.raiz)

    def _inorden(self,arbol): #método "_inorden" (recursivo) que recorre el árbol en orden.
        if arbol != None:
            self._inorden(arbol.hijoIzquierdo)
            print(arbol.cargaUtil)
            self._inorden(arbol.hijoDerecho)

    def postorden(self): #método para recorrer el árbol en postorden.
        self._postorden(self.raiz)

    def _postorden(self, arbol):
        if arbol:
            self._postorden(arbol.hijoDerecho)
            self._postorden(arbol.hijoIzquierdo)
            print(arbol.clave)            

    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self,arbol):
        if arbol:
            print(arbol.clave)            
            self._preorden(arbol.hijoIzquierdo)
            self._preorden(arbol.hijoDerecho)

class NodoArbol: #representa cada nodo en el árbol.
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave # Cada nodo tiene una clave, un valor y dos referencias a otros nodos.
        self.cargaUtil = valor # valor asociado (carga útil)
        self.hijoIzquierdo = izquierdo # referencia al hijo izquierdo
        self.hijoDerecho = derecho # referencia al hijo derecho
        self.padre = padre # referencia al padre
        self.factorEquilibrio = 0 #Balance del arbol. Se utiliza para el balanceo AVL

    def tieneHijoIzquierdo(self): #método para verificar si un nodo tiene hijo izquierdo.
        return self.hijoIzquierdo
       
    def tieneHijoDerecho(self): #método para verificar si un nodo tiene hijo derecho.
        return self.hijoDerecho

    def esHijoIzquierdo(self): #método para verificar si un nodo es hijo izquierdo.
        return self.padre and self.padre.hijoIzquierdo == self
    
    def esHijoDerecho(self): #método para verificar si un nodo es hijo derecho.
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self): #método para verificar si un nodo es la raíz.
        return not self.padre

    def esHoja(self): #método para verificar si un nodo es hoja.
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self): #método para verificar si un nodo tiene algún hijo.
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self): #método para verificar si un nodo tiene ambos hijos.
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder): #método para reemplazar la clave, el valor y los hijos de un nodo.
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self    

    def encontrarSucesor(self): #método para encontrar el sucesor de un nodo.
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self): #método para empalmar un nodo.
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem

if __name__ == "__main__": #test del árbol.
    miArbol = ArbolBinarioBusqueda()
    miArbol[3]="rojo"
    miArbol[4]="azul"
    miArbol[6]="amarillo"
    miArbol[2]="en"

    print(miArbol[6])
    print(miArbol[2])

    for i in miArbol:
        print (i)
    miArbol.inorden()