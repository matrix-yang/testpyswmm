from pyswmm import Simulation
import paramermanager as pm

sim = Simulation('D:\SWMMH\Examples\\test2.inp')
#sim.report()
sim.execute()
sim.close()