class car:
    color = "red"
    model = "BMW"

    def drive(self):
        print("The car is driving")
    def stop(self):
        print("The car is stopped")

my_car = car()
my_car.drive()
my_car.stop()
print(my_car.color)
