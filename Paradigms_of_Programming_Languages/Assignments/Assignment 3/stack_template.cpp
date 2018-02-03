#include <bits/stdc++.h>
using namespace std;

template < class T>
class Stack{
public:
	class Node{
	public:
		T data;
		Node *next;
	};

	Node *head;

	void push(T data){
		Node *temp = new Node;
		temp->data = data;
		temp->next = head;
		head=temp;		
	}

	void pop(){ 		// Observe that this function will be the same
		Node *temp = head;
		head = head->next;
		delete temp;
	}

	bool empty(){ 		// Observe that this function will be the same
		if(head)
			return true;
		else
			return false;
	}

	T top(){
		if(head == NULL)
			return -1;
		else
			return head->data;
	}

	Stack(){
		head = NULL;
	}
};

int main(){
	Stack<int> a;
	Stack<float> b;
}