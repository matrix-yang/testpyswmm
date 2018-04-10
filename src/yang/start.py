import src.yang.paramermanager as pm
import numpy as np
from pyswmm import Simulation
import matplotlib.pyplot as plt
pm.readFile()
# 0.011-0.024
manningRange = np.linspace(0.011, 0.024, 10, True)
maxRes, avgRes = [], []
for num in manningRange:
    pm.changeManning(num)
    pm.saveFile()
    sim = Simulation('D:\SWMMH\Examples\\test2.inp')
    # sim.report()
    sim.execute()
    sim.close()
    avg,max=pm.getResult()
    maxRes.append(max)
    avgRes.append(avg)

plt.figure()
plt.plot(manningRange,maxRes,label="max")
plt.plot(manningRange,avgRes,label="avg")
plt.xlabel('manning')
plt.ylabel('water level')
plt.legend(['max', 'avg'])
plt.show()
