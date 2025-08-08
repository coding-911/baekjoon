import sys

answer = 0
N = int(sys.stdin.readline())
area = []

for i in range(0,N):
    area.append(list(map(int, sys.stdin.readline().split(' '))))

# 여기서 물이 들어오지 않을 때를 고려하여 [0]를 추가해줘야 함
heights = [0] + sorted({h for row in area for h in row})

# 물이 들어오지 않았을 때 + 실제 존재하는 높이 만큼 물이 들어왔을 때
for water in heights:
    print("== water level ", water, "==")
    visited = [[0]*N for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > water and visited[i][j]==0: 
                cnt += 1
                print(cnt, "번째 안전 영역")
                visited[i][j] = 1
                stack = []
                stack.append((i,j))
                while stack:
                    x, y = stack.pop(0)
                    for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<N and 0<=ny<N and area[nx][ny] > water and visited[nx][ny]==0:
                            visited[nx][ny] = 1
                            stack.append((nx,ny))
    print("cnt: ", cnt)
    if cnt >= answer: answer = cnt
print(answer)