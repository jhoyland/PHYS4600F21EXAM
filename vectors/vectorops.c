#include "vectorops.h"
#include <math.h>

// by MICHAEL YAKOVLEV

// NOTE: All vectors should be stored as arrays of 3 doubles.

void subtractVectors(double* result, double* v0, double* v1)
{
  result[0]=v1[0]-v0[0];
  result[1]=v1[1]-v0[1];
  result[2]=v1[2]-v0[2];
}

void addVectors(double* result, double* v0, double* v1)
{
  result[0]=v1[0]+v0[0];
  result[1]=v1[1]+v0[1];
  result[2]=v1[2]+v0[2];
}

void crossProduct(double* result, double* v0, double* v1)
{
  result[0]=v0[1]*v1[2]-v1[1]*v0[2];
  result[1]=-(v0[0]*v1[2]-v1[0]*v0[2]);
  result[2]=v0[0]*v1[1]-v1[0]*v0[1];
}

double dotProduct(double* v0, double* v1)
{
  double value=v0[0]*v1[0]+v0[1]*v1[1]+v0[2]*v1[2];
  return value;
}

double vectorMagnitude(double* v)
{
  double value= sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]);
  return value;
}

double angleBetweenVectors(double* v0, double* v1)
{
    double l_v0=vectorMagnitude(v0);
    double l_v1=vectorMagnitude(v1);
    double dot_=dotProduct(v0,v1);
    double value=acos(dot_/(l_v0*l_v1));
    return value;
}

// by MICHAEL YAKOVLEV