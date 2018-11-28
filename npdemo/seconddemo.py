import sys
import matplotlib.pyplot as plt
import numpy as np

para1 = int(sys.argv[1])
para2 = int(sys.argv[2])
data = np.arange(para1, para2)
plt.plot(data)

plt.show()
