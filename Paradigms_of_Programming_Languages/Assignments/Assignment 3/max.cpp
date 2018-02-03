#include <bits/stdc++.h> 
using namespace std;

#define max1(a,b) (((a)>(b))?(a):(b))

inline int max2(int a, int b)
{
	if(a > b)
		return a;
	else
		return b;
}

int normal_max(int a, int b)
{
	if(a > b)
		return a;
	else
		return b;
}

int main()
{
	int x,y;
	cin>>x>>y;
	cout<<"Using Macro Definition: "<<max1(x,y)<<endl;
	cout<<"Using Inline Function: "<<max2(x,y)<<endl;
	cout<<"Using Normal Function: "<<normal_max(x,y)<<endl;
	// string a = max1(x,y);
	// string b = max2(x,y);
}