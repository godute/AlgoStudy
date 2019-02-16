#include <iostream>
#include <queue>

using namespace std;

int M, N;
int box[1000][1000];
int green = 0;
int temp, temp_r, temp_c, temp_date;
queue<int> q;
int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

bool isOutOfBox(int r, int c) {
    if(r == -1 || r == N || c == -1 || c == M) return true;
    else return false;
}

void ripe(int r, int c, int date) {
    for(int i = 0; i < 4; i++) {
        if(isOutOfBox(r + dr[i], c + dc[i])) continue;
        else if(box[r + dr[i]][c + dc[i]] == 0) {
            box[r + dr[i]][c + dc[i]] = 1;
            green--;
            q.push(r + dr[i]);
            q.push(c + dc[i]);
            q.push(date);
        }
    }
}

int main() {
    cin.sync_with_stdio(false);
    cin >> M >> N;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> temp;
            box[i][j] = temp;
            if(!temp) green++;
            if(temp == 1) {
                q.push(i);
                q.push(j);
                q.push(0);
            }
        }
    }
    
    if(!green) {
        cout << 0 << endl;
        return 0;
    }

    while(!q.empty()) {
        temp_r = q.front();
        q.pop();
        temp_c = q.front();
        q.pop();
        temp_date = q.front();
        q.pop();
        ripe(temp_r, temp_c, temp_date + 1);
    }
    
    if(green) {
        cout << -1 << endl;
        return 0;
    }

    cout << temp_date << endl;
    return 0;
  }