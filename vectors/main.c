#include <stdio.h>
#include <stdlib.h>
#include "vectorops.h"


double areaTriangle(double* p0, double* p1, double* p2)
{
  // Find the vectors pointing from p0 to the other two points
  double area;
  double result1[] = {0,0,0};
  double result2[] = {0,0,0};
  double result3[] = {0,0,0};

  //calculate the area which will be 1/2 * magnitude of ((P1-P0) X (P2-P0))
  subtractVectors(result1,p1,p0);       
  subtractVectors(result2,p2,p0);
  crossProduct(result3,result1,result2);
  area = 0.5*vectorMagnitude(result3);

  return area;
}

int main(int argc, char** argv)
{
  // Example of triangle points
  double p0[3] = {0,0,0};
  double p1[3] = {2,0,0};
  double p2[3] = {0,4,0};

  double p3[3] = {6,6,6};
  double p4[3] = {2,3,0};
  double p5[3] = {0,4,24};

  double p6[3] = {5,0,6};
  double p7[3] = {3,78,5};
  double p8[3] = {2,4,1};



  double area1 = areaTriangle(p0,p1,p2);
  printf("Triangle 1\n");
  printf("Area: %g\n", area1);
  printf("Point 1 Coordinates - x:%g  y:%g  z:%g\n", p0[0],p0[1],p0[2]);
  printf("Point 2 Coordinates - x:%g  y:%g  z:%g\n", p1[0],p1[1],p1[2]);
  printf("Point 3 Coordinates - x:%g  y:%g  z:%g\n\n", p2[0],p2[1],p2[2]);

  double area2 = areaTriangle(p3,p4,p5);
  printf("Triangle 2\n");
  printf("Area: %g\n", area2);
  printf("Point 1 Coordinates - x:%g  y:%g  z:%g\n", p3[0],p3[1],p3[2]);
  printf("Point 2 Coordinates - x:%g  y:%g  z:%g\n", p4[0],p4[1],p4[2]);
  printf("Point 3 Coordinates - x:%g  y:%g  z:%g\n\n", p5[0],p5[1],p5[2]);

  double area3 = areaTriangle(p6,p7,p8);
  printf("Triangle 3\n");
  printf("Area: %g\n", area3);
  printf("Point 1 Coordinates - x:%g  y:%g  z:%g\n", p6[0],p6[1],p6[2]);
  printf("Point 2 Coordinates - x:%g  y:%g  z:%g\n", p7[0],p7[1],p7[2]);
  printf("Point 3 Coordinates - x:%g  y:%g  z:%g\n\n", p8[0],p8[1],p8[2]);

  return 0;
}
