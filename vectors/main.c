#include <stdio.h>
#include <stdlib.h>
#include "vectorops.h"


double areaTriangle(double* p0, double* p1, double* p2)
{
	double p0_to_p1[3];
	subtractVectors(p0_to_p1, p0, p1);

	double p0_to_p2[3];
	subtractVectors(p0_to_p2, p0, p2);

	double crossProd[3];
	crossProduct(crossProd, p0_to_p1, p0_to_p2);

	return 0.5*vectorMagnitude(crossProd);

}

int main(int argc, char** argv)
{
	// Example of triangle points
	double p0[3] = {0,0,0};
	double p1[3] = {2,0,0};
	double p2[3] = {0,4,0};
	double answer1 = areaTriangle(p0, p1, p2);
	printf("The area of the triangle formed by these points: \n");
	printCords(0,p0);
	printCords(1,p1);
	printCords(3,p2);
	printf("is equal to %f\n\n", answer1);

	p0[1] = 1;
	p1[1] = 5;
	p2[2] = 6;
	double answer2 = areaTriangle(p0, p1, p2);
	printf("The area of the triangle formed by these points: \n");
	printCords(0,p0);
	printCords(1,p1);
	printCords(3,p2);
	printf("is equal to %f\n\n", answer2);

	p0[1] = 1;
	p1[2] = 10;
	p2[0] = -9;
	double answer3 = areaTriangle(p0, p1, p2);
	printf("The area of the triangle formed by these points: \n");
	printCords(0,p0);
	printCords(1,p1);
	printCords(3,p2);
	printf("is equal to %f\n\n", answer3);

}
