#include <iostream>

using namespace std;

int N, M;
int lab[8][8];
int simulation[8][8];
int maxSafeArea = 0;
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

bool isOutOfRange(int r, int c) {
    if(r < 0 || r > N - 1 || c < 0 || c > M - 1) return true;
    else return false;
}

void diffusion(int r, int c) {
    int new_r, new_c;
    simulation[r][c] = 2;
    for(int i = 0; i < 4; i++) {
        new_r = r + dr[i];
        new_c = c + dc[i];
        if(isOutOfRange(new_r, new_c)) continue;
        else if(!simulation[new_r][new_c]) diffusion(new_r, new_c);
    }
}

void countSafeArea() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            simulation[i][j] = lab[i][j];
        }
    }

    for(int r = 0; r < N; r++) {
        for(int c = 0; c < M; c++) {
            if(simulation[r][c] == 2) {
                diffusion(r, c);
            }
        }
    }

    int cnt = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(!simulation[i][j]) cnt++;
        }
    }
    if(maxSafeArea < cnt) maxSafeArea = cnt;
}

void buildWall(int r, int c, int cnt) {
    if(cnt == 3) {
        lab[r][c] = -1;
        countSafeArea();
        lab[r][c] = 0;
        return;
    }

    lab[r][c] = -1;
    for(int i = r; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(!lab[i][j]) buildWall(i, j, cnt+1);
        }
    }
    lab[r][c] = 0;
}

int main()
{
    cin.sync_with_stdio(false);

    cin >> N >> M;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> lab[i][j];
        }
    }

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            if(!lab[i][j]) buildWall(i, j, 1);
        }
    }

    cout << maxSafeArea << endl;
    
    return 0;
}
