settings.outformat = "pdf";

size(4cm);

real c = 0.6;
pair C = (c,0);
pair O = (0,0);
real deg = 180/pi;
real theta0 = 0;
real theta1 = 1.1;

path rara = arc(O,1,theta0*deg,theta1*deg);
path petitrara = scale(0.3)*rara;
draw(rara,red+1);
draw(petitrara);

pair A0 = (cos(theta0),sin(theta0));
pair A1 = (cos(theta1),sin(theta1));

path CA0 = C--A0;
path A1C = A1--C;
path part = CA0--rara--A1C..cycle;
fill(part,red);

//draw(C--A0,red+1);
//draw(C--A1,red+1);
draw(O--C,black+1);
draw(O--A1,black+1);
dot(C);dot(A1);

label("$C$",C,S);
label("$\theta$",(0.31,0.2));
label("$M_\theta$",A1,N);
