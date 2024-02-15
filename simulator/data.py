from simulator import Simulator

#reading and writing to files
import csv
import json

#math and graphs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

class Data:
    def __init__(self,input_file,output_file) -> None:
        self.input_file :str = input_file
        self.output_file :str = output_file
        self.__get_intervals__(self.input_file)

    def __get_intervals__(self,file) -> None:
        """Load min,max,step values for all the parametrs from a .json file"""

        with open(file) as f:
            data = json.load(f)
            velocity_intervals = data["velocity"]
            self.max_velocity = velocity_intervals["max"]
            self.min_velocity = velocity_intervals["min"]
            self.velocity_step = velocity_intervals["step"]

            spin_intervals = data["spin"]
            self.max_spin = spin_intervals["max"]
            self.min_spin = spin_intervals["min"]
            self.spin_step = spin_intervals["step"]

            angle_intervals = data["angle"]
            self.max_angle = angle_intervals["max"]
            self.min_angle = angle_intervals["min"]
            self.angle_step  = angle_intervals["step"]
            
    def get_min_spin(self) ->dict:
        """Iterate throughout all the parametrs and find for each
          of them the smallest spin for which a backward bounce occurs."""
        
        ans = {}
        for velocity in np.arange(self.min_velocity,self.max_velocity,self.velocity_step):
            for angle in np.arange(self.min_angle,self.max_angle,self.angle_step):
                for spin in np.arange(self.min_spin,self.max_spin,self.spin_step):
                    #print all the simulator koefitiens as a legend in the graph.
                    simulator = Simulator(
                    velocity=velocity,angle=math.radians(angle),spin=-spin,
                    CoSF=0.2,VRC=0.9,HRC=0,Radius=0.025,D=0,AMC=0.4
                    )
                    rebound_speed = simulator.simulate_roling()[1]
                    if rebound_speed<0:
                        ans[velocity,angle] = spin
                        break
        return ans
    
    def write_data(self,file) -> None:
        """Writes all the data in a file"""

        results = self.get_min_spin()
        column_names = ["velocity","angle", "min_spin"]
        with open(file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(column_names)
            for key in results:
                writer.writerow([key[0],key[1],results[key]])
    
    def find_minimum_angle(self) -> list:
        """Gather minimum angle for a speed that a backward bounce can happen."""

        data=pd.read_csv("data.csv")
        velocities = data["velocity"]
        angles = data["angle"]
        
        if angles[0] !=0:    
            vel_labels = [velocities[0]]
            ang_labels = [angles[0]]
        else:
            vel_labels = []
            ang_labels = []

        for i,velocity in enumerate(velocities):
            try:
                if velocity != velocities[i-1] and angles[i]!=0:
                        vel_labels.append(velocity)
                        ang_labels.append(angles[i])
            except:
                pass
        return vel_labels,ang_labels

    def generate_graph(self) -> None:
        """Creates graph from all of the values"""

        data = pd.read_csv('data.csv')
        x=data["velocity"]
        y=data["angle"]
        z=data["min_spin"]
        plt.scatter(x,y,c=z,cmap="viridis")
        
        # Add colorbar
        cbar = plt.colorbar()
        cbar.set_label('minimum spin')

        # axis labels
        plt.xlabel('velocity')
        plt.ylabel('angle')
        plt.title('amogus')

        # Minimum angles labels
        xlabels,ylabels = self.find_minimum_angle()
        plt.plot(xlabels,ylabels,color='red', linestyle='-', marker='', label='Minimum angle for bacwards rebound')

        plt.legend()

        plt.show()

if __name__ == "__main__":
    data = Data("intervals.json","data.csv")
    #data.write_data(data.output_file)
    data.generate_graph()