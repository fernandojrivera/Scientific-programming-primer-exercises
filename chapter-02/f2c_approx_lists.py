n = 10
F = [0 + i*10 for i in range(n+1)]
C = [(f - 32)*(5.0/9) for f in F]
C_hat = [(f - 30)/2 for f in F]
table = [[f, c, ch] for f, c, ch in zip(F, C, C_hat)]
table.insert(0, ["F", "C", "C^"])

print("----------------------")
for i in range(n+2): # n+2 because we added headers
    if i==0:
        print(table[i])
        print("----------------------")
    else:
        print("%.2f, %.2f, %.2f" %(table[i][0], table[i][1], table[i][2]))
print("----------------------")