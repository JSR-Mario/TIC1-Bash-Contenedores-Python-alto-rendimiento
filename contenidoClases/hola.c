#include <stdio.h>
#include "omp.h"


void main ()
{
	double A[1000] = { 0 };
	#pragma omp parallel
	{
		int ID=omp_get_thread_num();
		printf("Hola (%d)\n", ID);
		printf("Mundo (%d)\n", ID);
		printf("A[%d] = %d", ID, A[ID]);
	}
}
