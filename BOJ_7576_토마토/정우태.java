import java.util.*;
class Node {
	public int i, j;
	public Node(int i, int j) {
		this.i = i;
		this.j = j;
	}
}
public class 정우태  {
	public static int H, W;
	public static int[][] Map = new int[8][8];
	public static int[][] temp_Map = new int[8][8];
	public static int[][] d = { {-1, 0}, {1, 0}, {0, 1}, {0, -1}};
	public static int Answer = 0;
	public static ArrayList<Node> list = new ArrayList<Node>();
	public static Queue<Node> q = new LinkedList<Node>();
	public static void Print() {
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				System.out.print(temp_Map[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	public static void DFS(int index, int depth) {
		if(depth == 3) {
			int temp = Solution();
			//Print();
			Answer = Answer > temp ? Answer : temp;
			return;
		}
		for(int i = index; i < H*W; i++) {
			int next_i = i/W;
			int next_j = i%W;
			if(Map[next_i][next_j] == 0) {
				Map[next_i][next_j] = 1;
				DFS(i+1, depth+1);
				Map[next_i][next_j] = 0;
			}
		}
	}
	public static int Solution() {
		int result = 0;
		Spread();
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				if(temp_Map[i][j] == 0)
					result++;
			}
		}
		return result;
	}
	public static boolean is_bound(int i , int j) {
		return i>=0 && i< H && j>= 0 && j < W;
	}
	public static void Spread() {
		for(int i = 0; i < H; i++)
			for(int j = 0; j < W; j++)
				temp_Map[i][j] = Map[i][j];
		for(int i = 0; i < list.size(); i++) 
			q.offer(list.get(i));
		while(!q.isEmpty()) {
			Node node = q.poll();
			for(int k =0 ; k < 4; k++) {
				int next_i = node.i + d[k][0];
				int next_j = node.j + d[k][1];
				if(is_bound(next_i, next_j)) {
					if(temp_Map[next_i][next_j] == 0) {
						temp_Map[next_i][next_j] = 2;
						q.offer(new Node(next_i, next_j));
					}
				}
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		H = sc.nextInt();
		W = sc.nextInt();
		for(int i = 0; i < H; i++)  {
			for(int j = 0; j < W; j++) {
				Map[i][j] = sc.nextInt();
				if(Map[i][j] == 2) {
					list.add(new Node(i, j));
				}
			}
		}
		DFS(0, 0);
		System.out.println(Answer);
	}
}