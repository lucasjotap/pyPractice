class Person:
	"""Defining a class to represent people who enter the establishment."""
	def __init__(self, name, age):
		self.name = name 
		self.age = age  
	
	def get_name(self):
		name = f"Costumer: {self.name}"
		return name 

	def get_age(self):
		age = f"Age: {self.age}"
		return age 

class Costumer(Person):
	"""Creating child class to create costumers."""
	def __init__(self, name, age, account_num=None, costumer=None):
		super().__init__(name, age)
		self.account_num = account_num
		self.costumer = costumer if costumer else False

	def get_account_num(self):
		if self.account_num:
			account_num = f"Account number: {self.account_num}"
			return account_num
		else:
			msg = "This costumer doesn't have an account yet."
			return msg

	def get_costumer_status(self):
		if self.costumer and self.account_num:
			msg = (
			"This person is a costumer.\n"
			f"Account number: {self.account_num}\n"
			f"Status: {self.costumer}"
			)
			return msg
		elif self.costumer:
			msg = f"This person is a costumer, but still doesn't have an account number."
			return msg
		else:
			msg = f"This person in not a costumer yet."
			return msg

class Order(Costumer):
	"""Creating a class for coffee orders."""
	order_id_list = []
	def __init__(self, name, age, account_num, costumer, coffe_type, order_id):
		super().__init__(name, age, account_num, costumer)
		self.coffe_type = coffe_type
		self.order_id = int(order_id) + 1000

	def get_coffe_type(self):
		msg = "Coffee type is {}".format(self.coffe_type)
		return msg

	def get_order_id(self):
		order_id = self.order_id
		self.order_id_list.append(self.order_id)
		return self.order_id_list[self.order_id - 1001]

costumer = Costumer("Chloe", 19)
print(costumer.get_name())
print(costumer.get_account_num())

costumer_two = Order("Jackie", 29, coffe_type="Cappuccino", order_id="1", account_num="123213", costumer="Regular")
print(costumer_two.get_name())
# print(costumer_two.get_account_num())
print(costumer_two.get_costumer_status())
print(costumer_two.get_order_id())