import json
import math
#distance in cm
#angle in degrees from the atan function converted
#time in seconds
file = open("raw-data.json")
data = json.load(file)

#TODO ehm koukat na videa fakt pomalu a opisovat číslíčka
#vyčíslit chybu.

forward = data["forward"]
backward = data["backward"]


def calculate(values):
    procesed = []
    for video in values:
        displacement = abs(video["p1"][0]-video["p2"][0])/abs(video["p1"][1]-video["p2"][1])
        time = abs(video["t1"]-video["t2"])
        angle_change = abs(video["a1"]-video["a2"])

        velocity=displacement/time
        spin = angle_change/time
        angle = ((math.atan(velocity))/math.pi)*180
        procesed.append({
            "velocity":velocity,
            "angle":angle,
            "spin":spin
        })
    return procesed

forward_processed = calculate(forward)
backward_processed = calculate(backward)

data = json.dumps({"forward":forward_processed,
        "backward":backward_processed},indent=3)

out_file = open("processed.json","w")
out_file.write(data)