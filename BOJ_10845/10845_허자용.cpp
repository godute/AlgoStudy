#include <iostream>
#include <string>

using namespace std;

int len = 0;
int insert = 0;
int queue[10000];
int head = 0;

int push(int x) {
	queue[insert] = x;
	insert++;
	len++;
	return 0;
}

void pop() {
	if (!len) {
		cout << -1 << endl;
		return;
	}
	cout << queue[head] << endl;
	head++;
	len--;
	return;
}

void front() {
	if (!len) cout << -1 << endl;
	else cout << queue[head] << endl;
	return;
}

void back() {
	if (!len) cout << -1 << endl;
	else cout << queue[insert-1] << endl;
	return;
}


int main()
{	
	int T;
	cin >> T;
	string text;
	int a;

	for (int i = 0; i < T; i++) {
		cin >> text;
		if (text == "push") {
			cin >> a;
			push(a);
		}
		else if (text == "pop") pop();
		else if (text == "size") cout << len << endl;
		else if (text == "empty") {
			if (len) cout << 0 << endl;
			else cout << 1 << endl;
		}
		else if (text == "front") front();
		else if (text == "back") back();
	}
}
