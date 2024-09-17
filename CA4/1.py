def convert_string_to_list(input_string):
    result_list = []
    for char in input_string:
        if char == '-':
            result_list.append(0)
        elif char == 'X':
            result_list.append(1)
    return result_list

def find_possible_moves(targetIndex, k, flood_index):
    possible_moves = [[0, 1], [0, -1]]
    if targetIndex[0] == 0:
        possible_moves.append([1, k])
    else:
        possible_moves.append([-1, k])
    filtered_moves = []
    for move in possible_moves:
        new_x = targetIndex[0] + move[0]
        new_y = targetIndex[1] + move[1]
        if new_x < 0 or new_x >= 2 or new_y < 0:
            continue
        if new_y < n:
            if island[new_x][new_y] == 1:
                continue
        if new_y <= flood_index:
            continue
        filtered_moves.append(move)
    return filtered_moves

def canDo(targetIndex, n, k, island, visited, flood_index):
    if targetIndex[1] >= n:
        return True
    if visited[targetIndex[0]][targetIndex[1]]:
        return False
    visited[targetIndex[0]][targetIndex[1]] = True
    possible_moves = find_possible_moves(targetIndex, k, flood_index)
    for move in possible_moves:
        new_x = targetIndex[0] + move[0]
        new_y = targetIndex[1] + move[1]
        if canDo([new_x, new_y], n, k, island, visited, flood_index + 1):
            return True
    return False

query_num = int(input())
for _ in range(query_num):
    n, k = map(int, input().split())
    islandString1 = input()
    islandString2 = input()
    island1 = convert_string_to_list(islandString1)
    island2 = convert_string_to_list(islandString2)
    island = [island1, island2]
    visited = [[False] * n for _ in range(2)]

    targetIndex = [0, 0]

    if canDo(targetIndex, n, k, island, visited, 0):
        print("YES")
    else:
        print("NO")

