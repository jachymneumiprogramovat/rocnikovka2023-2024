from simulator import Simulator
import math
class Data:
    def __init__(self) -> None:
        self.spin_step = 5
        self.velocity_step = 0.5
        self.angle_step = 1

        self.spin_max = 1000
        self.spin_min = 0

        self.velocity_max = 10
        self.velocity_min = 1

        self.angle_max = 90
        self.angle_min = 0

    def get_min_omega(self,velocity=1,angle=0,spin=0) ->dict:
        ans = {}
        iteration =0
        while velocity<self.velocity_max:
            while angle<self.angle_max:
                while spin < self.spin_max:
                    iteration+=1
                    simulator = Simulator(
                    velocity=velocity,angle=math.radians(angle),spin=-spin,
                    CoSF=0.2,VRC=0.9,Radius=0.025,D=0,AMC=0.4
                    )
                    rebound_speed = simulator.simulate()[1]
                    if rebound_speed<0:
                        print(velocity,spin,angle,rebound_speed)
                        ans[velocity,angle] = spin
                        break
                    spin += self.spin_step
                    
                spin = self.spin_min
                angle += self.angle_step

            spin = self.spin_min
            angle = self.angle_min
            velocity += self.velocity_step
        return ans
data = Data()
print(data.get_min_omega())