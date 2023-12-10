import math as math

class Simulator:
    """
    AMC = angular momentum coeficient
    VRC = vertical restitution coeficient
    CoSF = coeficient of sliding friction
    HRC = horizontal restitution coefitient.
    """
    def __init__(
            self,velocity=0, angle=0, spin=0, CoSF=0, VRC=0, HRC=None, Radius=0, D=0, AMC=0
            ) -> None:
        self.angle = angle
        self.velocity = velocity
        self.Vx1 = math.cos(angle) * velocity
        self.Vy1 = math.sin(angle) * velocity
        #print("angle:",math.degrees(self.angle))
        #print("Vx1:",self.Vx1,"Vy1:",self.Vy1)
        self.spin = spin
        #koefitients
        self.u = CoSF
        self.ey = VRC
        self.ex = HRC
        self.R = Radius
        self.D = D
        self.a = AMC
    
    def simulate(self):
        sliding_spin = self.get_sliding_spin()
        sliding_speed = self.get_sliding_speed()
        return sliding_spin,sliding_speed

    def get_sliding_speed(self):
        rebound_speed= self.Vx1 
        - self.u * (1 + self.ey) * math.tan(self.angle) * self.Vx1
        return rebound_speed

    def get_sliding_spin(self):
        rebound_spin = self.spin 
        + (1 + self.ey) * (self.u -(self.D/self.R)) * self.Vy1/(self.a*self.R)
        return rebound_spin
    
    def get_sliding_backwards_bounce(self)->bool:
        return math.tan(self.angle) > 1/(self.u*(1+self.ey))

    def get_griping_speed(self):
        rebound_speed = ((1-self.a*self.ex)*self.Vx1)/(1+self.a) 
        + (self.a*self.R*self.spin*(1+self.ex))/(1+self.a) 
        - (self.D*self.Vy1*(1+self.ex))/(self.R*(1+self.a))
        return rebound_speed
    
    def get_griping_spin(self):
        rebound_spin = ((self.a-self.ex)*self.spin)/(1+self.a) 
        + (self.Vx1*(1+self.ex))/(self.R*(1+self.a)) 
        - (self.D*self.Vy1*(1+self.ey))/((self.R**2)*(1+self.a))
        return rebound_spin