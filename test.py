import numpy as np
x = np.arange(-20, 20, 0.1)
y = np.arange(-20, 20, 0.1)
xgrid, ygrid = np.meshgrid(x, y)
print map(lambda x, y: x+y, xgrid, ygrid)

