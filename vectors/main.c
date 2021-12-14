#include <stdio.h>
#include <stdlib.h>
#include "vectorops.h"

// by MICHAEL YAKOVLEV

double areaTriangle(double* p0, double* p1, double* p2)
{
  double v1_p[3];
  double v2_p[3];
  subtractVectors(v1_p, p0, p1);
  //printf("\nVector 1:\t\t%lfi\t%lfj\t%lfk",v1_p[0],v1_p[1],v1_p[2]);
  subtractVectors(v2_p, p0, p2);
  //printf("\nVector 2:\t\t%lfi\t%lfj\t%lfk",v2_p[0],v2_p[1],v2_p[2]);
  double v_area[3];
  crossProduct(v_area, v1_p, v2_p);
  //printf("\nVector A:\t\t%lfi\t%lfj\t%lfk",v_area[0],v_area[1],v_area[2]);
  double A= vectorMagnitude(v_area)/2.0;
  return A;
}

// by MICHAEL YAKOVLEV

int main(int argc, char** argv)
{
  // Example of triangle points
  double p0[3] = {0,0,0};
  double p1[3] = {2,0,0};
  double p2[3] = {0,4,0};
  double area=areaTriangle(p0,p1,p2);
  printf("\nPoint of Origin:\t%lfi\t%lfj\t%lfk",p0[0],p0[1],p0[2]);
  printf("\nEnd Point 1:\t\t%lfi\t%lfj\t%lfk",p1[0],p1[1],p1[2]);
  printf("\nEnd Point 2:\t\t%lfi\t%lfj\t%lfk",p2[0],p2[1],p2[2]);
  printf("\nArea:\t\\tt%lf",area);
  printf("\n\n\n");

  double p00[3] = {1,1,1};
  double p01[3] = {2,0,3};
  double p02[3] = {8,4,0};
  area=areaTriangle(p00,p01,p02);
  printf("\nPoint of Origin:\t%lfi\t%lfj\t%lfk",p00[0],p00[1],p00[2]);
  printf("\nEnd Point 1:\t\t%lfi\t%lfj\t%lfk",p01[0],p01[1],p01[2]);
  printf("\nEnd Point 2:\t\t%lfi\t%lfj\t%lfk",p02[0],p02[1],p02[2]);
  printf("\nArea:\t\t\t%lf",area);
    printf("\n\n\n");

  double p000[3] = {-11,-37,-23};
  double p001[3] = {77,-7,96};
  double p002[3] = {-13,66,-44};
  area=areaTriangle(p000,p001,p002);
  printf("\nPoint of Origin:\t%lfi\t%lfj\t%lfk",p000[0],p000[1],p000[2]);
  printf("\nEnd Point 1:\t\t%lfi\t%lfj\t%lfk",p001[0],p001[1],p001[2]);
  printf("\nEnd Point 2:\t\t%lfi\t%lfj\t%lfk",p002[0],p002[1],p002[2]);
  printf("\nArea:\t\t\t%lf",area);
}

// by MICHAEL YAKOVLEV