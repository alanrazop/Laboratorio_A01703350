
import numpy as np

"Se importa numpy"
import numpy as np

"Se establecen las matrices a utilizar" 

mat = np.matrix('1 2 3 4 5 6; 7 8 9 10 11 12; 0 0 1 16 17 18; 0 1 0 7 23 24; 1 7 6 5 4 3')
kernel = np.matrix('1 1 1; 0 0 0; 2 10 3')
row = (np.shape(mat)[0] - (np.shape(kernel)[0]/2) * 2) + 1
col = (np.shape(mat)[1] - (np.shape(kernel)[1]/2) * 2) + 1



final = np.zeros((int(row), int(col)), dtype = int)


"Matriz final"
final = np.zeros((int(row), int(col)), dtype = int)

"Se establece la variable en cero"

num1 = 0
for i in range (np.shape(mat)[0] - np.shape(kernel)[0] + 1):
    for j in range (np.shape(mat)[1] - np.shape(kernel)[1] + 1):
        num1 += np.multiply((mat[i:i + (np.shape(kernel)[0]), j:j + (np.shape(kernel)[1])]), kernel)
        final[i][j] = num1.sum()
        num1 = 0
print(final)