# Omondi is starting a new business, a car renting business.
#
# Omondi starts with five different Cars.
#
# Each car has a model, a year when it was released, a year when Omondi acquired it,
# the money made from that car, the car's plate number, and the number of times that
# it has been in business. (It has been rented).
#
# As Omondi is looking into expansion, he wants to be able to rent the cars, add new
# cars to his collection, remove the cars from his collection, count the number that each
# car has been rented out, and the money made from each car.
#
# Please help Omondi.




#this shows the profit omondi gained from his business and also the number of times the cr was rented
profit_gained = 0
number_of_times_rented_ = 0

#details of each of the cars which Omondi started business with:

Bentley = {"brand": "Bentley", "model": "Bentayga", "year of release": "2012", "year Omondi acquired the car": "2014",
           "money made from the car": profit_gained, "nmber plate": "X7 Raw",
           "number of times in bussiness": number_of_times_rented_}

Jeep = {"brand": "Jeep", "model": "Gladiator", "year of release": "2011", "year Omondi acquired the car": "2013",
           "money made from the car": profit_gained, "nmber plate": "GEB 560",
           "number of times in bussiness": number_of_times_rented_}

Toyota = {"brand": "Toyota", "model": "Avalon", "year of release": "2012", "year Omondi acquired the car": "2014",
           "money made from the car": profit_gained, "nmber plate": "ABC 1234",
           "number of times in bussiness": number_of_times_rented_}

Audi = {"brand": "Audi", "model": "A3 Sedan", "year of release": "2010", "year Omondi acquired the car": "2012",
           "money made from the car": profit_gained, "nmber plate": "15466",
           "number of times in bussiness": number_of_times_rented_}

BMW = {"brand": "BMW", "model": "X7", "year of release": "2016", "year Omondi acquired the car": "2018",
           "money made from the car": profit_gained, "nmber plate": "S3 BMR",
           "number of times in bussiness": number_of_times_rented_}

omondis_cars = {"name1":"Bentley", "name2":"Jeep", "name3":"Toyota", "name4":"Audi", "name5":"BMW"}

#asking the user if they would like to use the app
user_info = input('Hey Mr Omondi, would you love to use our app for car renting')
if user_info == "yes":
    print("This is what you can do on the app ")
    to_do =(input("click on D = Displaying the list of cars\n"
                 "click on A  = Adding a new car\n"
                 "click on R  = Removing car from the list\n"
                 "click on S  = Selecting the car you want to rent out and how many times have you rented the car\n"
                 "click on P  = How much has the car made\n"))

#I used this method to display all cars in the collection
    if to_do == "D":
       print(omondis_cars.values())
#used this method so that the can be able to input the details of the new car being added to the collection
    if to_do == "A":
        brand = input("Which car do you want to add to your collection?\n")
        model = input("Which car brand do you want to add to your collection?\n")
        release_year = int(input("Which year was the car released?\n"))
        year_acquired = int(input("Which year did you acquire the car?\n"))
        number_plate = input("What is the plate number of the car?\n")
#this is the dictionary which contains the details of the new care added to the collection
        new_car = {"car brand": brand, "car model": model, "year of release": release_year,
                   "year omundi acquired the car": year_acquired, "plate number": number_plate, "rented": number_of_times_rented_}
#I used this to add the new car brand into omondi_cars collection
        omondis_cars.update({"car brand": brand})
        print(omondis_cars)
# print the updated dictionary
        print("The new car has been added to your collection!!!")
#I used this pop function to remove a car from omondi_cars since its a dictionary
    if to_do == "R":
        deleted_item = omondis_cars.pop("name1")
        print(deleted_item)
        print("The car " + deleted_item + " has been removed from your collection.")
#I used this method to calculate the number of times a particular car has been rented out
    if to_do == "S":
        brand = input("Which car would you like to rent out?")
        amount = (input("At what price would you like to rent out the car?"))
        omondis_cars[brand]["amount"] += amount
        omondis_cars[brand]['number_of_times'] += 1
        print("You have rented " + brand + " " + str(omondis_cars[brand]['number_of_times']), "times")
#I used this method to calculate the amount obtained from a particular car
    if to_do == "P":
        car_cash = input("Which car do you want to find its profit?: ")
        omondis_cars[car_cash].get('Money_made')
        print("Your " + car_cash + " has made $" + str(omondis_cars[car_cash].get('amount')) + ' profit')
##I used this to ask him if he wants to use the app again
user_info = input("Would you like to use this app again?")
if user_info == "yes":
    print("Thank you for choosing to use this app, you can click on sign to access it as many times as you want ")
else:
    print("We had a great time with you on this app Mr Omondi,thank you for visiting us!!")# Omondi is starting a new business, a car renting business.
#
# Omondi starts with five different Cars.
#
# Each car has a model, a year when it was released, a year when Omondi acquired it,
# the money made from that car, the car's plate number, and the number of times that
# it has been in business. (It has been rented).
#
# As Omondi is looking into expansion, he wants to be able to rent the cars, add new
# cars to his collection, remove the cars from his collection, count the number that each
# car has been rented out, and the money made from each car.
#
# Please help Omondi.




#this shows the profit omondi gained from his business and also the number of times the cr was rented
profit_gained = 0
number_of_times_rented_ = 0

#details of each of the cars which Omondi started business with:

Bentley = {"brand": "Bentley", "model": "Bentayga", "year of release": "2012", "year Omondi acquired the car": "2014",
           "money made from the car": profit_gained, "nmber plate": "X7 Raw",
           "number of times in bussiness": number_of_times_rented_}

Jeep = {"brand": "Jeep", "model": "Gladiator", "year of release": "2011", "year Omondi acquired the car": "2013",
           "money made from the car": profit_gained, "nmber plate": "GEB 560",
           "number of times in bussiness": number_of_times_rented_}

Toyota = {"brand": "Toyota", "model": "Avalon", "year of release": "2012", "year Omondi acquired the car": "2014",
           "money made from the car": profit_gained, "nmber plate": "ABC 1234",
           "number of times in bussiness": number_of_times_rented_}

Audi = {"brand": "Audi", "model": "A3 Sedan", "year of release": "2010", "year Omondi acquired the car": "2012",
           "money made from the car": profit_gained, "nmber plate": "15466",
           "number of times in bussiness": number_of_times_rented_}

BMW = {"brand": "BMW", "model": "X7", "year of release": "2016", "year Omondi acquired the car": "2018",
           "money made from the car": profit_gained, "nmber plate": "S3 BMR",
           "number of times in bussiness": number_of_times_rented_}

omondis_cars = {"name1":"Bentley", "name2":"Jeep", "name3":"Toyota", "name4":"Audi", "name5":"BMW"}

#asking the user if they would like to use the app
user_info = input('Hey Mr Omondi, would you love to use our app for car renting')
if user_info == "yes":
    print("This is what you can do on the app ")
    to_do =(input("click on D = Displaying the list of cars\n"
                 "click on A  = Adding a new car\n"
                 "click on R  = Removing car from the list\n"
                 "click on S  = Selecting the car you want to rent out and how many times have you rented the car\n"
                 "click on P  = How much has the car made\n"))

#I used this method to display all cars in the collection
    if to_do == "D":
       print(omondis_cars.values())
#used this method so that the can be able to input the details of the new car being added to the collection
    if to_do == "A":
        brand = input("Which car do you want to add to your collection?\n")
        model = input("Which car brand do you want to add to your collection?\n")
        release_year = int(input("Which year was the car released?\n"))
        year_acquired = int(input("Which year did you acquire the car?\n"))
        number_plate = input("What is the plate number of the car?\n")
#this is the dictionary which contains the details of the new care added to the collection
        new_car = {"car brand": brand, "car model": model, "year of release": release_year,
                   "year omundi acquired the car": year_acquired, "plate number": number_plate, "rented": number_of_times_rented_}
#I used this to add the new car brand into omondi_cars collection
        omondis_cars.update({"car brand": brand})
        print(omondis_cars)
# print the updated dictionary
        print("The new car has been added to your collection!!!")
#I used this pop function to remove a car from omondi_cars since its a dictionary
    if to_do == "R":
        deleted_item = omondis_cars.pop("name1")
        print(deleted_item)
        print("The car " + deleted_item + " has been removed from your collection.")
#I used this method to calculate the number of times a particular car has been rented out
    if to_do == "S":
        brand = input("Which car would you like to rent out?")
        amount = (input("At what price would you like to rent out the car?"))
        omondis_cars[brand]["amount"] += amount
        omondis_cars[brand]['number_of_times'] += 1
        print("You have rented " + brand + " " + str(omondis_cars[brand]['number_of_times']), "times")
#I used this method to calculate the amount obtained from a particular car
    if to_do == "P":
        car_cash = input("Which car do you want to find its profit?: ")
        omondis_cars[car_cash].get('Money_made')
        print("Your " + car_cash + " has made $" + str(omondis_cars[car_cash].get('amount')) + ' profit')
##I used this to ask him if he wants to use the app again
user_info = input("Would you like to use this app again?")
if user_info == "yes":
    print("Thank you for choosing to use this app, you can click on sign to access it as many times as you want ")
else:
    print("We had a great time with you on this app Mr Omondi,thank you for visiting us!!")