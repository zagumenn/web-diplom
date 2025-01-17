from src.Models.Car import *



class CarController:
    @classmethod
    def get(cls):
        return Cars.select()

if __name__ == "__main__":
    for row in CarController.get():
        print(row.brand, row.model, row.color, row.state_number)