class Car1:
    number_of_cars = 10
    color_of_car = "Red"

    def add_numbers(self,num1,num2,extraNum):
        sum = num1 + num2
        for num in extraNum:
            sum = sum+num
        print(sum)

calculator = Car1()
#print("Color of my car is "+audi.color_of_car)
calculator.add_numbers(25,45)
