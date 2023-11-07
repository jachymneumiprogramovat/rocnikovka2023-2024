paper_values30 = {
    0:0.65,
    20:1,
    40:1.5,
    50:1.8
}

paper_values60 = {
    0:0.15,
    20:0.51,
    40:0.85,
    60:1.25,
    70:1.35
}

paper_value120 = {
    0: -1,
    20:-0.45,
    40: -0.15,
    60: 0.15,
    80:0.3,
}

speed_values = {
    0:2,
    20:1.7,
    30:1.4,
    40:1.15,
    50:0.75,
    60:0.035,
    70:0.1,
    80:-0.35,
    90:-0.75
}

spins = {
    30:paper_values30,
    60:paper_values60,
    120:paper_value120
}

from simulator import Simulator
import math
def testing(spin):
    print("----------------spin =",spin,"---------------------")
    spin_values = spins[spin]
    for angle in spin_values:
        simulator = Simulator(
            velocity=2,angle=math.radians(angle),spin=spin,
            CoSF=0.2,VRC=0.9,Radius=0.025,D=0,AMC=0.4
        )
        
        difference_spin = spin_values[angle]-simulator.Simulate()[0]
        difference_speed = speed_values[angle] - simulator.Simulate()[1]
        print("---",angle,"---")
        print("spin difference:",difference_spin)
        print("speed difference:",difference_speed)
        print("debuging:",spin_values[angle],simulator.Simulate()[0])
testing(30)
testing(60)
testing(120)

