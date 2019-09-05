size(15cm);
//import graph;
import settings;
outformat = "pdf";

real[] theta = {-0.5, 1.0, 0.4, -0.4, -0.8, 0.6, -0.4, 0.55, -0.7};

pair[] A;
pair[] B;

real l = 1.4;
real r = 1.2;
A[0] = (0,0);
B[0] = A[0] + (l,0);

int i = 0;
for (real t : theta){
  A.push(A[i] + 3*expi(t));
  B.push(A[i+1] + (l,0));
  i = i + 1;
}
pair I = (-2,0);
pair F = A[9] + (2,0);

path mol = A[0]--A[1]--A[2]--A[3]--A[4]--A[5]--A[6]--A[7]--A[8]--A[9];

//draw(mol,deepgreen +1);
draw(I--A[0],BeginArrow);
//draw(A[0]--A[1],deepgreen +1);

draw(A[9]--F,EndArrow);

draw((0,-3)--(xpart(A[9]),-3),Arrows);
draw(A[0]--(0,-3),dotted);
draw(A[9]--(xpart(A[9]),-3),dotted);

for (int i = 0; i < 9; ++i){
  if (i != 5){
    draw(A[i]--A[i+1],deepgreen +1);
  } else {
    draw(A[i]--A[i+1],dotted + deepgreen +1);
  }
  if ((i < 3) | (i > 6)) {
    draw(A[i]--B[i],dotted);
    draw(arc(A[i],r,0.0,degrees(theta[i])),ArcArrow(2));
  }
}

label("$z$", (xpart(A[9])/2,-3.4));

pair P;
real rho = 1.8;

P = A[0] + rho*expi(theta[0]/2); 
label("$\theta_0$",P);

P = A[1] + rho*expi(theta[1]/2); 
label("$\theta_1$",P);

P = A[2] + rho*expi(theta[2]/2.5); 
label("$\theta_2$",P);

P = A[7] + rho*expi(theta[7]/2.5) + (0.2,0); 
label("$\theta_{n-2}$",P);

P = A[8] + rho*expi(theta[8]/2) + (0.2,0); 
label("$\theta_{n-1}$",P);