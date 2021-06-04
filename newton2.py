#Método de Newton-Raphson para el problema 12
def f(x): #Definimos la función
    y= (1-0.6*x)/x
    return y

def fp(x): #La primer derivada de la función
    y = -1/x**2
    return y

def fpp(x): #La segunda derivada de la función
    y = 2/x**3
    return y

def newton(x): #Formula del método
    N = x-f(x)/fp(x)
    return N

def convergencia(x): #Comprobar convergencia
    y = abs((f(x) * fpp(x))/ fp(x)**2)
    return y

#Inicializamos las variables
p0=1 #Valor del punto 0
tol=0.01 #Tolerancia/error minimo para terminar el método
n0=50 #Número de iteraciones
i=0 #Indice del iterador

if convergencia(p0) < 1: #Comprueba que la función converga
    while i<=n0: #Inician las iteraciones
        p=newton(p0) #Evalua con la ecuacion de Newton con el punto 0
        if abs(p-p0)<tol: #Comprueba el error que hay
                print("La solucion es ",p," despues de ",i," iteraciones")
                break #Imprime y termina el ciclo en caso de que el error sea menor al establecido
        i=i+1
        p0=p #Asigna como nuevo valor de p0 al resultado de la evaluación
else:
    print("No converge")