from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_cost(self):
        pass

    @abstractmethod
    def calculate_time(self):
        pass

class PassengerCar(Transport):
    def __init__(self, distance, speed, fuel_cost):
        self.distance = distance
        self.speed = speed
        self.fuel_cost = fuel_cost

    def calculate_cost(self):
        return self.distance * self.fuel_cost

    def calculate_time(self):
        return self.distance / self.speed

class CargoTruck(Transport):
    def __init__(self, distance, speed, fuel_cost, cargo_weight):
        self.distance = distance
        self.speed = speed
        self.fuel_cost = fuel_cost
        self.cargo_weight = cargo_weight

    def calculate_cost(self):
        return (self.distance  + (0.1*self.cargo_weight)) * self.fuel_cost

    def calculate_time(self):
        return self.distance / self.speed

class Bus(Transport):
    def __init__(self, distance, speed, fuel_cost, passengers):
        self.distance = distance
        self.speed = speed
        self.fuel_cost = fuel_cost
        self.passengers = passengers

    def calculate_cost(self):
        return (self.distance  + (0.05*self.passengers)) * self.fuel_cost

    def calculate_time(self):
        return self.distance / self.speed

import tkinter as tk

root = tk.Tk()
root.title("Калькулятор для автомобилистов")

transport_var = tk.IntVar()
tk.Radiobutton(root, text="Легковая машина", variable=transport_var, value=1).pack()
tk.Radiobutton(root, text="Грузовая машина", variable=transport_var, value=2).pack()
tk.Radiobutton(root, text="Пассажирская машина", variable=transport_var, value=3).pack()

tk.Label(root, text="Дистанция (км)").pack()
distance_entry = tk.Entry(root)
distance_entry.pack()

tk.Label(root, text="Скорость (км/ч)").pack()
speed_entry = tk.Entry(root)
speed_entry.pack()

tk.Label(root, text="Стоимость топлива (руб/л)").pack()
fuel_cost_entry = tk.Entry(root)
fuel_cost_entry.pack()

tk.Label(root, text="Вес машины (кг)").pack()
cargo_weight_entry = tk.Entry(root)
cargo_weight_entry.pack()

tk.Label(root, text="Пассажиры").pack()
passengers_entry = tk.Entry(root)
passengers_entry.pack()

def calculate_transport():
    distance = float(distance_entry.get())
    speed = float(speed_entry.get())
    fuel_cost = float(fuel_cost_entry.get())

    if transport_var.get() == 1:
        transport = PassengerCar(distance, speed, fuel_cost)
    elif transport_var.get() == 2:
        cargo_weight = float(cargo_weight_entry.get())
        transport = CargoTruck(distance, speed, fuel_cost, cargo_weight)
    elif transport_var.get() == 3:
        passengers = float(passengers_entry.get())
        transport = Bus(distance, speed, fuel_cost, passengers)

    cost_label.config(text="Стоимость: ₽%.2f" % transport.calculate_cost())
    time_label.config(text="Время: %.2f ч" % transport.calculate_time())

calculate_btn = tk.Button(root, text="Калькулятор", command=calculate_transport)
calculate_btn.pack()

cost_label = tk.Label(root, text="Стоимость: -")
cost_label.pack()

time_label = tk.Label(root, text="Время: -")
time_label.pack()

root.mainloop()