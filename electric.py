
from car import Car

class ElectricCar(Car):
	"""Defining the child class"""
	def __init__(self, make, model, year, mileage, battery, odometer_reading=None):
		super().__init__(make, model, year, mileage)
		self.battery = battery
		self.default_color = "default color"
		self.odometer_reading = 0 if odometer_reading is None else odometer_reading

	def get_info(self):
		print(f"This electric car has {self.mileage} and this much battery capacity {self.battery}.")

	def change_color(self, new_color):
		self.default_color = new_color
		print(f"Your car paint job has been ordered. New color selected: {self.default_color}.")
	
	def get_odometer_reading(self):
		if self.odometer_reading > 0:
			print((
				f"This car ain't new!\n"
				f"It's current odometer reading is at {self.odometer_reading}.")
				)
		else:
			print("This a brand-new car!")

my_electric = ElectricCar("Toyota", "Model-e", 2015, 200, 20)
my_electric.get_info()
my_electric.change_color("light-blue")
my_electric.get_odometer_reading()
my_other_electric = ElectricCar("Toyota", "Model-e", 2015, 200, 20, 100)
my_other_electric.get_odometer_reading()