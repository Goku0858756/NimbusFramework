from phue import Bridge
import random
from time import sleep

class HueController:
    def __init__(self):
        self.name = "Hue Controller Object"
        
        self.b = Bridge(ip="10.0.1.16", username="----")
        # self.bri = 254
        self.command = {'transitiontime': 100, 'on': True, 'bri': 127}
        self.lights = self.b.get_light_objects()

        try:
            self.b.connect()
        except Exception as e:
            print(e)

    def randomize(self):

        # for light in self.lights:
        #     light.brightness = 113
        #     light.xy = [random.random(), random.random()]

        for i in range(1, 100):
            print(i)

            for light in self.lights:
                light.brightness = random.randint(1, 254)
                light.xy = [random.random(),random.random()]
                # sleep(0.50)

    def state(self, state=None):

        if state == 'on':
            print("set lights on")
            # self.b.set_light( [1, 2, 3], 'on', True)
            self.b.set_light(3, self.command)
        elif state == 'off':
            print("Set lights OFF")
            self.b.set_light([1, 2, 3], 'on', False)
        else:
            print("Dont understand")


if __name__ == '__main__':
    h = HueController()
    # h.state(state='on')
    h.randomize()
