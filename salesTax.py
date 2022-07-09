#task two day 1

# for every 115 square feet -> 1 gallon of paint, 8 hrs labour
# $20.00 per hr of labour
# program asks for square feet?
# price of paint per gallon?

class Paint():
    def __init__(self, charge_per_hour = 20, no_sqr_feet = 0, price_of_paint_per_gallon = 0) -> None:
        # here we initialize class variables
        # they apply to the whole block of class functions
        self.charge_per_hour = charge_per_hour # $20
        self.no_sqr_feet = no_sqr_feet #set initial value as 0
        self.price_of_paint_per_gallon = price_of_paint_per_gallon #set initial value as 0
        super().__init__()
    # destroy the class function
    def __del__(self):
        class_name = self.__class__.__name__
        pass

    def ask_for_feet_and_price(self):
        self.no_sqr_feet = int(input("Enter the number of Square feet required: "))
        self.price_of_paint_per_gallon = float(input("Enter the price of Paint per gallon in dollars($): ")) #float because currency is always in .00 most time eg $45.89

    def calculate_gallons_required(self):
        # for each 115 feet -> 8hrs -> 2000 per hour
        no_of_gallons_needed = self.no_sqr_feet / 115 # since 1 gallon = 115 square feet, we devide by 115 sqr feet to obtain the gallons needed
        no_of_hours_required = no_of_gallons_needed * 8
        cost_of_paint = no_of_gallons_needed * self.price_of_paint_per_gallon
        labour_charges = no_of_hours_required * self.charge_per_hour
        total_cost_of_paint_job = cost_of_paint + labour_charges
        # we the print the answers here
        print("No of gallons needed: \n" + str(int(no_of_gallons_needed)), "\n No of hours required: \n"+ str(int(round(no_of_hours_required,1))), "\n Cost for 1 labor hour: \n"+ "$" + str(self.charge_per_hour),"\n Cost of paint: \n"+ "$" + str(cost_of_paint), "\n Labour charges: \n"+ "$" +str(labour_charges), "\n Total Paint Cost: \n"+ "$" +str(total_cost_of_paint_job))

#here we initialize the class object and call the methods/functions
paint = Paint()
paint.ask_for_feet_and_price()
paint.calculate_gallons_required()

