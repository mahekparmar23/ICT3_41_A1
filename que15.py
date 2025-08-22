# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 09:39:11 2025

@author: DICT
"""


class Car:
    def __init__(self, brand, model, year, color, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.price = price

    def display_details(self):
        print(f"Brand   : {self.brand}")
        print(f"Model   : {self.model}")
        print(f"Year    : {self.year}")
        print(f"Color   : {self.color}")   
        print(f"Mileage : {self.mileage} kmpl")
        print(f"Price   : ₹{self.price:,}")          
        print("-" * 30)


class CarShowroom:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print(f"{car.brand} {car.model} has been added to the showroom.")

    def view_available_cars(self):
        if not self.inventory:
            print("No cars available in the showroom.")
        else:
            print("Available Cars in Showroom:")
            for i, car in enumerate(self.inventory):
                print(f"{i + 1}. {car.brand} {car.model}")

    def display_car_details(self, index):
        if 0 <= index < len(self.inventory):
            self.inventory[index].display_details()
        else:
            print("Invalid car index!")

    def sell_car(self, index):
        if 0 <= index < len(self.inventory):
            sold_car = self.inventory.pop(index)
            print(f"{sold_car.brand} {sold_car.model} has been sold!")
        else:
            print("Invalid car index!")


showroom = CarShowroom()

showroom.add_car(Car("Toyota", "Innova", 2022, "White", 12, 2000000))
showroom.add_car(Car("Hyundai", "Creta", 2021, "Black", 16, 1500000))
showroom.add_car(Car("Honda", "City", 2020, "Red", 17, 1200000))

while True:
    print("\n------ Menu ------")
    print("1. View available cars")
    print("2. Display car details")
    print("3. Sell a car")
    print("4. Buy (Add) a car")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        showroom.view_available_cars()

    elif choice == '2':
        index = int(input("Enter car index to view details: ")) - 1
        showroom.display_car_details(index)

    elif choice == '3':
        index = int(input("Enter car index to sell: ")) - 1
        showroom.sell_car(index)

    elif choice == '4':
        brand = input("Enter car brand: ")
        model = input("Enter car model: ")
        year = int(input("Enter manufacturing year: "))
        color = input("Enter car color: ")
        mileage = float(input("Enter mileage (kmpl): "))
        price = int(input("Enter price: ₹"))
        new_car = Car(brand, model, year, color, mileage, price)
        showroom.add_car(new_car)

    elif choice == '5':
        print("Thank you for visiting the Car Showroom!")
        break

    else:
        print("Invalid choice. Please try again.")
