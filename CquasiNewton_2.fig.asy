size(5cm);
import graph;
import settings;
outformat = "pdf";

real a = 1.;
real b = 2.7;

xaxis("$x$", -1, 4, EndArrow); 
yaxis("$y$", -3, 2 , EndArrow);

label("$x_n$",(a,0),SW);
dot((a,0),red+4);
label("$b$",(b,0),S);

real f(real x) { return 10*(x-0.92)^(0.1) - 10;};
real aa = a -f(a)/((a-0.92)^(-0.9));

dot((aa,0),red+4);
label("$x_{n+1}$",(aa,0),NE);

draw(graph(f,a,b));
draw((a,0)--(a,f(a)),dotted);
draw((b,0)--(b,f(b)),dotted);
draw((a,f(a))--(aa,0), red+1+dashed);
