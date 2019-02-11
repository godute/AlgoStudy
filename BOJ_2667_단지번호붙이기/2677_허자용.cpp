#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
bool visited[25][25] = {false, };
int land[25][25] = {0, };
int N, housecount;
vector<int> numberOfHouse;

bool isOutOfRange(int r, int c) {
    if (r < 0 || r > N - 1 || c < 0 || c > N - 1) return true;
    else return false;
}

void countHouse(int r, int c) {
    housecount++;
    visited[r][c] = true;
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};
    int next_r;
    int next_c;

    for(int i = 0; i < 4; i++) {
        next_r = r + dr[i];
        next_c = c + dc[i];
        if(isOutOfRange(next_r, next_c)) continue;
        else if(land[next_r][next_c] == land[r][c] && !visited[next_r][next_c]) {
            countHouse(next_r, next_c);
        }
    }
}

int main()
{
    cin >> N;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            scanf("%1d", &land[i][j]);
        }
    }

    int blockcount = 0;
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            if(land[r][c] && !visited[r][c]) {
                housecount = 0;
                blockcount++;
                countHouse(r, c);
                numberOfHouse.push_back(housecount);
            }
        }
    }

    cout << blockcount << endl;
    sort(numberOfHouse.begin(), numberOfHouse.end());
    for(int i = 0; i < numberOfHouse.size(); i++) cout << numberOfHouse[i] << endl;

    return 0;
}
