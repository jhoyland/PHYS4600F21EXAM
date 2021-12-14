#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

double randrange(double a, double b)
{
  // TODO: Write a function to generate a random number between x0 and x1
	if(srand())
}

double function(double x)
{
  return sin(x);
}

double Montecarlo(double a, double b, int N)
{
  // TODO: Write a function which uses the Monte carlo method to integrate "function" between a and n
  // N is the number of values to average over
}

int main(int argc, char** argv)
{
  srand(time(0)); // This seeds the random number generator and should be called just once here.

  // Put your code here to run the Montecarlo integration for different values of N
  // How big N is required for the integral to converge?
}
