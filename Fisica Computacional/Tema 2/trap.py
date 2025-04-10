def trap(f, a, b, N):
    h = (b-a)/N
    I = h/2*(f(a)+f(b))
    for k in range(1,N):
        I+=h*f(a+k*h)
    return I

f = lambda x: x**4-2*x+1

print(trap(f,0,2,10))