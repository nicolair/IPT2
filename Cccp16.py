def eval_sm(x,y,t):
    r = (x**2 + y**2)**(-1.5)
    xsv = x -rv*cos(Omega*t + Phi)
    ysv = y -rv*sin(Omega*t + Phi)
    dv = (xsv**2 + ysv**2)**(-1.5)
    Sx = -Gms*x*r - Gmv*xsv*dv
    Sy = -Gms*y*r - Gmv*ysv*dv
    return Sx,Sy
    
# les variables suivantes sont connues    
# deltaT (flottant) 
# n entier
# x0 y0 (pos) u0 v0 (vit) ini flottants
x = [x0]
y = [y0]
u = [u0]
v = [v0]
t = [0.]


for i in range(n):
    Sx , Sy = eval_sm(x[i],y[i],t[i])
    x.append(x[i] + deltaT*u[i])
    y.append(y[i] + deltaT*v[i])
    u.append(u[i] + deltaT*Sx)
    v.append(v[i] + deltaT*Sy)
    t.append(t+deltaT)
# dans le cadre d'une procédure
# return x,y,u,v,t

import matplotlib.pyplot as plt
def vitesse_sonde(u,v,t):
    normeV = []
    for i in range(len(u)):
        #convertir en km/s
        normeV.append(0.001*(u[i]**2+v[i]**2)**0.5)
        plt.plot(t,normeV)
        xlabel('Temps en s')
        ylabel('Norme vitesse en km/s')
        title('Evolution norme vitesse')
