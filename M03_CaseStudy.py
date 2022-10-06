class Vehicle:
	def __init__(self,type):
		self.type=type 
class Automobile(Vehicle):
	def __init__(self,type,year,make,model,doors,roof):
		super().__init__(type)
		self.year=year
		self.make=make
		self.model=model
		self.doors=doors
		self.roof=roof

type_i=input("What type of vehicle is it? :")
year_i=input("What is the year? :")
make_i=input("What is the make? :")
model_i=input("What is the model? :")
doors_i=input("Is it 2 or 4 door? :")
roof_i=input("Is it a solid or a sun roof? :")
A=Automobile(type_i,year_i,make_i,model_i,doors_i,roof_i)

print("\nVehicle Type :"+A.type)
print("\nYear :"+A.year)
print("\nMake :"+A.make)
print("\nModel :"+A.model)
print("\nNo of doors :"+A.doors)
print("\nType of roof :"+A.roof)