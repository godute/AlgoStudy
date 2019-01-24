

#include<stdio.h>
#include<queue>
#include<cmath>

using namespace std;

int T;
int N, M;

int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};
int arr[100][100];


int main(){
    int s_r,s_c,e_r,e_c;
    int Answer;

    scanf("%d %d",&N, &M);
    
    s_r = 1;
    s_c = 1;
    e_r = N;
    e_c = M;
    
    char arr_temp[M];
    for (int i=1;i<=N;i++){         //arr 입력
        scanf("%s", arr_temp);
        for(int j=1;j<=M;j++){
            arr[i-1][j-1] = (int)arr_temp[j-1] - 48;
        }
    }
    
    
    
    Answer = -1;
    queue <pair <pair <int, int >, int > > que; // ((row,col),cost) queue 생성
    que.push(make_pair(make_pair(s_r,s_c),1));  // 첫번째 queue push
    //bool visited[100][100] = {false}; // 새로 생성
    
    
    
    while(!que.empty()){
        int row_now = que.front().first.first;
        int col_now = que.front().first.second;
        int cost_now = que.front().second;
        que.pop();
        //arr[row_now-1][col_now-1] = 0; // 방문표시 <=== 중요! <=== 메모리 초과 원인
        
        // 종료조건
        if(row_now == e_r && col_now == e_c){
            Answer = cost_now;
            break;
        }

        //탐색
        for (int i=0;i<4;i++){
            // que push 조건
            
            int row_nxt = row_now + dr[i];
            int col_nxt = col_now + dc[i];
            int cost_nxt = cost_now + 1;
            
            
            if (row_nxt <= N && col_nxt <= M && row_nxt >= 1 && col_nxt >= 1){
                
                if(arr[row_nxt-1][col_nxt-1] == 1){
                    arr[row_nxt-1][col_nxt-1] = 0; // 새 방문표시
                    que.push(make_pair(make_pair(row_nxt,col_nxt),cost_nxt));
                }
            }
        }
    }
    printf("%d",Answer);
}

