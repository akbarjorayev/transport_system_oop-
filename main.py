import abc

# Abstrakt bazaviy sinf (Abstraksiya)
class Vehicle(abc.ABC):
    def __init__(self, make, model, year):
        self.__make = make  # Inkapsulyatsiya: private maydon
        self.__model = model
        self.__year = year

    # Getter metodlar
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setter metodlar
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        if year > 1900 and year <= 2026: # Oddiy validatsiya
            self.__year = year
        else:
            print("Yil noto'g'ri kiritildi.")

    @abc.abstractmethod
    def start_engine(self):
        pass

    @abc.abstractmethod
    def stop_engine(self):
        pass

    def display_info(self):
        return f"Make: {self.__make}, Model: {self.__model}, Year: {self.__year}"

# Vorislik: Car sinfi Vehicle sinfidan meros oladi
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.__num_doors = num_doors # Inkapsulyatsiya

    def get_num_doors(self):
        return self.__num_doors

    def set_num_doors(self, num_doors):
        self.__num_doors = num_doors

    # Metodni qayta aniqlash (Override)
    def start_engine(self):
        return f"{self.get_make()} {self.get_model()} avtomobil dvigateli ishga tushdi."

    def stop_engine(self):
        return f"{self.get_make()} {self.get_model()} avtomobil dvigateli o'chirildi."

    def display_info(self):
        return f"{super().display_info()}, Doors: {self.__num_doors}"

# Vorislik: Boat sinfi Vehicle sinfidan meros oladi
class Boat(Vehicle):
    def __init__(self, make, model, year, boat_type):
        super().__init__(make, model, year)
        self.__boat_type = boat_type # Inkapsulyatsiya

    def get_boat_type(self):
        return self.__boat_type

    def set_boat_type(self, boat_type):
        self.__boat_type = boat_type

    # Metodni qayta aniqlash (Override)
    def start_engine(self):
        return f"{self.get_make()} {self.get_model()} qayiq dvigateli ishga tushdi."

    def stop_engine(self):
        return f"{self.get_make()} {self.get_model()} qayiq dvigateli o'chirildi."

    def display_info(self):
        return f"{super().display_info()}, Type: {self.__boat_type}"

# Vorislik: Plane sinfi Vehicle sinfidan meros oladi
class Plane(Vehicle):
    def __init__(self, make, model, year, max_altitude):
        super().__init__(make, model, year)
        self.__max_altitude = max_altitude # Inkapsulyatsiya

    def get_max_altitude(self):
        return self.__max_altitude

    def set_max_altitude(self, max_altitude):
        self.__max_altitude = max_altitude

    # Metodni qayta aniqlash (Override)
    def start_engine(self):
        return f"{self.get_make()} {self.get_model()} samolyot dvigateli ishga tushdi."

    def stop_engine(self):
        return f"{self.get_make()} {self.get_model()} samolyot dvigateli o'chirildi."

    def display_info(self):
        return f"{super().display_info()}, Max Altitude: {self.__max_altitude} feet"


# Polimorfizmni ko'rsatish
print("\n--- Polimorfizm misoli ---")
vehicles = [
    Car("Toyota", "Camry", 2020, 4),
    Boat("Yamaha", "WaveRunner", 2022, "Jet Ski"),
    Plane("Boeing", "747", 2018, 45000),
    Car("Honda", "Civic", 2023, 4)
]

for vehicle in vehicles:
    print(vehicle.display_info())
    print(vehicle.start_engine())
    print(vehicle.stop_engine())
    print("-" * 20)

# Inkapsulyatsiya va getter/setter metodlari misoli
print("\n--- Inkapsulyatsiya misoli ---")
my_car = Car("BMW", "X5", 2021, 5)
print(f"Avtomobilning markasi: {my_car.get_make()}")
my_car.set_year(2024) # Yilni o'zgartirish
print(f"Yangi yil: {my_car.get_year()}")
my_car.set_year(1800) # Noto'g'ri yil kiritish
print(my_car.display_info())

# Vorislik misoli
print("\n--- Vorislik misoli ---")
my_boat = Boat("Mercury", "Sport", 2023, "Motorboat")
print(my_boat.display_info())
print(my_boat.start_engine())

# Metodlarni qayta aniqlash (Override) misoli
print("\n--- Metodlarni qayta aniqlash misoli ---")
my_plane = Plane("Airbus", "A380", 2019, 43000)
print(my_plane.start_engine())
