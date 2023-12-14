paper_speed_values0 = {
    40 : 0.65,
    50 : 0.5,
    60 : 0.35,
    70 : 0.1,
    80 : -0.15,
    90 : -0.3,
}
paper_speed_values3 = {
    40 : 0.4,
    50 : 0.25,
    60 : 0.1,
    70 : -0.15,
    80 : -0.3,
    90 : -0.5
}

paper_spin_values3 = {
    40 : 55,
    50 : 45,
    60 : 30,
    70 : 20,
    80 : 7,
    90 : 0
}
paper_spin_values0 = {
    40 : 25,
    50 : 17,
    60 : 10,
    70 : 2,
    80 : -10,
    90 : -15
}

HRC = {
    0 :(paper_spin_values0,paper_speed_values0),
    0.3 : (paper_spin_values3,paper_speed_values3)
}

from simulator import Simulator
import math
def testing(ex):
    spin_values,speed_values = HRC[ex]
    for angle in spin_values:

        simulator = Simulator(velocity=-2,angle=angle,spin=-60)


testing(0)
testing(0.3)