#include <vector>
#include <queue>

using namespace std;

// ���� ������ ������ ��� �Լ� ���� �ʱ�ȭ �ڵ带 �� �ۼ����ּ���.
vector<int> solution(int m, int n, vector<vector<int> > picture) {
	int number_of_area = 0;
	int max_size_of_one_area = -1;
	int cnt = -1;

	vector<int> answer(2);

	queue<pair<int, int> > color;

	int dir_x[4] = { -1,1,0,0 };
	int dir_y[4] = { 0,0,-1,1 };
	int curr_color = 0;

	for (int i = 0; i < m * n; i++)
	{
		int col = i / n;
		int row = i % n;

		// �̹� ��ĥ�߰ų� ��ĥ���� �ʴ� ���̸� �н� 
		if ((picture[col][row] == -1) || (picture[col][row] == 0))
			continue;

		// ���ο� ���� ��ĥ�ҰŴϱ� count �ʱ�ȭ 
		cnt = 0;
		
		// ���� ��ġ ���� ����ϰ� ���� 
		color.push(make_pair(col, row));
		curr_color = picture[col][row];
		picture[col][row] = -1;

		while (!color.empty())
		{
			pair<int, int> curr = color.front();
			color.pop();
			cnt++;

			for (int j = 0; j < 4; j++)
			{
				int tmp_x = curr.first + dir_x[j];
				int tmp_y = curr.second + dir_y[j];
				if ((tmp_x >= 0) && (tmp_y >= 0) && (tmp_x < m) && (tmp_y < n) && (picture[tmp_x][tmp_y] == curr_color))
				{
					color.push(make_pair(tmp_x, tmp_y));
					picture[tmp_x][tmp_y] = -1;
				}
			}
		}

		// ���� �߰��ϰ� max �� ���� 
		number_of_area++;
		if (max_size_of_one_area < cnt)
				max_size_of_one_area = cnt;
	}

	answer[0] = number_of_area;
	answer[1] = max_size_of_one_area;
	return answer;
}