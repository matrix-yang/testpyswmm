from pyswmm import Simulation
from src.yang.paramer import Paramer
import src.yang.paramermanager as pm
import numpy as np
import time
allImpact = 0

manningRange = np.linspace(0.011, 0.024, 10, True)
manning = Paramer(manningRange, 'changeManning')

# N-imperv 0.005-0.05
NimpervRange = np.linspace(0.005, 0.05, 10, True)
Nimperv = Paramer(NimpervRange, 'changeNimperv')

# N-perv 0.005-0.5
NpervRange = np.linspace(0.005, 0.5, 10, True)
Nperv = Paramer(NpervRange, 'changeNperv')

# S-imperv 0.2-10
SimpervRange = np.linspace(0.2, 10, 10, True)
Simperv = Paramer(SimpervRange, 'changeSimperv')

# S-perv 2-10
SpervRange = np.linspace(2, 10, 10, True)
Sperv = Paramer(SpervRange, 'changeSperv')

# Pct-Zero 5-85
PctZeroRange = np.linspace(5, 85, 10, True)
PctZero = Paramer(PctZeroRange, 'changeCZero')
paramers = []
paramers.append(manning)
paramers.append(Nimperv)
paramers.append(Nperv)
paramers.append(Simperv)
paramers.append(Sperv)
paramers.append(PctZero)

subImpact = []

def initInp(paramers):
    for p in paramers:
        str = 'pm.' + p.getName()
        eval(str)(p.get(0))
        pm.saveFile()

def getSubImpact(paramers):
    avg, max = pm.getResult()
    global subImpact
    inpfile=pm.getCurrentInp()
    for p in paramers:
        str='pm.'+p.getName()
        print('---------------',p.nextNum)
        eval(str)(p.nextNum())
        pm.saveFile()
        runModel()
        avgNext, maxNext = pm.getResult()
        subImpact.append(avgNext-avg)
        pm.setinpfile(inpfile)
    return subImpact

def runModel(path='D:\SWMMH\Examples\\test2.inp'):
    sim = Simulation(path)
    sim.execute()

def getAllImpact(tValue):
    avg, max = pm.getResult()
    avgf=float(avg)
    return avgf - tValue

def test():
    global paramers
    global allImpact
    global subImpact
    initInp(paramers)
    runModel()
    allImpact=getAllImpact(0.04)
    getSubImpact(paramers)
    print(subImpact)

test()