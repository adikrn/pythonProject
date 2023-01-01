class Car:

    def turn_on(self):
        print("Start the engine")
        return self

    def drive(self):
        print("Drive")
        return self

    def brake(self):
        print("Brake")
        return self

    def turn_off(self):
        print("Turn off")
        return self

car = Car()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()