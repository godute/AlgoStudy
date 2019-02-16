#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
enum{NONE=-1,TOMATO,WELL};
/*
정수 M,N // M 은 상자의 가로 칸 수 , N은 상자의 세로 칸 수 
하나의 상자에 저장된 토마토들의 정보 // 1 익은 토마토 0 익지 x -1 토마토없음
 */
int dir_x[4] = {1,-1,0,0};
int dir_y[4] = {0,0,1,-1};
int M,N;
int tomato[1001][1001];

int findWELL()
{
	int days = -1;
	queue <pair <int,int> > que;

	//익었으면 시작한다. 
	for(int i = 0 ; i < N; i++)
	{
		for (int j = 0 ; j <M;j++)
		{
			if (tomato[i][j] == WELL)
			{
				pair<int, int> p(i, j);
				que.push(p);
			}
		}
	}

	while(!que.empty())
	{
		int size = que.size();
		// size가 끝나면 하루가 지났다.
		while(size--)
		{
			int tmp_x = que.front().first;
			int tmp_y = que.front().second;
			que.pop();
			
			for(int i = 0 ; i < 4 ; i ++)
			{
				int x = tmp_x;
				int y = tmp_y;

				x+= dir_x[i];
				y+= dir_y[i];
				
				if (x < 0 || y < 0 || x >= N || y >= M)
					continue;
				if (tomato[x][y] != TOMATO)
					continue;

				//토마토가 잘 익었넹 
				tomato[x][y] = WELL;
				pair <int, int> atom(x, y);
				que.push(atom);
			}
		}
		days++;
	}
	
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (tomato[i][j] == TOMATO)
				return -1;
	return days;
}



 int main()
{
	scanf("%d%d",&M,&N);
	
	for (int i =0; i <N;i++)
	{
		for(int j = 0 ; j < M ;j++)
		{
			scanf("%d",&tomato[i][j]);
		}
	}

	
	printf("%d",findWELL());
	return 0;
}


