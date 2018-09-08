
def calc_score(matrix):
    score = 0
    for w in matrix:
        for i in w:
            if i % 2 == 0:
                score += 1
    return score

h, w = map(int, raw_input().split())
matrix = []
for i in range(h):
    matrix.append([ int(j) for j in raw_input().split()])

result = []
for i in range(h):
    for j in range(w):
        if matrix[i][j] % 2 == 1:
            matrix[i][j] -= 1
            if j + 1 < w:
                matrix[i][j+1] += 1
                result.append((i,j,i,j+1))
            elif i + 1 < h:
                matrix[i+1][j] += 1
                result.append((i,j,i+1,j))
            score = calc_score(matrix)

print(len(result))
for data in result:
    print("%d %d %d %d" % data)
