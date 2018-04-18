from pyswmm import Simulation
from src.yang.paramer import Paramer
import src.yang.paramermanager as pm
import numpy as np
allImpact=0

manningRange = np.linspace(0.011, 0.024, 10, True)
manning = Paramer(manningRange,'manningRange')

# N-imperv 0.005-0.05
NimpervRange = np.linspace(0.005, 0.05, 10, True)
Nimperv = Paramer(NimpervRange,'NimpervRange')

# N-perv 0.005-0.5
NpervRange = np.linspace(0.005, 0.5, 10, True)
Nperv = Paramer(NpervRange,'NpervRange')

# S-imperv 0.2-10
SimpervRange = np.linspace(0.2, 10, 10, True)
Simperv = Paramer(SimpervRange,'SimpervRange')

# S-perv 2-10
SpervRange = np.linspace(2, 10, 10, True)
Sperv = Paramer(SpervRange,'SpervRange')

# Pct-Zero 5-85
PctZeroRange = np.linspace(5, 85, 10, True)
PctZero = Paramer(PctZeroRange,'PctZeroRange')
paramers=[]
paramers.append(manning)
paramers.append(Nimperv)
paramers.append(Nperv)
paramers.append(Simperv)
paramers.append(Sperv)
paramers.append(PctZero)

subImpact=[]
def getSubImpact(paramers):
    avg, max = pm.getResult()
    for p in paramers:
        if(p.getName=='manningRange'):
            pm.changeManning(p.next)
        if (p.getName == 'NpervRange'):
            pm.changeManning(p.next)
        if (p.getName == 'manningRange'):
            pm.changeManning(p.next)
        if (p.getName == 'manningRange'):
            pm.changeManning(p.next)
        if (p.getName == 'manningRange'):
            pm.changeManning(p.next)
        if (p.getName == 'manningRange'):
            pm.changeManning(p.next)

def runModel(path='D:\SWMMH\Examples\\test2.inp'):
    sim = Simulation(path)
    sim.execute()

def getAllImpact(tValue):
    avg, max = pm.getResult()
    return avg-tValue
