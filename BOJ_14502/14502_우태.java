import java.util.*;

class Node {
	public int i, j;
	public Node(int i, int j) {
		this.i = i;
		this.j = j;
	}
}
public class Main {
	public static int N, M, Answer;
	public static int[][] Lap = new int[8][8];
	public static int[][] Temp_Lap = new int[8][8];
	public static int[][] d = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
	public static int[] wall = {0, 0, 0};
	public static Queue<Node> q = new LinkedList<Node>();
	public static void PRINT() {
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				System.out.print(Temp_Lap[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	public static void init() {
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) { 
				Temp_Lap[i][j] = Lap[i][j];
				if(Lap[i][j] == 2)
					q.offer(new Node(i, j));
			}
		}
	}
	public static boolean is_bound(int i, int j ) {
		return (i>=0 && i<N && j >= 0 && j < M) && (Temp_Lap[i][j] == 0);
	}
	public static int count_zero() {
		int result = 0;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(Temp_Lap[i][j] == 0)
					result++;
			}
		}
		return result;
	}
	public static void DFS(int depth, int index) {
		if(depth == 3) {	//벽을 다 세우면?
			for(int i =0; i < 3; i++) {
				int ni = wall[i] / M;
				int nj = wall[i] % M;
				Temp_Lap[ni][nj] = 1;
			}
			
			while(!q.isEmpty()) {
				Node node = q.poll();
				for(int k = 0; k < 4; k++) {
					int ni = node.i + d[k][0];
					int nj = node.j + d[k][1];
					if(is_bound(ni, nj)) {
						Temp_Lap[ni][nj] = 2;
						q.offer(new Node(ni, nj));
					}
				}
			}
			//PRINT();
			
			int res = count_zero();
			init();
			Answer = res > Answer ? res : Answer;
			return;
		}
		for(int i = index; i < N*M; i++) {
			int ni = i / M;
			int nj = i % M;
			if(Temp_Lap[ni][nj] == 0) {	//빈칸이면? 벽세우
				wall[depth] = i;
				DFS(depth + 1, i + 1);
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Answer = 0;
		N = sc.nextInt();
		M = sc.nextInt();
		for(int i = 0; i < N; i++) {
			for(int j =0; j< M; j++) { 
				Lap[i][j] = sc.nextInt();
			}
		}
		init();
		DFS(0, 0);
		System.out.println(Answer);
	}
}
