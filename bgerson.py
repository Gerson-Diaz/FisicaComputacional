def factorial(x):
    if x == 0:
        return 1
    i = x
    f = 1
    while i != 0:
        f = f*i
        i -= 1
    return f 

def catalan(n):
    if n == 0:
        return 1
        
    # Arrancamos con el valor de C_0
    c = 1
    
    # Calculamos los siguientes valores paso a paso hasta llegar a n
    for i in range(1, n + 1):
        # Multiplicamos primero y usamos división entera (//)
        c = (c * (4 * i - 2)) // (i + 1)
        
    return c

def maxdiv(m,n):
    #Si n llega a cero retornamos a m
    if n == 0:
        return m
    #si n > 0 llamamos de nuevo a la funcion pero con nuevos valores
    return maxdiv(n,m%n)