#include <iostream>
using namespace std;
int Arr[11];
int MAX, MIN;
void DFS(int n, int depth, int op1, int op2, int op3, int op4, int sum) {
    if (depth == n) {
        if (sum > MAX) {
            MAX = sum;
        }
        if (sum < MIN) {
            MIN = sum;
        }
        return;
    }
    if (op1 > 0) {
        DFS(n, depth + 1, op1 - 1, op2, op3, op4, sum + Arr[depth]);
    }
    if (op2 > 0) {
        DFS(n, depth + 1, op1, op2 - 1, op3, op4, sum - Arr[depth]);
    }
    if (op3 > 0) {
        DFS(n, depth + 1, op1, op2, op3 - 1, op4, sum*Arr[depth]);
    }
    if (op4 > 0) {
        DFS(n, depth + 1, op1, op2, op3, op4 - 1, sum / Arr[depth]);
    }
}
int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> Arr[i];
    }
    int op1, op2, op3, op4;
    cin >> op1 >> op2 >> op3 >> op4;
    MAX = -1000000000;
    MIN = 1000000000;
    DFS(N, 1, op1, op2, op3, op4, Arr[0]);
    cout << MAX << endl << MIN << endl;
    return 0;
}