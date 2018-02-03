#include <bits/stdc++.h>
using namespace std;

class Stack{
public:
	class Node{
	public:
		int data;
		Node *next;
	};

	Node *head;

	void push(int);
	void push(float);

	virtual void pop(){ 		// Observe that this function will be the same
		Node *temp = head;
		head = head->next;
		delete temp;
	}

	virtual bool empty(){ 		// Observe that this function will be the same
		if(head){
			return true;
		}
		else{
			return false;
		}
	}

	Stack(){
		head = NULL;
	}
};

class StackInt : public Stack{
public:
	class Node{
	public:
		int data;
		Node *next;
	};

	Node *head;

	int top(){
		if(head == NULL){
			return -1;
		}
		else{
			return head->data;
		}
	}

	void push(int data){
		Node *temp = new Node;
		temp->data = data;
		temp->next = head->next;
		head=temp;
	}
};

class StackFloat : public Stack{
public:
	class Node{
	public:
		float data;
		Node *next;
	};

	Node *head;

	float top(){
		if(head == NULL){
			return -1;
		}
		else{
			return head->data;
		}
	}

	void push(float data){
		Node *temp = new Node;
		temp->data = data;
		temp->next = head->next;
		head=temp;
	}
};


int main(){
	StackInt a;
	StackInt b;
}
