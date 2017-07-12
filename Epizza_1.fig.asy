size(4cm);
draw(unitcircle,red+1);
real c = 0.4;
pair C = (c,0);
real theta0 = 0;
real theta1 = 1.1;
real theta2 = 1.9;
real theta3 = 4.1;
pair A0 = (cos(theta0),sin(theta0));
pair A1 = (cos(theta1),sin(theta1));
pair A2 = (cos(theta2),sin(theta2));
pair A3 = (cos(theta3),sin(theta3));
draw(C--A0,red+1);
draw(C--A1,red+1);
draw(C--A2,red+1);
draw(C--A3,red+1);
label("$C$",C,S);