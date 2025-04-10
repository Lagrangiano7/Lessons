def simpson(f, a, b, N):
    if N%2!=0:
        print("N debe ser par")
        return
    h = (b-a)/N
    I = (f(a)+f(b))
    for k in range(1, N//2): # Llego solo hasta N/2-1 (me quedo corto en 1 término de la primera sumatoria) y luego se lo añado
        I+=4*f(a+(2*k-1)*h)+2*f(a+2*k*h)
    I+=4*f(b-h)
    I=h*I/3
    return I

f = lambda x: x**4-2*x+1
I = simpson(f,0,2,10)