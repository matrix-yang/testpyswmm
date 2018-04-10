import src.yang.paramermanager as pm
import numpy as np
from pyswmm import Simulation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.yang.paramer import Paramer
pm.readFile()
# 0.011-0.024
manningRange = np.linspace(0.011, 0.024, 10, True)
manning= Paramer(manningRange)

# N-imperv 0.005-0.05
NimpervRange=np.linspace(0.005,0.05, 10, True)
Nimperv=Paramer(NimpervRange)

# N-perv 0.005-0.5
NpervRange=np.linspace(0.005,0.5, 10, True)
Nperv=Paramer(NpervRange)

# S-imperv 0.2-10
SimpervRange=np.linspace(0.2,10, 10, True)
Simperv=Paramer(SimpervRange)

# S-perv 2-10
SpervRange=np.linspace(2,10, 10, True)
Sperv=Paramer(SpervRange)

# Pct-Zero 5-85
PctZeroRange=np.linspace(5,85, 10, True)
PctZero=Paramer(PctZeroRange)

maxRes, avgRes = [], []
for num in range(10):

    #调整曼宁
    pm.repliceManning('gq1','j1','j2',str(manning.get(num)))
    pm.repliceManning('gq2', 'j2', 'j3', str(manning.get(num)))
    pm.repliceManning('gq3', 'j3', 'pfk1', str(manning.get(num)))

    #调整汇水面参数
    pm.changeSimperv(Simperv.get(num))
    pm.changeSperv(Sperv.get(num))
    pm.changeNimperv(Nimperv.get(num))
    pm.changeNperv(Nperv.get(num))
    pm.changeCZero(PctZero.get(num))

    # pm.changeManning(num)
    pm.saveFile()
    sim = Simulation('D:\SWMMH\Examples\\test2.inp')
    # sim.report()
    sim.execute()
    sim.close()
    avg,max=pm.getResult()
    maxRes.append(max)
    avgRes.append(avg)

fig=plt.figure()
ax = Axes3D(fig)
# plt.plot(range(10),maxRes,label="max")
# plt.plot(range(10),avgRes,label="avg")
X, Y = np.meshgrid(manningRange, SimpervRange)
ax.plot_surface(manningRange, SimpervRange, avgRes, rstride=1, cstride=1, cmap='rainbow')
# plt.xlabel('manning')
# plt.ylabel('water level')
# plt.legend(['max', 'avg'])
plt.show()
