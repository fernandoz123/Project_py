import math
def heron(t1): #Calcular el area del triangulo con el teorema de heron
    p = sum(t1) #perimetro del triangulo
    area = math.sqrt((p-t1[0])*(p-t1[1])*(p-t1[2])) #area del triangulo
    area = round(area,2) #resultado con 2 decimales
    return area

def es_primo(num):
    if num >=2:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    else:
        return False

