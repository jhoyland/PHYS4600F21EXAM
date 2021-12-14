#include <stdio.h>
#include <stdlib.h>
#include "vectorops.h"


double areaTriangle(double* p0, double* p1, double* p2)
{
  // Find the vectors pointing from p0 to the other two points
  int i;
  double v0[3], v1[3];
  for (i=0; i<2; i++){
  	v0[i] = p1[i] - p0[i];}
  for (i=0; i<2; i++){
  	v1[i] = p2[i] - p0[i];}
  
  printf("%f, %f, %f \n",v0[0],v0[1],v0[2]);
  printf("%f, %f, %f \n",v1[0],v1[1],v1[2]);
}

int main(int argc, char** argv)
{
  // Example of triangle points
  double p0[3] = {0,0,0};
  double p1[3] = {2,0,0};
  double p2[3] = {0,4,0};

areaTriangle(p0,p1,p2);

// maybe something wrong with makefile that is not allowing the functions
// to be declared through the h file? 
/*
double result[3];
subtractVectors(result, p2, p1);
printf("%f, %f, %f \n", result[0], result[1],result[2]);

double addresult[3];
addVectors(result, p2, p1);
printf("%f, %f, %f \n", addresult[0],addresult[1],addresult[2]);

double crossresult[3];
crossProduct(result, p2, p1);
printf("%f, %f, %f \n", crossresult[0],crossresult[1],crossresult[2]);

double dot, angle;
dot = dotProduct(p2, p1);
printf("%f \n", dot);

angle=angleBetweenVectors(p2, p1);
printf("%f \n", angle);
*/
return 0;
}