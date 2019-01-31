

#include <stdio.h>
#include <queue>

using namespace std;

int dr[4] = {1,0,-1,0};
int dc[4] = {0,1,0,-1};

int N, M;

queue < pair < int, int > > que;
queue < pair < int, int > > loc_virus;
queue < pair < int, int > > loc_virus_c;

int mat[10][10];
int mat_c[10][10];
bool visited[10][10] = {0, };
bool visited_c[10][10] = {0, };

int n_safe = 0;
int n_virus = 0;
int n_safe_ans;
int count_safe = 0;
int count_safe_min = 100;




void bfs(){
    count_safe = 0;
    // 격자판 복사
    for (int i=1;i<=N;i++){
        for(int j=1;j<=M;j++){
            mat_c[i][j] = mat[i][j];
            visited_c[i][j] = false;
        }
    }
    loc_virus_c = loc_virus;
    while(!loc_virus_c.empty()){
        
        int now_virus_row = loc_virus_c.front().first;
        int now_virus_col = loc_virus_c.front().second;
        loc_virus_c.pop();
        que.push(make_pair(now_virus_row,now_virus_col));
        
        while(!que.empty()){
        
            int now_row = que.front().first;
            int now_col = que.front().second;
            
            que.pop();
        
            // 종료조건 없음
        
            // 탐색 조건
            for(int i = 0;i<4;i++){
                int nxt_row = now_row + dr[i];
                int nxt_col = now_col + dc[i];
                if(nxt_row <= N && nxt_row >= 1 && nxt_col <= M && nxt_col >= 1){
                    if(mat[nxt_row][nxt_col] == 0 && visited_c[nxt_row][nxt_col] == false){
                        visited_c[nxt_row][nxt_col] = true;
                        count_safe = count_safe + 1;
                        que.push(make_pair(nxt_row,nxt_col));
                        
                    }
                }
            }
        }
    }
}


void dfs(int now, int cnt){
    
    if (cnt == 3){  // 종료조건
        bfs();
        if(count_safe<count_safe_min){
            count_safe_min = count_safe;
        
        }
    }
    else {
        for(int i = now; i < N*M; i++){
            int nxt_row = (i/M) + 1;
            int nxt_col = (i%M) + 1;
            if (mat[nxt_row][nxt_col] == 0){
                mat[nxt_row][nxt_col] = 1;
                dfs(i + 1, cnt + 1);
                mat[nxt_row][nxt_col] = 0;
            }
        }
    }
}




int main(){
    scanf("%d %d", &N, &M);
    for (int i = 1;i<=N;i++){ // 격자 입력
        for(int j=1;j<=M;j++){
            scanf("%d", &mat[i][j]);
            if(mat[i][j] == 0){
                n_safe = n_safe + 1;
            }else if(mat[i][j] == 2){
                n_virus = n_virus + 1;
                loc_virus.push(make_pair(i,j));
            }
        }
    }
    
    dfs(0,0);
    n_safe_ans = n_safe - 3 - count_safe_min;
    printf("%d\n",n_safe_ans);

    
}



// 초기화
