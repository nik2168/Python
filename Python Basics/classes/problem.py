# define fair calculation for any vechicle and specificly for a bus vehicle

class Vehicle:

    def __init__(self, capacity):
          self.capactiy = capacity

    def get_fare(self):
     return self.capactiy * 100

class Bus(Vehicle):   #inheritance
     
     def __init__(self, capacity):
         super().__init__(capacity)      # parent class constructure
         self.capactiy = capacity

     def get_fare(self):
          raw_fair = super().get_fare()
          service_charge = 0.1 * raw_fair
          total_fair = raw_fair + service_charge
          return total_fair
     


bus1 = Vehicle(30)
print(bus1.get_fare())

bus2 = Bus(30)
print(bus2.get_fare())