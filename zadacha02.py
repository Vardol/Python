# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

matrix = [[False,False,False], [False,False,True], [False,True,False], [False,True,True], [True,False,False], [True,False,True], [True,True,False], [True,True,True]]
boolValueLeft = False
boolValueRight = False
boolResult = True
for i in range(0, 8) :
    boolValueLeft = -(matrix[i][0] or matrix[i][1] or matrix[i][2])
    boolValueRight = -matrix[i][0] and -matrix[i][1] and -matrix[i][1]
    print(matrix[i], " - ", boolValueLeft == boolValueRight)
    if(boolValueLeft != boolValueRight):
        boolResult = False

if boolResult: print('Утверждение верно')
else: print('Утверждение НЕ верно')