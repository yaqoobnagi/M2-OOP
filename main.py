from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer

def run_inspection(car, meter, officer):
    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print(f"{car.make} {car.model} is legally parked.\n")

def main():
    print("===== Scenario 1: Legally Parked =====")
    car1 = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter1 = ParkingMeter(40)
    officer1 = PoliceOfficer("John Doe", "5678")
    run_inspection(car1, meter1, officer1)

    print("===== Scenario 2: Less Than 1 Hour Over =====")
    car2 = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter2 = ParkingMeter(60)
    officer2 = PoliceOfficer("Jane Smith", "1234")
    run_inspection(car2, meter2, officer2)

    print("===== Scenario 3: Multiple Hours Over =====")
    car3 = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter3 = ParkingMeter(60)
    officer3 = PoliceOfficer("James Brown", "4321")
    run_inspection(car3, meter3, officer3)

    print("===== Scenario 4: Multiple Cars =====")
    officer4 = PoliceOfficer("Sarah Green", "9999")

    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)),
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)),
        (ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)),
        (ParkedCar("Mazda", "3", "Blue", "MAZ321", 45), ParkingMeter(60)),
    ]

    for car, meter in cars:
        run_inspection(car, meter, officer4)

if __name__ == "__main__":
    main()
