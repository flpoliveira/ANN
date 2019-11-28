import numpy as np
import math
y = [0.918, 1.0959, 1.4191, 1.7456, 2.0194, 2.6954]
yLinha = []
somatorioYlinha = 0
for i in y:
	yLinha.append(math.log(i))
	somatorioYlinha+=math.log(i)
x = [-2, -1.5, -1, -0.5, 0, 0.5]
somatorioX = 0
somatorioX2 = 0
somatorioYlinhaX = 0
aux = 0
for i in x:
	somatorioX+=i
	somatorioX2+=i**2
	somatorioYlinhaX+=(yLinha[aux]*i)
	aux+=1

k = 6
a = np.array([[k, somatorioX], [somatorioX, somatorioX2]])
b = np.array([somatorioYlinha, somatorioYlinhaX])

resultado = np.linalg.solve(a,b)
#print(resultado)
print("a = "+str(math.exp(resultado[0]))+", b = "+str(resultado[1]))
