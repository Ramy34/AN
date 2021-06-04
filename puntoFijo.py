#Método de punto fijo para el problema 8
import math #Importamos la libreria math para hacer uso de las funciones trigonometricas

def g(x): #Definición de la función de la forma que la pide el método g(x)=x
    y=math.sqrt(2)*math.sin(x)
    return y

#Inicializamos las variables
p0=0.1 #Valor del punto 0
tol=0.0001 #Tolerancia/error minimo para terminar el método
n0=50 #Número de iteraciones
i=0 #Indice del iterador

while i<=n0: #Iniciamos las iteraciones
    p=g(p0) #Evaluamos el punto 0 en la función
    if abs(p-p0)<tol: #Comprueba el error que hay
        print("El punto fijo es ",p," despues de ",i," iteraciones")
        break #Imprime y termina el ciclo en caso de que el error sea menor al establecido
    i=i+1
    p0=p
if i>n0:
    print("El metodo no converge ")