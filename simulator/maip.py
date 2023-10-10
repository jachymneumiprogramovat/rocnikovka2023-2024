from simulator import Simulator
import math
simulator = Simulator(
    velocity=2,angle=math.radians(80),spin=-120,CoSF=0.2,VRC=0.9,Radius=0.025,D=0.0019,AMC=0.25
    )
simulator.Simulate()