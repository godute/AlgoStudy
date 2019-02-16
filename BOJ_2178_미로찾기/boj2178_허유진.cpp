#include <iostream>
#include <queue>
#include <utility>

using namespace std;

enum{NONE,PATH,VISITED};
//어디로 갈까?
int dir_x[4] = { 1,0,-1,0 };
int dir_y[4] = { 0,1,0,-1 };

int maze[101][101] = { 0, };
int M, N;

int bfs_find_path(int x, int y)
{
	int cnt = 0;

	queue<pair<int, int> > Q;
	pair<int, int> p(x, y);
	pair<int,int> tmp;
        pair<int, int> atom;
	
	//일단 하나 넣고 
	Q.push(p);
        maze[p.first][p.second] = VISITED;
	

	while (!Q.empty())
	{
		int size = Q.size();
		
		//이 while 문이 끝나면 depth가 1 증가 
		while (size--)
		{
			//Q에서 하나 꺼냅니다. 
			atom = Q.front();
			Q.pop();
			
			//출구에 도착 ! cnt 1증가해서 반환 ^_^ 
			if ((atom.first == N) && (atom.second == M))
				return cnt+1;

			for (int i = 0; i < 4; i++)
			{
				//tmp 에 원래 것을 저장하고 방향을 바꾸면서 고고 
				tmp = atom;
			
				tmp.first += dir_x[i];
				tmp.second += dir_y[i];
				
				int tmp_x = tmp.first;
				int tmp_y = tmp.second;
				
				
				//범위 밖이면 다시 for문으로 돌아가용 
				if (tmp_x < 1 || tmp_y < 1 || tmp_x > N || tmp_y > M)
					continue;
				//길이 아니여도 다시  for문으로 고고 
				else if (maze[tmp_x][tmp_y] != PATH)
					continue;
				else
				{
					//방문 코드 삽입 주의 *^^* 
					Q.push(tmp);
                    			maze[tmp.first][tmp.second] = VISITED;
				}
			}
		}
		cnt++;

	}
	return cnt;
}

int main()
{
	scanf("%d%d", &N,&M);

	for (int i = 1; i < N + 1; i++)
		for (int j = 1; j < M + 1; j++)
			scanf("%1d", &maze[i][j]);

	printf("%d\n", bfs_find_path(1, 1));

	return 0;
}
