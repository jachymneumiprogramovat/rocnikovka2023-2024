paper_speed_values0 = {
    40 : 0.56,
    50 : 0.5,
    60 : 0.35,
    70 : 0.1,
    80 : -0.15,
    89 : -0.4,
}
paper_speed_values3 = {
    40 : 0.45,
    50 : 0.3,
    60 : 0.1,
    70 : -0.15,
    80 : -0.34,
    89 : -0.5
}

paper_spin_values3 = {
    40 : 55,
    50 : 42,
    60 : 35,
    70 : 20,
    80 : 7,
    89 : 0
}
paper_spin_values0 = {
    40 : 25,
    50 : 20,
    60 : 13,
    70 : 2,
    80 : -8,
    89 : -17
}

HRCs = {
    0 :(paper_spin_values0,paper_speed_values0),
    0.3 : (paper_spin_values3,paper_speed_values3)
}

from simulator import Simulator
import math
def testing(ex):
    print("\n-----------------ex = ",ex,"--------------------")
    spin_values,speed_values = HRCs[ex]
    for angle in spin_values:

        simulator = Simulator(
            velocity=2,angle=math.radians(angle),spin=-60,
            CoSF=0.2,VRC=0.9,HRC=ex,Radius=0.025,D=0,AMC=0.4)
        
        simulated_value = simulator.simulate_roling()
        difference_spin = abs(spin_values[angle]-simulated_value[0])
        difference_speed = abs(speed_values[angle] - simulated_value[1])
        print("---",angle,"---")
        #print("spin dif:",difference_spin<3, difference_spin)
        #print(f'sim spin:{simulated_value[0]}  target:{spin_values[angle]}')
        #print("speed dif:",difference_speed<0.2,difference_speed)
        #print(f'sim speed:{simulated_value[1]}  target:{speed_values[angle]}')
        #print(simulator.get_roling_backwards_bounce(), simulated_value[1]<0)


testing(0)
testing(0.3)