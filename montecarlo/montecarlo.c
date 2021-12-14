#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

double randrange(double a, double b)
{
	if(a > b)
	{
		double temp = a;
		a = b;
		b = temp;
	}
  // TODO: Write a function to generate a random number between x0 and x1
	double randDouble = (double)rand()/RAND_MAX*b-a;

	return randDouble;
}

double function(double x)
{
  return sin(x);
}

double Montecarlo(double a, double b, int N)
{
	double sumFunc = 0.0;
	for(int i = 0; i <= N; i++)
	{
		double randNum = randrange(a,b);
		sumFunc += function(randNum);
	}

	return (b - a)*sumFunc/N;
  // TODO: Write a function which uses the Monte carlo method to integrate "function" between a and n
  // N is the number of values to average over
}

int main(int argc, char** argv)
{
  srand(time(0)); // This seeds the random number generator and should be called just once here.

  double tolerance = 0.01;
  double result = 0.0;
  int i = 1;
  double n = 2.0;
  while(n > tolerance)
  {
  	result = Montecarlo(0.0, M_PI, i);
  	i++;
  	n = 2.0 - result;
  	if(n < 0.0)
  	{
  		n *= -1;
  	}
  }
  printf("It took this many N = %d\n", i);
  printf("The result is %f\n", result);
  
  // Put your code here to run the Montecarlo integration for different values of N
  // How big N is required for the integral to converge?
}
