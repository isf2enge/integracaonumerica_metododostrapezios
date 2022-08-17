"""""
Programa 
"""""
def f(x): #função criada,para identificar o máximo e mínimo,e realizar o processo de iteração.

    return 4*x+1 #Digite sua função aqui


def resultado(a,b): #Função processual
    n = 100 #Número de divisões do trapézio
    d = (b-a)/n
    a_s = 0
    a_i = 0
    x = a
    while(x<b):
        g = f(x)
        r = f(x+d)
        a_s += d*max([g,r])
        a_i += d*min([g,r])
        x += d
    return((a_s+a_i)*0.5) #retorna a soma da interpolação,e dá o resultado.

print(resultado(0,2))   #Digite os intervalos