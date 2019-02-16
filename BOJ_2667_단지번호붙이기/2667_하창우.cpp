
#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int N;
bool visited[26][26] = {0,}; // <=== 없거나 위치 바뀌면 오답!
char mat_char[26][26];
queue < pair < int, int > > que;
int drc[4] = {1,0,-1,0};
int cnt_house;
vector < int > ans_list;

void bfs(int now_r,int now_c){
    cnt_house = 0;
    que.push(make_pair(now_r,now_c));
    mat_char[now_r][now_c] = '0';
    
    while(!que.empty()){
        
        int now_r = que.front().first;
        int now_c = que.front().second;
        cnt_house = cnt_house + 1;
        que.pop();
        
        
        // 탐색조건
        for(int i=0;i<4;i++){
            
            int nxt_r = now_r + drc[i];
            int nxt_c = now_c + drc[(i+1)%4];
            
            if(nxt_r<=N && nxt_r >= 1 && nxt_c <= N && nxt_c>=1 && mat_char[nxt_r][nxt_c] == '1'){
                
                que.push(make_pair(nxt_r,nxt_c));
                mat_char[nxt_r][nxt_c] = '0';
                
            }
        }
    }
}


int main(){
    scanf("%d", &N);     // 입력
    
    for(int i=1;i<=N;i++){
        scanf("%s",&mat_char[i][1]);
    }

    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            if(mat_char[i][j] == '1'){
                bfs(i,j);
                
                ans_list.insert(ans_list.end(),cnt_house);
                
            }
        }
    }
    printf("%d\n", (int)ans_list.size());
    sort(ans_list.begin(), ans_list.end()); // 정렬
    for(int i=1;i<=(int)ans_list.size();i++){
        printf("%d\n",ans_list[i-1]);
    }
}

