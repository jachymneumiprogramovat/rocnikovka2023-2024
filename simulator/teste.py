paper_values30 = {
    0:-30,
    20:-15,
    40:20,
    50:30
}

paper_values60 = {
    0:-60,
    20:-30,
    40:-15,
    60:0,
    70:10
}

paper_value120 = {
    0: -120,
    20: -90,
    40: -75,
    60: -55,
    80: -45,
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
    spin_values = spins[abs(spin)]
    for angle in spin_values:
        simulator = Simulator(
            velocity=2,angle=math.radians(angle),spin=spin,
            CoSF=0.2,VRC=0.9,Radius=0.025,D=0,AMC=0.4
        )
        print("---",angle,"---")

        simulated_value = simulator.simulate()
        difference_spin = spin_values[angle]-simulated_value[0]
        difference_speed = speed_values[angle] - simulated_value[1]
        print("target speed",speed_values[angle])
        print("simulated:",simulated_value[0])
        print("speed difference:",difference_speed)
testing(-30)
testing(-60)
testing(-120)