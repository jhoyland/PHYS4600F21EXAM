#include "vectorops.h"
#include <math.h>

// NOTE: All vectors should be stored as arrays of 3 doubles.

void subtractVectors(double* result, double* v0, double* v1)
{
  // TODO: write a function to subtract v1 from v0 and store the result in "result"
  for (int i=0; i<3; i++)
  {
    result[i] = v0[i] - v1[i];
  }
}

void addVectors(double* result, double* v0, double* v1)
{
  // TODO: write a function to add the two vectors v0 and v1 and store the result in "result"
  for (int i=0; i<3; i++)
  {
    result[i] = v0[i] + v1[i];
  }
}

void crossProduct(double* result, double* v0, double* v1)
{
  // TODO: write a program to find the cross product of the two vectors v0 and v1 and store the result in "result"
  result[0] = (v0[1]*v1[2]-v1[1]*v0[2]);
  result[1] = -1*(v0[0]*v1[2]-v1[0]*v0[2]);
  result[2] = (v0[0]*v1[1]-v1[0]*v0[1]);
}


double dotProduct(double* v0, double* v1)
{
  // TODO: write a function to find the dot product the two vectors v0 and v1 and store the result in result
  double result = 0;
  for (int i=0; i<3; i++)
  {
    result = result + v0[i]*v1[i];
  } 
  return result;
}

double vectorMagnitude(double* v)
{
  // TODO: write a function to return the magnitude of the vector v
  double result = 0;
  for (int i=0; i<3; i++)
  {
    result = result + pow(v[i],2);
  } 
  result = pow(result, 0.5);
  return result;

}

double angleBetweenVectors(double* v0, double* v1)
{

    // TODO: write a function to find the angle between the two vectors v0 and v1 and return result
  double angle;
  angle = acos(dotProduct(v0,v1)/(vectorMagnitude(v0)*vectorMagnitude(v1)));
  return angle;
}
