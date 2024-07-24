import math
G = 6.6743E-11 #constante de gravitacion universal
Mt = 5.972E24 #Masa de la tierra
rt = 6.371E6  #radio de la tierra
h = 6.62E-34 #Constante de planck
c = 3E8 #Velocidad de la luz en el vacio
g=9.81 #aceleracion de la gravedad en la superficie terrestre
def height_ball(v,t):
    """
    Funcion que calcula la altura de una bola en movimiento vertical.
    Argumentos:
    #velocidad inicial v
    #tiempo t
    #aceleracion de la gravedad g = 9.81 m/s^2
    """
    if v>=0 and t>=0 and t<= 2*v/g:
        y = v*t -0.5*g*t**2
        return y
    else:
        raise ValueError("Parece que no ingreso numeros adecuados")

def time_ball(v,y,g=9.81):
    """
    Funcion que calcula los tiempos en el que una bola con velocidad inicial v lanzada al aire alcanza un altura y en movimiento vertical.
    La funcion devuelve una tupla de dos elementos que son los 2 tiempos.
    Argumentos:
    #velocidad inicial v
    #altura y
    #aceleracion de la gravedad g = 9.81 m/s^2
    """
    assert(v>=0)
    t1 = (v - math.sqrt(v**2- 2*g*y))/g
    t2 = (v + math.sqrt(v**2- 2*g*y))/g
    if t1>=0 and t2>=0:
        return (t1,t2)
    else:
        return

def vel_escape_tierra():
    """
    Calcula la velocidad de escape de la tierra
    G = 6.6743E-11 #constante de gravitacion universal
    Mt = 5.972E24 #Masa de la tierra
    rt = 6.371E6  #radio de la tierra
    """
    v = math.sqrt(2*G*Mt/rt)
    return v

def vel_escape(x,y):
    v = math.sqrt(2*G*x/y)
    return v
