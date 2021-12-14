#include "vectorops.h"
#include <math.h>

// NOTE: All vectors should be stored as arrays of 3 doubles.

void subtractVectors(double* result, double* v0, double* v1)
{
  // TODO: write a function to subtract v1 from v0 and store the result in "result"
 printf("Sub = { ");		
 for(int i = 0; i < 3; i++) 
   {
    result[i] = v1[i]-v0[i];
	printf("%0.2f ",result[i]);
   }
 printf("}\n");
}

void addVectors(double* result, double* v0, double* v1)
{
  // TODO: write a function to add the two vectors v0 and v1 and store the result in "result"
 printf("Add = { ");
 for(int i = 0; i < 3; i++) 
   {
	result[i] = v0[i]+v1[i];
	printf("%0.2f ",result[i]);
   }
 printf("}\n");
}

void crossProduct(double* result, double* v0, double* v1)
{
  // TODO: write a program to find the cross product of the two vectors v0 and v1 and store the result in "result"
 printf("Cross = { ");
 result[0] = v0[1]*v1[2]-v0[2]*v1[1];
 result[1] = v0[2]*v1[0]-v0[0]*v1[2];
 result[2] = v0[0]*v1[1]-v0[1]*v1[0];
 for(int i = 0; i < 3; i++) 
   {
	printf("%0.2f ",result[i]);
   }
 printf("}\n");
}

double dotProduct(double* v0, double* v1)
{
  // TODO: write a function to find the dot product the two vectors v0 and v1 and store the result in result
 double v2;
	v2 = v0[0]*v1[0]+v0[1]*v1[1]+v0[2]*v1[2];
 printf("Dot = {%0.2f}\n",v2);
 return v2;
}

double vectorMagnitude(double* v)
{
// TODO: write a function to return the magnitude of the vector v
 double m;
 m = sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2]);
 printf("Magni = {%0.2f}\n",m);
 return m;
}

double angleBetweenVectors(double* v0, double* v1)
{
    // TODO: write a function to find the angle between the two vectors v0 and v1 and return result
double C;
double A;
double B;
double t;
C =  dotProduct(v0,v1);
A = vectorMagnitude(v0);
B = vectorMagnitude(v1);

t = acos(C/(A*B));
printf("Angle = {%0.4f}\n",t);  
return t;
}
