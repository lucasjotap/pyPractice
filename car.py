class Car:
	"Attributes"
	def __init__(self, make, model, year, mileage):
		"Defining Attributes"
		self.make = make
		self.model = model
		self.year = year
		self.mileage = mileage

	def get_info(self):
		"Display car attributes"
		print(f"{self.make, self.model, self.year, self.mileage}")

	def update_mileage(self, new_mileage) -> int:
		"Updating mileage"
		self.mileage = new_mileage
		print(f"The car's new mileage is {self.mileage}")

# car = Car("Audi", "A3", 1997, 103)
# car.get_info()
# car.update_mileage(105)
