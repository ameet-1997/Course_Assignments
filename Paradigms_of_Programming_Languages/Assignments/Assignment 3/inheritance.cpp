#include <bits/stdc++.h>
using namespace std;

class stack_base{
public:
	class Node{
		Node* next;
	};
	Node* top;

	stack_base(){
		top = NULL;
	}

	// Node* new_node(){
	// 	Node* temp = new Node;

	// }

	// void push(){
	// 	Node* temp = new_node();
	// }
};


class stack_int{
public:
	class Node{
		int data;
		Node* next;
	};
	Node* top;

	stack_int(){
		top = NULL;
	}

	// Node* new_node(){
	// 	Node* temp = new Node;
		
	// }

	// void push(){
	// 	Node* temp = new_node();
	// }
};

int main()
{

}