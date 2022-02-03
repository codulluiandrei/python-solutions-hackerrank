X = int(input())
Y = int(input())
Z = int(input())
N = int(input())
X = X + 1
Y = Y + 1
Z = Z + 1
temp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(temp_list)