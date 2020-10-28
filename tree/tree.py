mport numpy

class NodoArbol(object):
  def __init__(self):
    self.raiz = None
    self.ope = None         # Operador
    self.der = None	     	# Rama derecha del árbol
    self.izq  = None		# Rama izquierda del árbol
    self.dato  = None		# Dato del nodo del árbol
  def tieneOpe(self):
      return self.ope
  def tieneDer(self):
      return self.der
  def tieneIzq(self):
      return self.izq   
  def esRaiz(self):
      return not self.raiz
  def esOp(self):
      return not self.ope and self.raiz.ope == self
  def esIzq(self):
      return not self.izq and self.raiz.izq == self
  def esDer(self):
      return not self.der and self.raiz.der == self
  def esHoja(self):
      return not (self.hijoDerecho or self.hijoIzquierdo)

  def tieneAlgunHijo(self):
      return self.izq or self.izq

  def tieneTodosHijos(self):
      return self.der and self.izq and self.ope

  def reemplazarDatoDeNodo(self,valor,hope,hizq,hder):
        
        self.dato = valor
        self.izq = hizq
        self.der = hder
        self.ope = hope
        if self.tieneOpe():
            self.ope.raiz = self
        if self.tieneIzq():
            self.izq.raiz = self
        if self.tieneDer():
            self.der.raiz = self

  def agregar(self, valor):
    if self.raiz:
        self._agregar(valor,self.raiz)
    else:
        self.raiz = NodoArbol(valor)
    self.tamano = self.tamano + 1

def _agregar(self,valor,nivel):
    if (self.tamano<tamMax):
        if  (valor == ):
            if nodoActual.tieneIzq():
                self._agregar(valor,nodoActual.hIzq)
            else:
                nodoActual.Izq = NodoArbol(valor,raiz=nodoActual)
        else:
            if nodoActual.tieneDer():
                self._agregar(clave,valor,nodoActualhDer)
            else:
                nodoActual.Der = NodoArbol(valor,padre=nodoActual)
    
def _recPreorden(self,valor,nivel):
    if ()
