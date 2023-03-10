import sys
sys.stdin = open('text.txt', 'r')
#####
import sys
input = sys.stdin.readline
def check(x, y, a):
    for k in range(9):
        # 가로 세로 검사
        if a == arr[x][k] or a == arr[k][y]:
            return False

    # 검색할 위치 고정
    # 나누고 곱하면 3의 배수가 됨미다
    nx = x // 3 * 3
    ny = y // 3 * 3
    # 박스 검사
    for l in range(3):
        for m in range(3):
            if a == arr[nx + l][ny + m]:
                return False
    return True

def dfs(idx):
    # 종료조건 : 빈칸 다 채우면 출력 후 종료
    if idx == len(stack):
        for ind in arr:
            print(*ind)
        exit(0)
    # idx번째 append 되었던 빈칸 좌표 받아와서
    x, y = stack[idx]
    # 빈칸에 1부터 9까지 넣어보고
    for num in range(1, 10):
        # 넣었을 때 문제 없으면
        if check(x, y, num):
            arr[x][y] = num # 해당 빈칸에 num 넣고 dfs

            dfs(idx + 1)

            arr[x][y] = 0
            # 다른 빈칸에서 문제를 해결하고 돌아왔을 때
            # 이전 빈칸에 넣었던 수가 아닌 새로운 수를 시도하기 위해서
            # 이전에 넣었던 수를 초기화


arr = [list(map(int, input().split())) for _ in range(9)]
stack = []
# 빈칸 찾으면 stack에 append
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            stack.append([i, j])

dfs(0)