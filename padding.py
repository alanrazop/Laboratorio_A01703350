"Se importan las librerías que se van a ocupar"
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

"Dimension de la imagen: 920x1900
"

"Funcion que convierte las matrices con numpy"
def padding (mat, rows, cols):
    mat = np.matrix(mat)
    "Más renglones y columnas que la matriz original"
    m = math.floor((rows - np.shape(mat)[0]) / 2)
    n = math.floor((cols - np.shape(mat)[1]) / 2)
    
    "Matriz final"
    final = np.zeros((rows, cols))
    
    
    
