# 1569
def taxi_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
val_range = [
    [min(points, key=lambda x: x[i])[i], max(points, key=lambda x: x[i])[i]] for i in range(2)
]
max_dist = max([val_range[i][1] - val_range[i][0] for i in range(2)])
flag = False
for i in range(val_range[0][0], val_range[0][1] + 1):
    for j in range(val_range[1][0], val_range[1][1] + 1):
        d_0 = taxi_distance(points[0], [i, j])
        if all([taxi_distance([i, j], k) == d_0 for k in points]):
            flag = True
            break
print(max_dist if flag else -1)
