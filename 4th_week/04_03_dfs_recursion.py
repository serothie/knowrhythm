# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []


# 구현해보세요!

def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!

# 재귀함수를 통해서는 무한정 깊어지는 노드가 있는 경우 에러가 생길 수 있습니다!
#
# 예전에 저희가 탈출조건 없이 반복시켰더니 RecursionError 라는
# 에러를 발생시켰던 것과 같이 DFS 의 깊이가 무한정 깊어지면 에러가 발생할 수 있기 때문입니다!