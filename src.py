import copy
import math


class mylist(list):

    def __getitem__(self, n):
        return list.__getitem__(self, n)


class Node:

    def __init__(self, d, board, parent=None):
        self.state = State(d=d, board=board)
        self.parent = parent

    def is_goal(self):
        return self.state._goal_check()


class DFS():

    def __init__(self):
        self.explored = []

    def backtrack(self, node):
        while node.state.d < ((int(p / N) + 1) * N):
            c = node.state.d % N
            for r in range(0, N):
                if node.state.board[r][c] != 0 or not node.state.is_square_safe(r, c):
                    continue

                child = copy.deepcopy(node)
                child.state.board[r][c] = 1
                child.state.archer_count = node.state.archer_count + 1
                child.state.d = (node.state.d + 1)
                child.parent = node

                if child.is_goal():
                    solution(child.state.board, N)
                    exit()
                else:
                    self.backtrack(child)

            node.state.d = node.state.d + 1
        return False


def solution(board, N):
    for i in range(0, N):
        print(str(board[i]))


class State:

    def __init__(self, d, board):
        self.archer_count = 0
        self.tree_count = 0
        self.d = d
        self.board = board

    def _goal_check(self):

        if self.archer_count != p:
            return False
        return True

    def is_square_safe(self, r, c):

        rmul = [-1, 1, 0, 0, 1, 1, -1, -1]
        cmul = [0, 0, -1, 1, 1, -1, 1, -1]

        for k in range(0, 8):
            i = 1
            try:
                while True:
                    if self.board[r + i * rmul[k]][c + i * cmul[k]] == 1: return False
                    if self.board[r + i * rmul[k]][c + i * cmul[k]] == 2: break
                    i += 1
            except IndexError as e:
                pass

        return True


if __name__ == '__main__':

    lines = tuple(open("input.txt", 'r'))
    lines = [l.strip() for l in lines]
    print(lines)
    N = int(lines[0])
    p = int(lines[1])

    input_board = mylist()
    for i in range(0, N):
        row = mylist()
        row.extend([int(l) for l in list(lines[2 + i])])
        input_board.append(row)

    node = Node(d=0, board=input_board)

    dfs = DFS()
    status = dfs.backtrack(node)

    solution(node.state.board, N)
