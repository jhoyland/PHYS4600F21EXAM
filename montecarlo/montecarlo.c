#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

double randrange(double a, double b)
{
  // TODO: Write a function to generate a random number between x0 and x1
	//i'll say a as the lower number and b is the higher number.
	double randnum = 0.0;
	double range = b-a;

	randnum = ((double)rand()*range)/(double)RAND_MAX + a;
	return randnum;
}

double function(double x) //the random number goes in here.
{
  return sin(x);
}

double Montecarlo(double a, double b, int N) //this computes the LHS of the equation.
{
  // TODO: Write a function which uses the Monte carlo method to integrate "function" between a and n
  // N is the number of values to average over
	double sum  = 0.0;
	double ans = 0.0;
	for(int i = 0; i<=N; i++)
	{
		sum = sum + function(randrange(a,b));
	}

	ans = (b-a) * ((double)1.0/N) * sum;

	return ans;
}

int main(int argc, char** argv)
{
  srand(time(0)); // This seeds the random number generator and should be called just once here.
  // Put your code here to run the Montecarlo integration for different values of N
  // How big N is required for the integral to converge to within 1%?
  //From symbolab, the definite integral of sin(x)dx from 0 to pi is 2.
  //For consistent results within 1%, N needs to be at least 10000. There seems to be caveats that lies beyond 1% even with a very big N=10000000.
  //Probably the random number.
  int a=0;
  int b=3.14159265358979323846;
  int N=10000;
  double ans=0.0;

  ans = Montecarlo(a, b, N);

  printf("%f\n", ans);

  return 0;
}
