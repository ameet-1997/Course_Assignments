#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int *a, *b, *c;

	int threads, n,m,l;
	scanf("%d %d %d %d",&threads, &n, &m, &l);

	a = (int*) malloc(n*m*sizeof(int));
	b = (int*) malloc(m*l*sizeof(int));
	c = (int*) malloc(n*l*sizeof(int));

	clock_t t;
	t = clock();

	// Initialize values
	int i,j,k;

	for(i=0;i<n;++i)
	{
		for(j=0;j<l;++j)
		{
			c[i*l+j] = 0;
		}
	}

	// Take input from stdin or file
	for(i=0;i<n;++i)
	{
		for(j=0;j<m;++j)
		{
			scanf("%d",&a[i*m+j]);
		}
	}

	for(i=0;i<m;++i)
	{
		for(j=0;j<l;++j)
		{
			scanf("%d",&b[i*l+j]);
		}
	}

	// Multiply the matrix
	for(i=0;i<n;++i)
	{
		for(j=0;j<l;++j)
		{	
			for(k=0;k<m;++k)
			{
				c[i*l+j] += a[i*m+k]*b[k*l+j];
			}
		}
	}

	// Output the final matrix
	for(i=0;i<n;++i)
	{
		for(j=0;j<l;++j)
		{
			printf("%d ", c[i*l+j]);
		}
		printf("\n");
	}

	t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("fun() took %f seconds to execute \n", time_taken);
}