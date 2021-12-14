#include "vectorops.h"
#include <math.h>

// NOTE: All vectors should be stored as arrays of 3 doubles.

void subtractVectors(double* result, double* v0, double* v1)
{
  // TODO: write a function to subtract v1 from v0 and store the result in "result"
int i;
for (i=0;i<2;i++){
	result[i] = v0[i] - v1[i];
}
}

void addVectors(double* result, double* v0, double* v1)
{
  // TODO: write a function to add the two vectors v0 and v1 and store the result in "result"
int i;
for (i=0;i<2;i++){
	result[i] = v0[i] + v1[i];
}
}

void crossProduct(double* result, double* v0, double* v1)
{
  // TODO: write a program to find the cross product of the two vectors v0 and v1 and store the result in "result"
// no angle given so assume 0? 
result[0] = (v0[1]*v1[2]) - (v0[2]*v1[1])
result[1] = (v0[2]*v1[0]) - (v0[0]*v1[2])
result[2] = (v0[0]*v1[1]) - (v0[1]*v1[0])

}

double dotProduct(double* v0, double* v1)
{
  // TODO: write a function to find the dot product the two vectors v0 and v1 and store the result in result
int i;
double result;
for (i=0;i<2;i++){
	result += v0[i]*v1[i];
}
return result;
}

double vectorMagnitude(double* v)
{

  // TODO: write a function to return the magnitude of the vector v
int i;
double mag;
for (i=0;i<2;i++){
	mag += pow(v[i],2);
}
mag = sqrt(mag);
return mag;
}

double angleBetweenVectors(double* v0, double* v1)
{
	//Find the dot product of the vectors.
    //Divide the dot product with the magnitude of the first vector.
    //Divide the resultant with the magnitude of the second vector.
int i;
double mag0, mag1, result;
for (i=0;i<2;i++){
	mag0 += pow(v0[i],2);
}
for (i=0;i<2;i++){
	mag1 += pow(v1[i],2);
}
mag0 = sqrt(mag0);
mag1 = sqrt(mag1);

prod = dotProduct(v0,v1);

result = prod/(mag0*mag1);

    // TODO: write a function to find the angle between the two vectors v0 and v1 and return result

}
