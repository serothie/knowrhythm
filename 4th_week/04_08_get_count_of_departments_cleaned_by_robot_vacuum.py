from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 모두 탐색! : BFS or DFS

# 방향 전진 수식화
#        r    c
# 북   -1  0
# 동   0    1
# 남   1    0
# 서   0  -1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 왼쪽 회전 수식화
# rotate 라는 함수를 쓰면 방향의 인덱스가 +3 % 4 한다는 것을 알 수 있습니다!
# 왼쪽 회전 방향 전환
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4

# 후진 회전 수식화
# 후진하는 방향 전환
def get_d_index_when_go_back(d):
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n, m = len(room_map), len(room_map[0]) # 2차원 배열나오면 묻따 행/열 길이 구하자
    count_of_departments_cleaned = 1
    room_map[r][c] = 2

    # BFS 관점
    # 1. 루트 노드를 큐에 넣는다
    # 2. 현재 큐의 노드를 빼서 visited에 추가한다
    # 3. 현재 방문한 노드와 인접 노드 중 방문하지 않은 노드를 큐에 추가한다
    # 4. 2부터 반복한다
    # 5. 큐가 비면 탐색 종료한다.
    queue = deque([[r,c,d]]) # 1. 루트 노드에 로청의 방향까지 저장해야한다.
    while queue:
        r, c, d = deque.popleft(queue)
        temp_d = d

        for i in range(4): # 동서남북
            temp_d = get_d_index_when_rotate_to_left(temp_d) # 회전
            new_r, new_c = r + dr[temp_d], c + dc[temp_d] # 이동
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0: # 청소여부까지 판단
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2 # CLENED = 2
                queue.append([new_r, new_c, temp_d])
                break
            elif i == 3: # 한 바퀴 회전을 마친 경우
                temp_d = get_d_index_when_go_back(d) # 처음 방향을 기준으로 후진해야함
                new_r, new_c = r + dr[temp_d], c + dc[temp_d] # 이동
                queue.append([new_r, new_c, d])
                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))