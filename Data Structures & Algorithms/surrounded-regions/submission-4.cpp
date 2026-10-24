class Solution {
public:
    void solve(vector<vector<char>>& board) {
        vector<vector<bool>> keep(board.size(), vector<bool>(board[0].size(), false));

        int ROW = board.size();
        int COL = board[0].size();
        // 1) Go through outer, run BFS on any 'O' - Pass 1
        for (int r = 0; r < ROW; ++r) {
            for (int c = 0; c < COL; ++c) {
                if ((r == 0 || r == ROW - 1) || (c == 0 || c == COL - 1)) {
                    if (board[r][c] == 'O') {
                        bfs(board, keep, r, c);
                    }
                }
            }
        }

        // 2) Pass 2 - Find 'O's and change if not in keep
        for (int r = 0; r < ROW; ++r) {
            for (int c = 0; c < COL; ++c) {
                if (board[r][c] == 'O' && !keep[r][c]) {
                    board[r][c] = 'X';
                }
            }
        }
    }

    void bfs(vector<vector<char>>& board, vector<vector<bool>>& keep, int r, int c) {
        if (keep[r][c]) return;

        int ROW = board.size();
        int COL = board[0].size();
        queue<pair<int, int>> q;
        q.push(make_pair(r, c));
        vector<int> directions = {0, 1, 0, -1, 0};
        keep[r][c] = true;

        while (!q.empty()) {
            pair<int, int> top = q.front();
            q.pop();
            
            for (int i = 0; i < directions.size() - 1; ++i) {
                int x = top.first + directions[i];
                int y = top.second + directions[i + 1];

                if (0 <= x && x < ROW && 0 <= y && y < COL && !keep[x][y] && board[x][y] == 'O') {
                    keep[x][y] = true;
                    q.push(make_pair(x, y));
                }
            }
        }
    }
};
