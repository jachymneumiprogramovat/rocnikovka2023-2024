import math as math

class Simulator:
    def __init__(
            self,velocity=0, angle=0, spin=0, CoSF=0, VRC=0, Radius=0, D=0, AMC=0
            #AMC = angular momentum coeficient
            #VRC = vertical restitution coeficient
            #CoSF = coeficient of sliding friction
            ) -> None:
        self.angle = angle
        self.velocity = velocity
        self.Vx1 = math.cos(angle) * velocity
        self.Vy1 = math.sin(angle) * velocity
        #print("angle:",math.degrees(self.angle))
        #print("Vx1:",self.Vx1,"Vy1:",self.Vy1)
        self.spin = spin
        #koefitients
        self.CoSF = CoSF
        self.VRC = VRC
        self.Radius = Radius
        self.D = D
        self.AMC = AMC
    
    def Simulate(self):
        #print(self.velocity,self.spin)
        #print("spin:",self.get_SlidingSpin(),"velocity:",self.get_SlidingVx2())
        sliding_spin = self.get_SlidingSpin()
        sliding_speed = self.get_SlidingVx2()
        return sliding_spin,sliding_speed

    #working proprely
    def get_SlidingVx2(self):
        rebound_speed= self.Vx1 - self.CoSF * (1 + self.VRC) * self.Vy1
        return rebound_speed
    #bruh
    def get_SlidingSpin(self):
        rebound_spin = self.spin + (1 + self.VRC) * (self.CoSF -(self.D/self.Radius)) * self.Vy1/(self.AMC*self.Radius)
        return rebound_spin