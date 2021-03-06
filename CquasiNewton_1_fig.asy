size(5cm);
import graph;
import settings;
outformat = "pdf";

real a = 1.;
real b = 2.7;

xaxis("$x$", -1, 4, EndArrow); 
yaxis("$y$", -1, 4 , EndArrow);

label("$a$",(a,0),N);
dot((b,0),red+4);
label("$x_n$",(b,0),NE);

real f(real x) { return (x-a)^3 - 1;};
real bb = b -f(b)/(3*(b-a)^2);
dot((bb,0),red+4);
label("$x_{n+1}$",(bb,0),SE);

draw(graph(f,a,b));
draw((a,0)--(a,f(a)),dotted);
draw((b,0)--(b,f(b)),dotted);
draw((b,f(b))--(bb,0), red+1+dashed);
