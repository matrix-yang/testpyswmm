from pyswmm import Simulation

sim = Simulation('D:\SWMMH\Examples\\test2.inp')
#sim.report()
sim.execute()
sim.close()

