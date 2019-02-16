// 18/1/22
// 토마토
// 유형 : bfs, dfs
// https://www.acmicpc.net/problem/7576

#include <stdio.h>
#include <queue>
using namespace std;

int N,M;
int mat[1001][1001];
int zero_cnt = 0;
queue <pair <pair <int, int >, int > > que; //
int dr[4] = {1,0,-1,0};
int dc[4] = {0,1,0,-1};
int tot_zero;
int cnt = 0;
int clk = 0;
int Ans;
int cur_clk;

int main(){
    scanf("%d %d",&M,&N);           // M,N 입력
    for (int i=1;i<=N;i++){         // mat 입력
        for(int j=1;j<=M;j++){
            scanf("%d",&mat[i][j]);
            if(mat[i][j] == 0){
                zero_cnt ++;
            }else if(mat[i][j] == 1){
                que.push(make_pair(make_pair(i,j),0));
            }
            
        }
    }
    
    tot_zero = zero_cnt;
    
    
    
    
    while(!que.empty()){
        int cur_r = que.front().first.first;
        int cur_c = que.front().first.second;
        cur_clk = que.front().second;
        que.pop();
        
        for(int i=0;i<4;i++){
            int nxt_r = cur_r + dr[i];
            int nxt_c = cur_c + dc[i];
            int nxt_clk = cur_clk + 1;
            
            if(nxt_r <=N && nxt_r >= 1 && nxt_c <= M && nxt_c >= 1){
                if (mat[nxt_r][nxt_c] == 0){
                    mat[nxt_r][nxt_c] = 1;
                    que.push(make_pair(make_pair(nxt_r,nxt_c) , nxt_clk));
                    cnt ++;
                }
            }
        }
        
        if(zero_cnt == cnt){
            break;
        }
        
    }
    
    if (zero_cnt == 0){
        printf("%d",0);
    }else if(cnt != zero_cnt){
        printf("%d",-1);
    }else{
        printf("%d",cur_clk+1);
    }
    
    
}
