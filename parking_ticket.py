import math

class ParkingTicket:
    def __init__(self, car, officer, illegal_minutes):
        self.car = car  # composition (retain reference)
        self.officer_name = officer.name
        self.badge_number = officer.badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        hours = math.ceil(self.illegal_minutes / 60)
        if hours <= 1:
            return 25.0
        else:
            return 25.0 + (hours - 1) * 10.0

    def __str__(self):
        return ("--- PARKING TICKET ---\n"
                f"{self.car}\n"
                f"Illegal Minutes: {self.illegal_minutes}\n"
                f"Fine: ${self.fine:.2f}\n"
                f"Issued By: Officer {self.officer_name}, "
                f"Badge #{self.badge_number}\n")
