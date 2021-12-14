#include <stdio.h>
#include <stdlib.h>
#include "vectorops.h"


double areaTriangle(double* p0, double* p1, double* p2)
{
  // Find the vectors pointing from p0 to the other two points
double A;
double v1[3];
double v2[3];
double v3[3];
subtractVectors(v1,p2,p0);
subtractVectors(v2,p2,p1);
crossProduct(v3,v1,v2);
A = vectorMagnitude(v3)/2;
printf("Area = %0.2f\n",A);
return A;
}

int main(int argc, char** argv)
{
  // Example of triangle points
  double p0[3] = {3,2,1};
  double p1[3] = {2,4,2};
  double p2[3] = {0,0,0};

  addVectors(p2, p0, p1);
  subtractVectors(p2, p0, p1);
  dotProduct(p0,p1);
  crossProduct(p2,p0,p1);
  vectorMagnitude(p0);
  angleBetweenVectors(p0,p1);
  areaTriangle(p0,p1,p2);
}
