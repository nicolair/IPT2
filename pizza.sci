// supprimer les variables
clear()
//effacer la fenêtre graphique
clf()

// noter les deux paramètres globaux k et cste
function [y]= Aire(theta)
  y = theta - k*sin(theta) - cste;
endfunction

function [y]=inversAire(cste)
    y = fsolve(cste,Aire)
endfunction

k = 0.5;
pas = 0.1

I = 0:pas:%pi;
cste = 0
J = Aire(I)

fig0 = scf(0)
plot(I,J)

//plot(I,inversAire) pour le même résultat, beaucoup plus cher que :
plot(J,I)

//angle pour le quart de pizza
theta4 = inversAire(%pi/2)
c4 = cos(theta4); s4 = sin(theta4)

fig1 = scf(1)
xaxa = get('current_axes')
xaxa.isoview = 'on'

I4 = 0:pas:theta4
R4 = theta4:pas:%pi
C = cos(R4); S = sin(R4)
plot(C,S); plot([k,c4],[0,s4])

u = 0.05; v = 0.05
C4 = cos(I4) + u; S4 = sin(I4) + v
plot(C4,S4)
plot([k,c4]+u,[0,s4]+v)
plot([k,1]+u,[0,0]+v)
