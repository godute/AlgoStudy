#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int d[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
bool is_bound(int i, int j, int m, int n) {
    return i>=0 && i<m && j >= 0 && j < n;
}
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int msize = 0;
    bool **visited = new bool*[m];
    for(int i = 0; i < m; i++)
        visited[i] = new bool[n];
    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++)
            visited[i][j] = false;
    queue<pair<int, int>> q;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(!visited[i][j] && picture[i][j] != 0) {
                visited[i][j] = true;
                q.push(make_pair(i, j));
                int result = 0;
                while(!q.empty()) {
                    int i = q.front().first;
                    int j = q.front().second;
                    q.pop();
                    result++;
                    for(int k = 0; k < 4; k++) {
                        int ni = i + d[k][0];
                        int nj = j + d[k][1];
                        if(is_bound(ni, nj, m, n) && !visited[ni][nj] && picture[i][j] == picture[ni][nj]) {
                            visited[ni][nj] = true;
                            q.push(make_pair(ni, nj));
                        }
                    }
                }
                msize = result > msize ? result : msize;
                number_of_area++;
            }
        }
    }
    max_size_of_one_area = msize;
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}