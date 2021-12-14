#ifndef __VECTOROPS_H
#define __VECTOROPS_H

void subtractVectors(double* result, double* v0, double* v1);
void addVectors(double* result, double* v0, double* v1);
void crossProduct(double* result, double* v0, double* v1);
double dotProduct(double* v0, double* v1);
double vectorMagnitude(double* v);
double angleBetweenVectors(double* v0, double* v1);

#endif
