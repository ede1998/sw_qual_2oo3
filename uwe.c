#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>


long double Rpld(char **argv, long double t)
{
  long double acc = 1.0;
  while (*++argv)
    {
      long double const lambdai = strtod(*argv, NULL);
      long double const term = -expm1l(-lambdai*t);
      acc *= term;
    }
  return 1.0 - acc;
}

double Rp(char **argv, double t)
{
  double acc = 1.0;
  while (*++argv)
    {
      double const lambdai = strtod(*argv, NULL);
      double const term = -expm1(-lambdai*t);
      acc *= term;
    }
  return 1.0 - acc;
}

long double Rp2ld(char **argv, long double t)
{
  long double acc = 0.0;
  while (*++argv)
    {
      long double const lambdai = strtod(*argv, NULL);
      long double const term = log1pl(-expl(-lambdai*t));
      acc += term;
    }
  return -expm1l(acc);
}


double Rp2(char **argv, double t)
{
  double acc = 0.0;
  while (*++argv)
    {
      double const lambdai = strtod(*argv, NULL);
      double const term = log1p(-exp(-lambdai*t));
      acc += term;
    }
  return -expm1(acc);
}

int main(int argc, char **argv)
{
  if (argc < 2) exit(EXIT_FAILURE);
  //printf("%.15e\n", Rp(argv, 87600.));
  //printf("%.15e\n", Rp2(argv, 87600.));
  //printf("%.20Le\n", Rpld(argv, 87600.));
  printf("%.18Le\n", Rp2ld(argv, 87600.));
  //printf("%.20Le\n", LDBL_TRUE_MIN);
}
