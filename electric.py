from car import Car

class ElectricCar(Car):
	"""Defining the child class"""
	def __init__(self, make, model, year, mileage, battery):
		super().__init__(make, model, year, mileage)
		self.battery = battery

	def get_info(self):
		print(f"This electric car has {self.mileage} and this much battery capacity {self.battery}.")

my_electric = ElectricCar("Toyota", "Model-e", 2015, 200, 20)
my_electric.get_info()