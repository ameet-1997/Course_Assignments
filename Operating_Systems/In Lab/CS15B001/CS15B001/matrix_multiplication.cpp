#include "ctpl_stl.h"
#include <bits/stdc++.h>

using namespace std;

vector< vector<int> > a;
vector< vector<int> > b;
vector< vector<int> > c;
int n,m,p;

struct Indices {
    Indices(int i, int j) { this->i = i; this->j = j; /*std::cout << "Indices ctor " << this->v << '\n';*/ }
    ~Indices() { /*std::cout << "Indices dtor\n";*/ }
    int i;
    int j;
};

void matrix_mult(int id, Indices& ind)
{	
	c[ind.i][ind.j] = 0;
	for(int k=0;k<m;++k)
	{
		c[ind.i][ind.j] += a[ind.i][k]*b[k][ind.j];
	}
}

int main()
{	
	// Initialize the thread pools	
	int num_of_threads = 3;
	ctpl::thread_pool pp(num_of_threads);
	
	// Take matrice indices as input
	cin>>n>>m>>p;

	// Initialize the vectors with required space
	a.resize(n);
	for(int i=0;i<n;++i)
	{
		a[i].resize(m);
	}

	b.resize(m);
	for(int i=0;i<p;++i)
	{
		b[i].resize(p);
	}

	c.resize(n);
	for(int i=0;i<p;++i)
	{
		c[i].resize(p);
	}
	// Matrix initialization complete

	// Take input from stdin
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<m;++j)
		{
			cin>>a[i][j];
		}
	}

	for(int i=0;i<m;++i)
	{
		for(int j=0;j<p;++j)
		{
			cin>>b[i][j];
		}
	}
	// Done taking inputs


	// Multiplty the matrices
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<p;++j)
		{
			pp.push(matrix_mult, Indices(i,j));
			// matrix_mult(1, Indices(i,j));
			// cout<<"Value Here is: "<<c[i][j]<<"\n";
		}
	}

	// Display the result
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<p;++j)
		{
			cout<<c[i][j]<<" ";
		}
		cout<<endl;
	}


} 
