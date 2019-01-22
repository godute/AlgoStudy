#include <iostream>
#include <queue>

using namespace std;

int N, M;
char temp;
bool map[100][100] = {0,};
bool visited[100][100] = {0,};
queue<int> q;
int ans = 0;

void push(int n, int m, int dist) {
  visited[n][m] = true;
  q.push(n);
  q.push(m);
  q.push(dist);
}


void go(int n, int m, int dist) {
    // up
    if (n && !visited[n-1][m] && map[n-1][m]) push(n-1, m, dist+1);
    // down
    if (n != N-1 && !visited[n+1][m] && map[n+1][m]) push(n+1, m, dist+1);
    // left
    if (m && !visited[n][m-1] && map[n][m-1]) push(n, m-1, dist+1);
    // right
    if (m != M-1 && !visited[n][m+1] && map[n][m+1]) push(n, m+1, dist+1);
}


int main() {
    cin >> N >> M;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> temp;
                if(temp == '0') map[i][j] = false;
                else map[i][j] = true;
        }
    }

    push(0, 0, 1);
    while(!q.empty()) {
        int temprow = q.front();
        //cout << temprow << endl;
        q.pop();
        int tempcol = q.front();
        //cout << tempcol << endl;
        q.pop();
        int tempdist = q.front();
        //cout << tempdist << endl;
        q.pop();
        if (temprow == N-1 && tempcol == M-1) {
          ans = tempdist;
          break;
        }
        else go(temprow, tempcol, tempdist);
    }
    cout << ans << endl;
    
    return 0;
}
