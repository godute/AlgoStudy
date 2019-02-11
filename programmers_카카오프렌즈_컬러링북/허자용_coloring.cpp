// #include <iostream>
#include <vector>

using namespace std;

bool visited[100][100];
int current_area = 0;

bool isOutOfRange(int m, int n, int r, int c) {
    if (r < 0 || r > m - 1 || c < 0 || c > n - 1) return true;
    else return false;
}

void areaCount(int m, int n, int r, int c, vector<vector<int> > picture) {
    current_area++;
    visited[r][c] = true;
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};
    int next_r;
    int next_c;

    for(int i = 0; i < 4; i++) {
        next_r = r + dr[i];
        next_c = c + dc[i];
        if(isOutOfRange(m, n, next_r, next_c)) continue;
        else if(picture[next_r][next_c] == picture[r][c] && !visited[next_r][next_c]) {
            areaCount(m, n, next_r, next_c, picture);
        }
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int> > picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    for(int i = 0; i < 100; i++) {
        for(int j = 0; j < 100; j++) {
            visited[i][j] = false;
        }
    }

    vector<int> answer(2);

    for(int r = 0; r < m; r++) {
        for(int c = 0; c < n; c++) {
            if(picture[r][c] && !visited[r][c]) {
                current_area = 0;
                number_of_area++;
                areaCount(m,n,r,c,picture);
                if (current_area > max_size_of_one_area) max_size_of_one_area = current_area;
            }
        }
    }

    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

// int main() {
//     vector<vector<int> > pic(6, vector<int>(4, 0));
//     int arr[6][4] = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
//     for(int i = 0; i < 6; i++) {
//         for(int j = 0; j < 4; j++) {
//             pic[i][j] = arr[i][j];
//         }
//     }
//
//     vector<int> answer(2);
//     answer = solution(6, 4, pic);
//     cout << answer[0] << "\n" << answer[1] << endl;
//     return 0;
// }
