settings.outformat = "pdf";
import graph;
size(4cm);
pen P = deepgreen+1;
pair O = (0,0);
pair X = (0,-5);
pair Y = (5,0);

draw(O--X,P,Arrow);
draw(O--Y,P,Arrow);
label("$x$",X,W);
label("$y$",Y,N);