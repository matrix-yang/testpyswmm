import src.yang.paramermanager as pm
import numpy as np
from pyswmm import Simulation

pm.readFile()
# 0.011-0.024
manningRange = np.linspace(0.011, 0.024, 10, True)
maxRes, avgRes = [], []
for num in manningRange:
    pm.changeManning(num)

sim = Simulation('D:\SWMMH\Examples\\test2.inp')
# sim.report()
sim.execute()
sim.close()