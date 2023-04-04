# 1569
def is_in_square(center, l, point):
    if max([abs(center[0] - point[0]), abs(center[1] - point[1])]) == l / 2:
        return True
    else:
        return False

# 입력
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

# 저장
val_range = [
    [min(points, key=lambda x: x[i])[i], max(points, key=lambda x: x[i])[i]] for i in range(2)
]
max_dxy = [val_range[0][1] - val_range[0][0], val_range[1][1] - val_range[1][0]]
small, large = (1, 0) if max_dxy[0] >= max_dxy[1] else (0, 1)
const = (val_range[large][0] + val_range[large][1]) / 2
able = [val_range[small][0] + max_dxy[large] / 2, val_range[small][1] - max_dxy[large] / 2]

# 실행
flag = False
for i in able:
    check_point = [const, i] if large == 0 else [i, const]
    if all([is_in_square(check_point, max_dxy[large], j) for j in points]):
        flag = True
        break
if flag:
    print(max_dxy[large])
else:
    print(-1)
