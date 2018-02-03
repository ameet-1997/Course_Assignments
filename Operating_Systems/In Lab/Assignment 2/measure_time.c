#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <time.h>

typedef struct indices_{
	int left;
	int right;
} indices;

// Variable Declarations
int *a, *b, *c;
int threads, n,m,l;
indices *ind;

void *thread_multiplication(void *row)
{	
	// printf("Inside the function\n");
	indices* temp = (indices*) row;

	int i=0,j=0,k=0;

	// printf("The left and right values are: %d %d\n", temp->left, temp->right);
	for(i = temp->left;i < temp->right;++i)
	{
		for(j=0;j<l;++j)
		{	
			for(k=0;k<m;++k)
			{
				c[i*l+j] += a[i*m+k]*b[k*l+j];
			}
		}
	}

}

int main()
{
	scanf("%d %d %d %d",&threads, &n, &m, &l);

	a = (int*) malloc(n*m*sizeof(int));
	b = (int*) malloc(m*l*sizeof(int));
	c = (int*) malloc(n*l*sizeof(int));
	ind = (indices*) malloc(sizeof(indices));

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

	clock_t t;
	t = clock();

	if(threads > n)
	{
		threads = n;
	}

	int blocks = n/threads;
	i = 0;

	pthread_t thread_array[50];
	indices index_array[50];
	int counter = 0;

	while(i < n)
	{		
		index_array[counter].left = i;
		if(i+blocks > n)
		{
			index_array[counter].right = n;
		}
		else
		{
			index_array[counter].right = i+blocks;
		}
		int x = pthread_create(&thread_array[counter], NULL, thread_multiplication, (void*)&index_array[counter]);
		i += blocks;
		counter++;
	}

	for(i=0;i<counter;++i)
	{
		pthread_join(thread_array[i], NULL);
	}

	t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("fun() took %f seconds to execute \n", time_taken);

	// Output the final matrix
	for(i=0;i<n;++i)
	{
		for(j=0;j<l;++j)
		{
			printf("%d\n", c[i*l+j]);
		}
	}
} 
 
