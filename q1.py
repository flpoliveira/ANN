import numpy as np
k = 8
somatorioX = 0+0.5+1+1.5+2+2.5+3+3.5
somatorioX2 = (0.5)**2+1+(1.5)**2+2**2+2.5**2+3**2+3.5**2
somatorioY = 1.1066 + 1.792 + 3.0026 + 3.9783 + 5.0893 + 5.922 + 7.2379 + 7.9519
somatorioYX = (0.5*1.792)+3.0026+(1.5*3.9783)+2*5.0893+2.5*5.922+3*7.2379+3.5*7.9519

a = [[k, somatorioX], [somatorioX, somatorioX2]]
print(a)
b = [somatorioY, somatorioYX]
print(b)
c = np.array(a)
d = np.array(b)

print(np.linalg.solve(c,d))