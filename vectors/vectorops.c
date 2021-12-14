#include "vectorops.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// NOTE: All vectors should be stored as arrays of 3 doubles.

void subtractVectors(double* result, double* v0, double* v1)
{
	result[0] = v0[0] - v1[0];
	result[1] = v0[1] - v1[1];
	result[2] = v0[2] - v1[2];
}

void addVectors(double* result, double* v0, double* v1)
{
	result[0] = v0[0] + v1[0];
	result[1] = v0[1] + v1[1];
	result[2] = v0[2] + v1[2];
}

void crossProduct(double* result, double* v0, double* v1)
{
	result[0] = v0[1]*v1[2] - v1[1]*v0[2];
	result[1] = v0[0]*v1[2] - v1[0]*v0[2];
	result[2] = v0[0]*v1[1] - v1[0]*v0[1];
}

double dotProduct(double* v0, double* v1)
{
	return v0[0]*v1[0] + v0[1]*v1[1] + v0[2]*v1[2];
}

double vectorMagnitude(double* v)
{
	return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

double angleBetweenVectors(double* v0, double* v1)
{
	return acos(dotProduct(v0, v1)/(vectorMagnitude(v0)*vectorMagnitude(v1)));
}

void printCords(int a, double* p)
{
	printf("p%d = {", a);
	for(int i=0; i<3; i++)
	{
		printf("%0.2f,", p[i]);
	}
	printf("}\n");
}