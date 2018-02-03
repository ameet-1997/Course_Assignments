#include <bits/stdc++.h>
using namespace std;

class Point{
	int x;
	int y;

public:
	Point(int x1, int y1){
		x = x1; y = y1;
	}

	int get_x() const{
		return x;
	}

	int get_y() const{
		return y;
	}
} ;


int main(){
	const Point center(3,4);
	cout<<"Values are: "<<center.get_x()<<" : "<<center.get_y()<<endl;
}