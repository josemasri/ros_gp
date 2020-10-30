from numpy import array
from random import randint, uniform,random

vel = array ([0,0.5,1,1.5,2])
dist = array ([0.5,1,1.5,2,2.5,3])
listd = []
listv = []
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
      return not (self.der or self.izq or self.ope)

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
   def sorteo(tam,arreglo):
       rd=random.randint(0,tam-1)
       if rd not in arreglo: 
            arreglo.append(rd)
            return rd
       elif len(arreglo)<5:
            rd=sorteo(tam,arreglo)
       else: 
            bandera=True
            return "Error"


def _agregar(self,valor,nivel):
   # Método de árbol con crecimiento acotado (Grow method).
   #Crear nodos de cualquier conjunto (funciones o terminales) si aún no se alcanza la profundidad máxima.
   #En otro caso, tomar solamente terminales.

    if (self.tamano<tamMax):
        if ((valor ==  "<" )or(valor == ">")):
                 self._agregar(valor,nodoActual.ope)
                 var = "d"
                 var2 = var+valor
                 ind=sorteo(6,listd)
                 if (ind == "Error"):
                    
                 else:
                    var3 = var2+dist[ind]
                    self.dato= var3 
                    
                    
                
        elif self.tieneIzq():
                 self._agregar(valor,nodoActual.der)
                 var = "v"
                 var2 = var+valor
                 ind=sorteo(6,listv)
                 if (ind == "Error"):
                    
                 else:
                     var3 = var2+vel[ind]
                     self.dato= var3
        else:
                 self._agregar(valor,nodoActual.izq)
                 var = "v"
                 var2 = var+valor
                ind=sorteo(6,listv)
                 if (ind == "Error"):
                    
                 else:
                    var3 = var2+vel[ind]
                    self.dato= var3
else:
        if self.tieneIzq():
                 self._agregar(valor,nodoActual.der)
                  var = "v"
                 var2 = var+valor
                ind=sorteo(6,listv)
                 if (ind == "Error"):
                    
                 else:
                    var3 = var2+vel[ind]
                    self.dato= var3
        else:
                 self._agregar(valor,nodoActual.izq)
                  var = "v"
                 var2 = var+valor
                ind=sorteo(6,listv)
                 if (ind == "Error"):
                    
                 else:
                    var3 = var2+vel[ind]
                    self.dato= var3
def _recPreorden(self,valor,nivel):
