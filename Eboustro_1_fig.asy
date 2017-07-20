size(6cm,3cm);
import graph;
import settings;
outformat = "pdf";

xaxis( xmin = -5, xmax = 5, EndArrow);
yaxis( ymin = -5, ymax =0, BeginArrow);
label("$i$",(5,0),N);
label("$j$",(0,-5),E);
for(int i=-4; i<5; ++i){
  for(int j=0; j+5>0; --j){
    dot((i,j));
  }
}
dot((0,0),red+7);
dot((-1,-1),red+7);dot((1,-1),red+7);
dot((-2,-2),red+7);dot((0,-2),red+7);dot((2,-2),red+7);
dot((-3,-3),red+7);dot((-1,-3),red+7);dot((1,-3),red+7);dot((3,-3),red+7);
dot((-4,-4),red+7);dot((-2,-4),red+7);dot((0,-4),red+7);dot((2,-4),red+7);dot((4,-4),red+7);
