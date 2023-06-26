from car import Car

class ElectricCar(Car):
	"""Defining the child class"""
	def __init__(self, make, model, year, mileage, battery):
		super().__init__(make, model, year, mileage)
		self.battery = battery
		self.default_color = "default color"

	def get_info(self):
		print(f"This electric car has {self.mileage} and this much battery capacity {self.battery}.")

	def change_color(self, new_color):
		self.default_color = new_color
		print(f"Your car paint job has been ordered. New color selected: {self.default_color}.")


my_electric = ElectricCar("Toyota", "Model-e", 2015, 200, 20)
my_electric.get_info()
my_electric.change_color("light-blue")