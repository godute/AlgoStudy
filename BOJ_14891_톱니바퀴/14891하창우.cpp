// 18/1/17
// 톱니바퀴

#include <stdio.h>
#include <cmath>


int T;
int t0;
int t1[4][8];
int p_12[4] = {0,0,0,0}; // 12시 방향의 위치
int p_12_temp;
int same[3]; // 만나는 곳의 같은지 여부
int com_num; // 톱니바퀴 숫자
int com_dir; // 회전 방향
int ans;
int r;
int l;
int p;
int dir_temp;

int main(){
    for(int i = 0;i<4;i++){ // 톱니입력
        scanf("%d",&t0);
        for (int j=0;j<8;j++){
            t1[i][j] = t0/int(pow(10,7-j)) % 10;
        }
    }
    
    scanf("%d",&T);
    for (int test=1;test<=T;test++){
        scanf("%d",&com_num);
        scanf("%d",&com_dir);
        com_num = com_num-1;
 

        for(int i=0;i<3;i++){ // same 입력 (마주하는 톱니가 같으면 1 다르면 0)
            r = (p_12[i]+10)%8;
            l = (p_12[i+1]+6)%8;
            if (t1[i][r] == t1[i+1][l]){
                same[i] = 1;
            }else{
                same[i] = 0;
            }
        }
        
        
        
        if (com_dir > 0){       // 중심(명령된) 톱니 회전
            p_12[com_num] = (p_12[com_num] + 7)%8;
        }else{
            p_12[com_num] = (p_12[com_num] + 9)%8;
        }
        
        
        int m = 1;              // 우측 톱니 회전
        while (com_num+m < 4){
            p = com_num+m;
            
            
            if (m%2 == 0){      //dir_temp 정의
                dir_temp = com_dir;
            }else{
                dir_temp = -1*com_dir;
            }
            
            if (same[p-1] == 0){
                if (dir_temp > 0){
                    p_12[p] = (p_12[p] + 7)%8;
                }else{
                    p_12[p] = (p_12[p] + 9)%8;
                }
                
            }else{
                break;
            }
            m = m+1;
        }
        
        
        
        m = 1;              //좌측 톱니 회전
        while (com_num-m >= 0){
            int p = com_num-m;
            
            if(m%2 == 0){
                dir_temp = com_dir;
            }else{
                dir_temp = -1*com_dir;
            }
            
            if (same[p] == 0){
                if (dir_temp > 0){
                    p_12[p] = (p_12[p] + 7)%8;
                    
                }else{
                    p_12[p] = (p_12[p] + 9)%8;
                }
                
            }else{
                break;
            }
            m = m+1;
        }
    }
    
    
    // 점수 계산
    ans = 0;
    for (int k = 0;k<4;k++){
        if (t1[k][p_12[k]] == 1){
            ans = ans + pow(2,k);
        }
    }
    printf("%d\n",ans);
}


