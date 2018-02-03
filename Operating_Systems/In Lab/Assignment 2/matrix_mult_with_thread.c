#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

// Variable Declarations
int *a, *b, *c;
int threads, n,m,l;
indices *index;

// typedef struct indices_{
// 	int i;
// 	int j;
// } indices;

typedef struct indices_{
	int left;
	int right;
} indices;



void thread_multiplication(void *row)
{
	// int r,c;
	// r = row->i;

	int i=0,j=0,k=0;
	for(i = row->left;i < row->right;++i)
	{
		for(j=0;j<l;++j)
		{	
			for(k=0;k<m;++k)
			{
				c[r*l+j] += a[r*m+k]*b[k*l+j];
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
	index = (indices*) malloc(sizeof(indices));

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

	// void *myThreadFun(void *vargp)
	// {
	//     sleep(1);
	//     printf("Printing GeeksQuiz from Thread \n");
	//     return NULL;
	// }
	  
	// int main()
	// {
	//     pthread_t tid;
	//     printf("Before Thread\n");
	//     pthread_create(&tid, NULL, myThreadFun, NULL);
	//     pthread_join(tid, NULL);
	//     printf("After Thread\n");
	//     exit(0);
	// }

	// Multiply the matrix
	// for(i=0;i<n;++i)
	int blocks = n/threads;
	while(i < n)
	{	
		index->i = i;
		pthread_t tid;
		pthread_create(&tid, NULL, thread_multiplication, index);
		// for(j=0;j<l;++j)
		// {	
		// 	for(k=0;k<m;++k)
		// 	{
		// 		c[i*l+j] += a[i*m+k]*b[k*l+j];
		// 	}
		// }
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
}