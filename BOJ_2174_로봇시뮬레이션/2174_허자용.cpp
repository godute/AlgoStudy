#include <iostream>
#include <utility>

using namespace std;

int A, B, N, M;
int plane[100][100] = {0, };
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int crashCode = 0;
int crashedRobotID = -1;

void checkWall(pair<int, int> c) {
    if(c.first < 0 || c.first > A - 1 || c.second < 0 || c.second > B - 1) crashCode = -1;
    return;
}

class Robot
{
private:
    int ID_number;
    pair<int, int> position;
    int direction;
public:
    void setInitialValue(int idn, int x, int y, int dir) {
        ID_number = idn;
        position.first = x;
        position.second = y;
        direction = dir;
        plane[x][y] = idn;
    }

    void rotate(int count) {
        direction = (direction + count) % 4;
    }

    void move(int count) {
        for(int i = 0; i < count; i++) {
            plane[position.first][position.second] = 0;
            position.first += dx[direction];
            position.second += dy[direction];
            checkWall(position);
            if(crashCode == -1) {
                crashedRobotID = ID_number;
                return;
            }
            else if(plane[position.first][position.second]) {
                crashedRobotID = ID_number;
                crashCode = plane[position.first][position.second];
                return;
            }
            else plane[position.first][position.second] = ID_number;
        }
    }
};

Robot *Bot = new Robot[100];

int main()
{
    cin >> A >> B >> N >> M;
    int init_x, init_y, init_dir;
    char tempdir;
    int robotID, count;
    char command;
    for(int i = 0; i < N; i++) {
        cin >> init_x >> init_y >> tempdir;
        switch(tempdir) {
            case 'W': init_dir = 0; break;
            case 'N': init_dir = 1; break;
            case 'E': init_dir = 2; break;
            case 'S': init_dir = 3; break;
        }
        Bot[i].setInitialValue(i+1, init_x -1, init_y - 1, init_dir);
    }

    for(int i = 0; i < M; i++) {
        cin >> robotID >> command >> count;
        if(crashCode) continue;
        switch(command){
            case 'L':
                Bot[robotID - 1].rotate(3*count);
                break;
            case 'R':
                Bot[robotID - 1].rotate(count);
                break;
            case 'F':
                Bot[robotID - 1].move(count);
                break;
        }
    }
    if(crashCode == -1) cout << "Robot " << crashedRobotID << " crashes into the wall" << endl;
    else if(crashCode) cout << "Robot " << crashedRobotID << " crashes into robot " << crashCode << endl;
    else cout << "OK" << endl;

    return 0;
}
